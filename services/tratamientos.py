from bson.objectid import ObjectId
from config.mongodb import mongo


def insert_tratamiento(tratamiento):
    return mongo.db.tratamientos_medicos.insert_one(tratamiento)


def get_tratamiento(id):
    return mongo.db.tratamientos_medicos.find_one({"_id": ObjectId(id)})


def update_tratamiento(id, actualizacion):
    return mongo.db.tratamientos_medicos.update_one({"_id": ObjectId(id)}, {"$set": actualizacion})


def delete_tratamiento(id):
    return mongo.db.tratamientos_medicos.delete_one({"_id": ObjectId(id)})
