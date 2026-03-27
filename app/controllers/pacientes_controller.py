from app.database.db import db
from app.models.pacientes_model import Pacientes 


def register_paciente(nombre, apellido, correo, telefono, fecha_nacimiento):
    print("Hola, desde controlador", nombre)

    paciente = Pacientes(
        nombre=nombre,
        apellido=apellido,
        correo=correo,
        telefono=telefono,
        fecha_nacimiento=fecha_nacimiento,
    )

    print("Diccionario que guarda el controller", paciente.to_dict())

    db.session.add(paciente)
    db.session.commit()
    return paciente


def get_all_pacientes():
    all_pacientes = Pacientes.query.all()
    all2 = [paciente.to_dict() for paciente in all_pacientes]

    print("Desde controller, digo: ", all2)
    return all2


def update_paciente(id_paciente, updated_data):
    paciente_to_update = Pacientes.query.get(id_paciente)

    if not paciente_to_update:
        return None

    for key, value in updated_data.items():  
        setattr(paciente_to_update, key, value)

    db.session.commit()
    return paciente_to_update


def delete_paciente(id_paciente):
    paciente = Pacientes.query.get(id_paciente)

    if not paciente:
        return None

    db.session.delete(paciente)
    db.session.commit()
    return paciente