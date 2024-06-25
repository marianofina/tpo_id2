from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.hospitalizaciones import *

hospitalizaciones_bp = Blueprint('hospitalizaciones', __name__)


@hospitalizaciones_bp.route('/hospitalizaciones', methods=['POST'])
def crear_hospitalizaciones():
    try:
        hospitalizaciones = request.json
        resultado = insert_hospitalizaciones(hospitalizaciones)
        return jsonify({"id": str(resultado.inserted_id)}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al crear hospitalizaciones"}), 400


@hospitalizaciones_bp.route('/hospitalizaciones/<id>', methods=['GET'])
@jwt_required()
def obtener_hospitalizaciones(id):
    try:
        hospitalizaciones = get_hospitalizaciones(id)
        current_user_id = get_jwt_identity()
        if hospitalizaciones['id_paci'] == current_user_id[0]:
            hospitalizaciones['_id'] = str(hospitalizaciones['_id'])
            for i in range(len(hospitalizaciones["tratamientos"])):
                hospitalizaciones["tratamientos"][i] = str(hospitalizaciones["tratamientos"][i])
            return jsonify(hospitalizaciones)
        return jsonify({"error": "No tiene permisos para modificar ver la hospitalización"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener hospitalizaciones"}), 400


@hospitalizaciones_bp.route('/hospitalizaciones/<id>', methods=['PUT'])
def actualizar_hospitalizaciones(id):
    try:
        actualizacion = request.json
        resultado = update_hospitalizaciones(id, actualizacion)
        if resultado.modified_count:
            return jsonify({"mensaje": "Hospitalizaciones actualizado correctamente"})
        return jsonify({"error": "Hospitalizaciones no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al actualizar hospitalizaciones"}), 400


@hospitalizaciones_bp.route('/hospitalizaciones/<id>', methods=['DELETE'])
def eliminar_hospitalizaciones(id):
    try:
        resultado = delete_hospitalizaciones(id)
        if resultado.deleted_count:
            return jsonify({"mensaje": "Hospitalizaciones eliminado correctamente"})
        return jsonify({"error": "Hospitalizaciones no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al eliminar hospitalizaciones"}), 400
