from bson.objectid import ObjectId
from config.mongodb import mongo


def insert_hospitalizaciones(hospitalizaciones):
    for i in range(len(hospitalizaciones["tratamientos"])):
        hospitalizaciones["tratamientos"][i] = ObjectId(hospitalizaciones["tratamientos"][i])
    return mongo.db.hospitalizaciones.insert_one(hospitalizaciones)


def get_hospitalizaciones(id):
    rta = mongo.db.hospitalizaciones.find_one({"_id": ObjectId(id)})
    return rta


def update_hospitalizaciones(id, actualizacion):
    if "tratamientos" in actualizacion:
        for i in range(len(actualizacion["tratamientos"])):
            actualizacion["tratamientos"][i] = ObjectId(actualizacion["tratamientos"][i])
    return mongo.db.hospitalizaciones.update_one({"_id": ObjectId(id)}, {"$set": actualizacion})


def delete_hospitalizaciones(id):
    return mongo.db.hospitalizaciones.delete_one({"_id": ObjectId(id)})
