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

def create_app(configuracion=None):
    app = Flask(__name__, instance_relative_config=True)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'propiedades_alpes.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize 'db' with the app
    from PropiedadesdelosAlpes.config.db import init_db
    init_db(app)

    from PropiedadesdelosAlpes.config.db import db

    with app.app_context():
        import_domain_models()
        db.create_all()  # Create database tables for our data models

    # Import and register your blueprints
    from . import cliente, propiedades
    app.register_blueprint(cliente.bp)
    app.register_blueprint(propiedades.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
