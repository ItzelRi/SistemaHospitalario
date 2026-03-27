from app.database.db import db

class Citas(db.Model):
    __tablename__ = "citas"
    id_cita = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey("pacientes.id_paciente"))
    id_doctor = db.Column(db.Integer, db.ForeignKey("doctores.id_doctor"))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    motivo = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id_cita": self.id_cita,
            "id_paciente": self.id_paciente,
            "id_doctor": self.id_doctor,
            "fecha": self.fecha.isoformat() if self.fecha else None,   # convierte date a "YYYY-MM-DD"
            "hora": self.hora.strftime("%H:%M:%S") if self.hora else None,  # convierte time a "HH:MM:SS"
            "motivo": self.motivo,
        }