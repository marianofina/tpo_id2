from bson.objectid import ObjectId
from config.mongodb import mongo


def insert_comentarios_trat(comentarios_trat):
    comentarios_trat["id_trat"] = ObjectId(comentarios_trat["id_trat"])
    return mongo.db.comentarios_trat.insert_one(comentarios_trat)


def get_comentarios_trat(id):
    rta = mongo.db.comentarios_trat.find_one({"_id": ObjectId(id)})
    return rta


def update_comentarios_trat(id, actualizacion):
    return mongo.db.comentarios_trat.update_one({"_id": ObjectId(id)}, {"$set": actualizacion})


def delete_comentarios_trat(id):
    return mongo.db.comentarios_trat.delete_one({"_id": ObjectId(id)})


def get_comentarios_by_medico(id_medico):
    rta = mongo.db.comentarios_trat.find({"id_medi": id_medico})
    return rta
