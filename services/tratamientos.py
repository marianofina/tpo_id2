from flask import request, jsonify
from config.mongodb import mongo


def set_tratamiento_service():
    data = request.json
    mongo.db.tratamientos.insert_one(data)
    return jsonify({"message": "Tratamiento guardado"})


def get_tratamientos_service():
    tratamientos = mongo.db.tratamientos.find()
    response = []
    for tratamiento in tratamientos:
        tratamiento['_id'] = str(tratamiento['_id'])
        response.append(tratamiento)
    return jsonify(response)
