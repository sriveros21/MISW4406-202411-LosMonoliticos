import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Identifies the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize the database variable here
db = SQLAlchemy()


def import_domain_models():
    # Import DTOs from the infrastructure layer to ensure they are recognized by SQLAlchemy
    import PropiedadesdelosAlpes.modulos.cliente.infraestructura.dto
    import PropiedadesdelosAlpes.modulos.propiedades.infraestructura.dto


def registrar_handles():
    import PropiedadesdelosAlpes.modulos.cliente.aplicacion
    import PropiedadesdelosAlpes.modulos.propiedades.aplicacion


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
    registrar_handles()

    with app.app_context():
        db.create_all()  # Create database tables for our data models

    # Import and register your blueprints
    from . import cliente
    from . import propiedades

    app.register_blueprint(cliente.bp)
    app.register_blueprint(propiedades.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app

    # if __name__ == "__main__":
    # create_app().run(debug=True)
