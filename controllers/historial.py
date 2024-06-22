
from flask import Blueprint, jsonify, request
from services.mongodb_service import insert_historial, get_historial, update_historial, delete_historial

historial_bp = Blueprint('historial', __name__)

@historial_bp.route('/historial', methods=['POST'])
def crear_historial():
    historial = request.json
    resultado = insert_historial(historial)
    return jsonify({"id": str(resultado.inserted_id)}), 201

@historial_bp.route('/historial/<id>', methods=['GET'])
def obtener_historial(id):
    historial = get_historial(id)
    if historial:
        historial['_id'] = str(historial['_id'])
        return jsonify(historial)
    return jsonify({"error": "Historial no encontrado"}), 404

@historial_bp.route('/historial/<id>', methods=['PUT'])
def actualizar_historial(id):
    actualizacion = request.json
    resultado = update_historial(id, actualizacion)
    if resultado.modified_count:
        return jsonify({"mensaje": "Historial actualizado correctamente"})
    return jsonify({"error": "Historial no encontrado"}), 404

@historial_bp.route('/historial/<id>', methods=['DELETE'])
def eliminar_historial(id):
    resultado = delete_historial(id)
    if resultado.deleted_count:
        return jsonify({"mensaje": "Historial eliminado correctamente"})
    return jsonify({"error": "Historial no encontrado"}), 404