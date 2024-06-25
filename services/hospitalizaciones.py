from flask import request, jsonify
from config.mongodb import mongo
from datetime import datetime
from bson.objectid import ObjectId
from flask_app import mongo
from config.mongodb import mongo

def set_hospitalizacion_service():
    data = request.json
    hospitalizacion = {
        "_id": ObjectId(),
        "id_paciente": ObjectId(data["id_paciente"]),
        "fecha_ingreso": datetime.strptime(data["fecha_ingreso"], "%Y-%m-%d"),
        "fecha_alta": datetime.strptime(data["fecha_alta"], "%Y-%m-%d"),
        "detalles_tratamiento": data.get("detalles_tratamiento", ""),
        "tratamientos_recibidos": []
    }
    mongo.db.hospitalizacion.insert_one(hospitalizacion)
    return jsonify({"message": "Hospitalización guardada"})

def get_hospitalizaciones_service():
    hospitalizaciones = mongo.db.hospitalizacion.find()
    response = []
    for hospitalizacion in hospitalizaciones:
        hospitalizacion['_id'] = str(hospitalizacion['_id'])
        response.append(hospitalizacion)
    return jsonify(response)