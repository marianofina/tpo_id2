from flask import Blueprint, jsonify, request
from services.tratamientos import *
from bson.objectid import ObjectId
from flask_app import mongo

tratamientos_bp = Blueprint('tratamientos', __name__)

@tratamientos_bp.route('/tratamientos', methods=['POST'])
def set_tratamiento():
    return set_tratamiento_service()


@tratamientos_bp.route('/tratamientos', methods=['GET'])
def get_tratamientos():
    return get_tratamientos_service()
@tratamientos_bp.route('/tratamientos', methods=['POST'])
def add_tratamiento():
    data = request.json
    mongo.db.tratamientos.insert_one(data)
    return jsonify({"message": "Tratamiento guardado"}), 201

@tratamientos_bp.route('/tratamientos/<id>', methods=['GET'])
def get_tratamiento(id):
    tratamiento = mongo.db.tratamientos.find_one({"_id": ObjectId(id)})
    if tratamiento:
        tratamiento["_id"] = str(tratamiento["_id"])
        return jsonify(tratamiento), 200
    else:
        return jsonify({"error": "Tratamiento no encontrado"}), 404