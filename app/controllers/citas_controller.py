from app.database.db import db
from app.models.citas_model import Citas

def register_cita(id_paciente, id_doctor, fecha, hora, motivo):
    print("Hola, desde controlador", fecha, hora)

    cita = Citas(
        id_paciente=id_paciente,
        id_doctor=id_doctor,
        fecha=fecha,
        hora=hora,
        motivo=motivo
    )

    print("Diccionario que guarda el controller", cita.to_dict())

    db.session.add(cita)
    db.session.commit()
    return cita


def get_all_citas():
    all_citas = Citas.query.all()
    all2 = [cita.to_dict() for cita in all_citas]

    print("Desde controller, digo: ", all2)
    return all2


def update_cita(id_cita, updated_data):
    cita_to_update = Citas.query.get(id_cita)

    if not cita_to_update:
        return None

    for key, value in updated_data.items():
        setattr(cita_to_update, key, value)

    db.session.commit()
    return cita_to_update


def delete_cita(id_cita):
    cita = Citas.query.get(id_cita)

    if not cita:
        return None

    db.session.delete(cita)
    db.session.commit()
    return cita