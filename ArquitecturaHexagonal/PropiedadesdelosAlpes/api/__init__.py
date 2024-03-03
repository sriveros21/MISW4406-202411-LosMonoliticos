import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Identifies the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

#Register Handlers
def registrar_handlers():
    import PropiedadesdelosAlpes.modulos.auditorias.aplicacion
    

# Initialize the database variable here
db = SQLAlchemy()

def import_domain_models():
    # Import DTOs from the infrastructure layer to ensure they are recognized by SQLAlchemy
    import PropiedadesdelosAlpes.modulos.propiedades.infraestructura.dto
    import PropiedadesdelosAlpes.modulos.propiedades.aplicacion.dto

def create_app(configuracion=None):
    app = Flask(__name__, instance_relative_config=True)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'propiedades_alpes.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize 'db' with the app
    from PropiedadesdelosAlpes.config.db import init_db
    init_db(app)

    from PropiedadesdelosAlpes.config.db import db
    import_domain_models()
    with app.app_context():
        db.create_all() 
        from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
        from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
        from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.mapeadores import MapeadorPropiedades

        fabrica_repositorio = FabricaRepositorio(db_session=db.session)
        repositorio_propiedades = fabrica_repositorio.crear_repositorio_propiedades()
        mapeador_propiedad = MapeadorPropiedades(db.session)
        app.extensions['repositorio_propiedades'] = repositorio_propiedades
        app.extensions['mapeador_propiedad'] = mapeador_propiedad

        # Storing ServicioPropiedad in app.extensions for global access
        servicio_propiedad = ServicioPropiedad(repositorio=repositorio_propiedades, mapeador=mapeador_propiedad)
        app.extensions['servicio_propiedad'] = servicio_propiedad

    # Import and register your blueprints
    from . import cliente, propiedades, auditorias
    app.register_blueprint(cliente.bp)
    app.register_blueprint(propiedades.bp)
    app.register_blueprint(auditorias.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app

#if __name__ == "__main__":
    create_app().run(debug=True)
