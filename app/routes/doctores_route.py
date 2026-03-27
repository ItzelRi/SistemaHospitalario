from flask import jsonify, request, Blueprint
from app.controllers.doctores_controller import register_doctor, update_doctor, get_all_doctores, delete_doctor

doctor_bp = Blueprint("doctor_bp", __name__, url_prefix="/doctores")

@doctor_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    print("Aqui DATA!!", data)

    nombre = data.get("nombre")
    apellido = data.get("apellido")
    especialidad = data.get("especialidad")
    correo = data.get("correo")
    telefono = data.get("telefono")

    if not nombre or not apellido:
        return jsonify({"error": "El nombre y apellido son obligatorios"}), 400

    doctor_registered = register_doctor(
        nombre,
        apellido,
        especialidad,
        correo,
        telefono
    )

    return jsonify({
        "msg": "Doctor creado con exito!",
        "doctor": doctor_registered.to_dict()
    }), 200


@doctor_bp.route("/getAll", methods=["GET"])
def get_doctores():
    all_doctores = get_all_doctores()

    if not all_doctores:
        return jsonify({"msg": "No se encontro nada :("}), 200

    return jsonify({
        "msg": "Encontrados con exito!",
        "doctores": all_doctores
    }), 200


@doctor_bp.route("/update/<int:id_doctor>", methods=['PUT'])
def update(id_doctor):
    data = request.json

    doctor = update_doctor(id_doctor, data)

    if not doctor:
        return jsonify({"error": "doctor no encontrado :("}), 400

    return jsonify({"msg": "doctor actualizado con exito!"}), 200


@doctor_bp.route("/delete/<int:id_doctor>", methods=['DELETE'])
def delete(id_doctor):
    doctor = delete_doctor(id_doctor)

    if not doctor:
        return jsonify({"error": "doctor no encontrado :("}), 400

    return jsonify({"msg": "doctor eliminado con exito!"}), 200