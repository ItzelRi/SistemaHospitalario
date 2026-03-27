from flask import Flask
from .config import Config
from .database.db import db
from flask_migrate import Migrate
from flask_cors import CORS

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

    from app.models.pacientes_model import Pacientes
    from app.models.doctores_model import Doctores
    from app.models.citas_model import Citas

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.pacientes_route import paciente_bp
    from app.routes.doctores_route import doctor_bp
    from app.routes.citas_route import cita_bp

    app.register_blueprint(paciente_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(cita_bp)
  
    return app