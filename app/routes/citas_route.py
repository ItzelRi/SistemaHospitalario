from flask import jsonify, request, Blueprint
from flask_cors import cross_origin  # 👈 IMPORTANTE
from app.controllers.citas_controller import register_cita, update_cita, get_all_citas, delete_cita
import datetime

cita_bp = Blueprint("cita_bp", __name__, url_prefix="/citas")


@cita_bp.route("/register", methods=["POST", "OPTIONS"])  # 👈 AQUI
@cross_origin()  # 👈 Y AQUI
def register():

    # 🔥 RESPUESTA AL PREFLIGHT (CORS)
    if request.method == "OPTIONS":
        return '', 200

    data = request.json
    print("Aqui DATA!!", data)

    id_paciente = data.get("id_paciente")
    id_doctor = data.get("id_doctor")
    motivo = data.get("motivo")

    print(data.get("fecha"))
    print(data.get("hora"))

    fecha = None
    if data.get("fecha"):
        splited_date = data["fecha"].split("-")

        fecha = datetime.date(
            int(splited_date[0]),
            int(splited_date[1]),
            int(splited_date[2])
        )

    hora = None
    if data.get("hora"):
        splited_time = data["hora"].split(":")

        hora = datetime.time(
            int(splited_time[0]),
            int(splited_time[1]),
            int(splited_time[2])
        )

    if not id_paciente or not id_doctor or not fecha or not hora:
        return jsonify({"error": "Datos basicos de la cita son obligatorios"}), 400

    if not motivo:
        motivo = ""

    cita_registered = register_cita(
        id_paciente,
        id_doctor,
        fecha,
        hora,
        motivo
    )

    return jsonify({
        "msg": "Cita creada con exito!",
        "cita": cita_registered.to_dict()
    }), 200


# 🔽 OPCIONAL pero recomendado (consistencia)
@cita_bp.route("/getAll", methods=["GET", "OPTIONS"])
@cross_origin()
def get_citas():
    if request.method == "OPTIONS":
        return '', 200

    all_citas = get_all_citas()

    if not all_citas:
        return jsonify({"msg": "No se encontro nada :("}), 200

    return jsonify({
        "msg": "Encontrados con exito!",
        "citas": all_citas
    }), 200


@cita_bp.route("/update/<int:id_cita>", methods=['PUT', 'OPTIONS'])
@cross_origin()
def update(id_cita):
    if request.method == "OPTIONS":
        return '', 200

    data = request.json

    cita = update_cita(id_cita, data)

    if not cita:
        return jsonify({"error": "cita no encontrada :("}), 400

    return jsonify({"msg": "cita actualizada con exito!"}), 200


@cita_bp.route("/delete/<int:id_cita>", methods=['DELETE', 'OPTIONS'])
@cross_origin()
def delete(id_cita):
    if request.method == "OPTIONS":
        return '', 200

    cita = delete_cita(id_cita)

    if not cita:
        return jsonify({"error": "cita no encontrada :("}), 400

    return jsonify({"msg": "cita eliminada con exito!"}), 200