from flask import request, jsonify
from config.mongodb import mongo
from datetime import datetime
from bson.objectid import ObjectId
from flask_app import mongo

def set_tratamiento_service():
    data = request.json
    tratamiento = {
        "_id": ObjectId(),
        "id_paciente": ObjectId(data["id_paciente"]),
        "medicacion": data.get("medicacion", ""),
        "procedimientos": data.get("procedimientos", ""),
        "recomendaciones": data.get("recomendaciones", ""),
        "fecha_inicio": datetime.strptime(data["fecha_inicio"], "%Y-%m-%d"),
        "fecha_fin": datetime.strptime(data["fecha_fin"], "%Y-%m-%d"),
        "comentarios": []
    }
    mongo.db.tratamientos.insert_one(data)
    return jsonify({"message": "Tratamiento guardado"})


def get_tratamientos_service():
    tratamientos = mongo.db.tratamientos.find()
    response = []
    for tratamiento in tratamientos:
        tratamiento['_id'] = str(tratamiento['_id'])
        response.append(tratamiento)
    return jsonify(response)
