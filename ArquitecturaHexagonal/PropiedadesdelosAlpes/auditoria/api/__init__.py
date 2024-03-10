import os
from flask import Flask, jsonify, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

# Identifies the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

def register_handlers():
    import PropiedadesdelosAlpes.auditoria.modulos.aplicacion

def import_domain_models():
    # Import DTOs from the infrastructure layer to ensure they are recognized by SQLAlchemy
    import PropiedadesdelosAlpes.auditoria.modulos.infraestructura.dto
    import PropiedadesdelosAlpes.auditoria.modulos.aplicacion.dto

def register_event_consumers(app):
    import threading
    import PropiedadesdelosAlpes.auditoria.modulos.infraestructura.consumidores as auditorias

    #SUBSCRIBING TO EVENTS
    threading.Thread(target=auditorias.suscribirse_a_eventos, args=[app]).start()

    #SUBSCRIBING TO COMMANDS
    threading.Thread(target=auditorias.suscribirse_a_comandos, args=[app]).start()

def create_app(configuracion={}):
    
    app = Flask(__name__, instance_relative_config=True)

    # Database Configuration
    app.secret_key = 'secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING', False)

    # Initialize 'db' with the app
    from PropiedadesdelosAlpes.auditoria.config.db import init_db, database_connection
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection(configuracion, basedir=basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_db(app)

    from PropiedadesdelosAlpes.auditoria.config.db import db

    import_domain_models()
    register_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            register_event_consumers(app)
        
        from PropiedadesdelosAlpes.auditoria.modulos.sagas.aplicacion.coordinadores.saga_auditorias import CoordinadorAuditorias
        CoordinadorAuditorias()

    from . import auditorias

    app.register_blueprint(auditorias.bp)

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
