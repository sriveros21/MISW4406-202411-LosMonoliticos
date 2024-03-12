import os
from flask import Flask, session

# Identifies the base directory
basedir = os.path.abspath(os.path.dirname(__file__))


def register_handlers():
    import PropiedadesdelosAlpes.cliente.modulos.aplicacion


def import_domain_models():
    # Import DTOs from the infrastructure layer to ensure they are recognized by SQLAlchemy
    import PropiedadesdelosAlpes.cliente.modulos.infraestructura.dto


def register_event_consumers(app):
    import threading
    import PropiedadesdelosAlpes.cliente.modulos.infraestructura.consumidores as cliente

    # SUBSCRIBING TO EVENTS
    threading.Thread(target=cliente.suscribirse_a_eventos, args=[app]).start()

    # SUBSCRIBING TO COMMANDS
    threading.Thread(target=cliente.suscribirse_a_comandos, args=[app]).start()


def create_app(configuracion={}):
    app = Flask(__name__, instance_relative_config=True)

    # Database Configuration
    app.secret_key = 'secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING', False)

    # Initialize 'db' with the app
    from PropiedadesdelosAlpes.cliente.config.db import init_db, database_connection

    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection(configuracion, basedir=basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_db(app)

    from PropiedadesdelosAlpes.cliente.config.db import db

    import_domain_models()
    register_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            register_event_consumers(app)

        from PropiedadesdelosAlpes.cliente.modulos.sagas.aplicacion.coordinadores.saga_auditorias import CoordinadorAuditorias
        CoordinadorAuditorias()

    from . import cliente

    app.register_blueprint(cliente.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    @app.route('/logout')
    def logout():
        db.session.remove()
        session.clear()
        return {"status": "downm"}

    return app
