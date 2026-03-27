from app.database.db import db
from app.models.doctores_model import Doctores  

def register_doctor(nombre, apellido, especialidad, correo, telefono):
    print("Hola, desde controlador", nombre)

    doctor = Doctores(
        nombre=nombre,
        apellido=apellido,
        especialidad=especialidad,
        correo=correo,
        telefono=telefono
    )

    print("Diccionario que guarda el controller", doctor.to_dict())

    db.session.add(doctor)
    db.session.commit()
    return doctor


def get_all_doctores():
    all_doctores = Doctores.query.all()
    all2 = [doctor.to_dict() for doctor in all_doctores]

    print("Desde controller, digo: ", all2)
    return all2


def update_doctor(id_doctor, updated_data): 
    doctor_to_update = Doctores.query.get(id_doctor)

    if not doctor_to_update:
        return None

    for key, value in updated_data.items():  # Iteramos
        setattr(doctor_to_update, key, value)

    db.session.commit()
    return doctor_to_update


def delete_doctor(id_doctor):
    doctor = Doctores.query.get(id_doctor)

    if not doctor:
        return None

    db.session.delete(doctor)
    db.session.commit()
    return doctor