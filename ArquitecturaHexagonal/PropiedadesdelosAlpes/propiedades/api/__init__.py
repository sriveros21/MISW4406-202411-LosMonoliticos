import os
from flask import Flask, jsonify, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

# Identifies the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

def register_handlers():
    import PropiedadesdelosAlpes.propiedades.modulos.aplicacion

def import_domain_models():
    # Import DTOs from the infrastructure layer to ensure they are recognized by SQLAlchemy
    import PropiedadesdelosAlpes.propiedades.modulos.infraestructura.dto
    import PropiedadesdelosAlpes.propiedades.modulos.aplicacion.dto

def register_event_consumers(app):
    import threading
    import PropiedadesdelosAlpes.propiedades.modulos.infraestructura.consumidores as propiedades

    #SUBSCRIBING TO EVENTS
    threading.Thread(target=propiedades.suscribirse_a_eventos).start()
    threading.Thread(target=auditorias.suscribirse_a_eventos, args=[app]).start()
    threading.Thread(target=cliente.suscribirse_a_eventos).start()

    #SUBSCRIBING TO COMMANDS
    threading.Thread(target=propiedades.suscribirse_a_comandos).start()
    threading.Thread(target=auditorias.suscribirse_a_comandos, args=[app]).start()
    threading.Thread(target=cliente.suscribirse_a_comandos).start()

def create_app(configuracion={}):
    
    app = Flask(__name__, instance_relative_config=True)

    # Database Configuration
    app.secret_key = 'secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING', False)

    # Initialize 'db' with the app
    from PropiedadesdelosAlpes.config.db import init_db, database_connection
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection(configuracion, basedir=basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_db(app)

    from PropiedadesdelosAlpes.config.db import db

    import_domain_models()
    register_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            register_event_consumers(app)
        
    from . import propiedades

    app.register_blueprint(propiedades.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}
    
    @app.route('/logout')
    def logout():
        db.session.remove()
        session.clear()
        return {"status": "downm"}
        #return redirect(url_for('login'))

    return app
