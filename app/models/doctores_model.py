from app.database.db import db

class Doctores(db.Model):
    __tablename__ = "doctores"

    id_doctor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=True)
    apellido = db.Column(db.String(100), nullable=True)
    especialidad = db.Column(db.String(100), nullable=True)
    correo = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)

    def to_dict(self):
        doctor = {
            'id_doctor': self.id_doctor,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'especialidad': self.especialidad,
            'correo': self.correo,
            'telefono': self.telefono
        }

        return doctor