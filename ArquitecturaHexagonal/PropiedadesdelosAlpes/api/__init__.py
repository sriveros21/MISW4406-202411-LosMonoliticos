import os
from flask import Flask, jsonify, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

# Identifies the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

def register_handlers():
    import PropiedadesdelosAlpes.modulos.propiedades.aplicacion
    import PropiedadesdelosAlpes.modulos.cliente.aplicacion
    import PropiedadesdelosAlpes.modulos.auditorias.aplicacion

def import_domain_models():
    # Import DTOs from the infrastructure layer to ensure they are recognized by SQLAlchemy
    import PropiedadesdelosAlpes.modulos.propiedades.infraestructura.dto
    import PropiedadesdelosAlpes.modulos.propiedades.aplicacion.dto
    import PropiedadesdelosAlpes.modulos.cliente.infraestructura.dto
    import PropiedadesdelosAlpes.modulos.cliente.aplicacion.dto
    import PropiedadesdelosAlpes.modulos.auditorias.infraestructura.dto
    import PropiedadesdelosAlpes.modulos.auditorias.aplicacion.dto

def register_event_consumers():
    import threading
    import PropiedadesdelosAlpes.modulos.propiedades.infraestructura.consumidores as propiedades
    import PropiedadesdelosAlpes.modulos.cliente.infraestructura.consumidores as cliente
    import PropiedadesdelosAlpes.modulos.auditorias.infraestructura.consumidores as auditorias

    #SUBSCRIBING TO EVENTS
    threading.Thread(target=propiedades.suscribirse_a_eventos).start()
    threading.Thread(target=auditorias.suscribirse_a_eventos).start()
    threading.Thread(target=cliente.suscribirse_a_eventos).start()

    #SUBSCRIBING TO COMMANDS
    threading.Thread(target=propiedades.suscribirse_a_comandos).start()
    threading.Thread(target=auditorias.suscribirse_a_comandos).start()
    threading.Thread(target=cliente.suscribirse_a_comandos).start()

def create_app(configuracion={}):
    
    app = Flask(__name__, instance_relative_config=True)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'propiedades_alpes.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING', False)

    # Initialize 'db' with the app
    from PropiedadesdelosAlpes.config.db import init_db
    init_db(app)

    from PropiedadesdelosAlpes.config.db import db

    import_domain_models()
    register_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            register_event_consumers()
        
    from . import propiedades
    from . import cliente
    from . import auditorias

    app.register_blueprint(propiedades.bp)
    app.register_blueprint(cliente.bp)
    app.register_blueprint(auditorias.bp)


        # from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
        # from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
        # from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.mapeadores import MapeadorPropiedades

        # fabrica_repositorio = FabricaRepositorio(db_session=db.session)
        # repositorio_propiedades = fabrica_repositorio.crear_repositorio_propiedades()
        # mapeador_propiedad = MapeadorPropiedades(db.session)
        # app.extensions['repositorio_propiedades'] = repositorio_propiedades
        # app.extensions['mapeador_propiedad'] = mapeador_propiedad

        # # Storing ServicioPropiedad in app.extensions for global access
        # servicio_propiedad = ServicioPropiedad(repositorio=repositorio_propiedades, mapeador=mapeador_propiedad)
        # app.extensions['servicio_propiedad'] = servicio_propiedad
        # handler_crear_propiedad = CrearPropiedadHandler(repositorio_propiedades, mapeador_propiedad)
        # app.extensions['handler_crear_propiedad'] = handler_crear_propiedad

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