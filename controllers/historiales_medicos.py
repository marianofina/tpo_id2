from flask import Blueprint, jsonify, request
from services.historiales_medicos import *
from bson.objectid import ObjectId
from flask_app import mongo

historial_medico_bp = Blueprint('historial_medico', __name__)

@historial_medico_bp.route('/historial_medico', methods=['POST'])
def add_historial_medico():
    data = request.json
    mongo.db.historial_medico.insert_one(data)
    return jsonify({"message": "Historial médico guardado"}), 201

@historial_medico_bp.route('/historial_medico', methods=['GET'])
def get_historiales_medicos():
    historiales = mongo.db.historial_medico.find()
    response = []
    for historial in historiales:
        historial['_id'] = str(historial['_id'])
        response.append(historial)
    return jsonify(response)

@historial_medico_bp.route('/historial_medico/<id>', methods=['GET'])
def get_historial_medico(id):
    historial = mongo.db.historial_medico.find_one({"_id": ObjectId(id)})
    if historial:
        historial["_id"] = str(historial["_id"])
        return jsonify(historial), 200
    else:
        return jsonify({"error": "Historial médico no encontrado"}), 404