from flask import jsonify, request
from datetime import datetime
from bson.objectid import ObjectId
from flask_app import mongo
from config.mongodb import mongo

def set_historial_medico_service():
    data = request.json
    historial_medico = {
        "_id": ObjectId(),
        "id_paciente": ObjectId(data["id_paciente"]),
        "diagnosticos": [],
        "tratamientos_previos": []
    }
    mongo.db.historial_medico.insert_one(historial_medico)
    return jsonify({"message": "Historial médico guardado"})

def get_historial_medico_service():
    historiales = mongo.db.historial_medico.find()
    response = []
    for historial in historiales:
        historial['_id'] = str(historial['_id'])
        response.append(historial)
    return jsonify(response)