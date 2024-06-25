from flask import Blueprint, jsonify, request
from services.hospitalizaciones import *
from bson.objectid import ObjectId
from flask_app import mongo

hospitalizaciones_bp = Blueprint('hospitalizaciones', __name__)

@hospitalizaciones_bp.route('/hospitalizaciones', methods=['POST'])
def add_hospitalizacion():
    data = request.json
    mongo.db.hospitalizacion.insert_one(data)
    return jsonify({"message": "Hospitalización guardada"}), 201

@hospitalizaciones_bp.route('/hospitalizaciones', methods=['GET'])
def get_hospitalizaciones():
    hospitalizaciones = mongo.db.hospitalizacion.find()
    response = []
    for hospitalizacion in hospitalizaciones:
        hospitalizacion['_id'] = str(hospitalizacion['_id'])
        response.append(hospitalizacion)
    return jsonify(response)

@hospitalizaciones_bp.route('/hospitalizaciones/<id>', methods=['GET'])
def get_hospitalizacion(id):
    hospitalizacion = mongo.db.hospitalizacion.find_one({"_id": ObjectId(id)})
    if hospitalizacion:
        hospitalizacion["_id"] = str(hospitalizacion["_id"])
        return jsonify(hospitalizacion), 200
    else:
        return jsonify({"error": "Hospitalización no encontrada"}), 404

