from flask import jsonify, request, Blueprint
from app.controllers.pacientes_controller import register_paciente, update_paciente, get_all_pacientes, delete_paciente
import datetime
from datetime import datetime


paciente_bp = Blueprint("paciente_bp", __name__, url_prefix="/pacientes")

@paciente_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    print("Aqui DATA!!", data)

    nombre = data.get("nombre")
    apellido = data.get("apellido")
    correo = data.get("correo")
    telefono = data.get("telefono")

    print(data.get("fecha_nacimiento"))

    fecha_nacimiento = None
    if data.get("fecha_nacimiento"):
        fecha_nacimiento = datetime.fromisoformat(
            data["fecha_nacimiento"].replace("Z", "")
        ).date()
       

    print("Fecha aqui!!", fecha_nacimiento)

    if not nombre or not apellido:
        return jsonify({"error": "El nombre y apellido son obligatorios"}), 400

    paciente_registered = register_paciente(
        nombre,
        apellido,
        correo,
        telefono,
        fecha_nacimiento,
    )

    return jsonify({
        "msg": "Paciente creado con exito!",
        "paciente": paciente_registered.to_dict()
    }), 200


@paciente_bp.route("/getAll", methods=["GET"])
def get_pacientes():
    all_pacientes = get_all_pacientes()

    if not all_pacientes:
        return jsonify({"msg": "No se encontro nada :("}), 200

    return jsonify({
        "msg": "Encontrados con exito!",
        "pacientes": all_pacientes
    }), 200


@paciente_bp.route("/update/<int:id_paciente>", methods=['PUT'])
def update(id_paciente):
    data = request.json

    if data.get("fecha_nacimiento"):
        fecha_nacimiento = datetime.fromisoformat(
            data["fecha_nacimiento"].replace("Z", "")
        ).date()
        data["fecha_nacimiento"]= fecha_nacimiento

    paciente = update_paciente(id_paciente, data)

    if not paciente:
        return jsonify({"error": "paciente no encontrado :("}), 400

    return jsonify({"msg": "paciente actualizado con exito!"}), 200


@paciente_bp.route("/delete/<int:id_paciente>", methods=['DELETE'])
def delete(id_paciente):
    paciente = delete_paciente(id_paciente)

    if not paciente:
        return jsonify({"error": "paciente no encontrado :("}), 400

    return jsonify({"msg": "paciente eliminado con exito!"}), 200