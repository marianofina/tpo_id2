from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.tratamientos import *

tratamientos_bp = Blueprint('tratamientos', __name__)


@tratamientos_bp.route('/tratamiento', methods=['POST'])
def crear_tratamiento():
    try:
        tratamiento = request.json
        resultado = insert_tratamiento(tratamiento)
        return jsonify({"id": str(resultado.inserted_id)}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al crear tratamiento"}), 400


@tratamientos_bp.route('/tratamiento/<id>', methods=['GET'])
@jwt_required()
def obtener_tratamiento(id):
    try:
        tratamiento = get_tratamiento(id)
        current_user_id = get_jwt_identity()
        if tratamiento['paci_id'] == current_user_id[0]:
            tratamiento['_id'] = str(tratamiento['_id'])
            return jsonify(tratamiento)
        return jsonify({"error": "No tiene permisos para modificar ver la hospitalización"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener tratamiento"}), 400


@tratamientos_bp.route('/tratamiento/<id>', methods=['PUT'])
def actualizar_tratamiento(id):
    try:
        actualizacion = request.json
        resultado = update_tratamiento(id, actualizacion)
        if resultado.modified_count:
            return jsonify({"mensaje": "Tratamiento actualizado correctamente"})
        return jsonify({"error": "Tratamiento no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al actualizar tratamiento"}), 400


@tratamientos_bp.route('/tratamiento/<id>', methods=['DELETE'])
def eliminar_tratamiento(id):
    try:
        resultado = delete_tratamiento(id)
        if resultado.deleted_count:
            return jsonify({"mensaje": "Tratamiento eliminado correctamente"})
        return jsonify({"error": "Tratamiento no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al eliminar tratamiento"}), 400
