from flask import Blueprint, jsonify, request
from services.comentarios_trat import *

comentarios_trat_bp = Blueprint('comentarios_trat', __name__)


@comentarios_trat_bp.route('/comentarios_trat', methods=['POST'])
def crear_comentarios_trat():
    try:
        comentarios_trat = request.json
        resultado = insert_comentarios_trat(comentarios_trat)
        return jsonify({"id": str(resultado.inserted_id)}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al crear comentario"}), 400


@comentarios_trat_bp.route('/comentarios_trat/<id>', methods=['GET'])
def obtener_comentarios_trat(id):
    try:
        comentarios_trat = get_comentarios_trat(id)
        if comentarios_trat:
            comentarios_trat['_id'] = str(comentarios_trat['_id'])
            comentarios_trat['id_trat'] = str(comentarios_trat['id_trat'])
            return jsonify(comentarios_trat)
        return jsonify({"error": "Comentario no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al obtener comentario"}), 400


@comentarios_trat_bp.route('/comentarios_trat/<id>', methods=['PUT'])
def actualizar_comentarios_trat(id):
    try:
        actualizacion = request.json
        resultado = update_comentarios_trat(id, actualizacion)
        if resultado.modified_count:
            return jsonify({"mensaje": "Comentario actualizado correctamente"})
        return jsonify({"error": "Comentario no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al actualizar comentario"}), 400


@comentarios_trat_bp.route('/comentarios_trat/<id>', methods=['DELETE'])
def eliminar_comentarios_trat(id):
    try:
        resultado = delete_comentarios_trat(id)
        if resultado.deleted_count:
            return jsonify({"mensaje": "Comentario eliminado correctamente"})
        return jsonify({"error": "Comentario no encontrado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Error al eliminar comentario"}), 400
