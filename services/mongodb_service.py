# services/mongodb_service.py

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()

def init_mongodb(app):
    mongo.init_app(app)

def insert_historial(historial):
    return mongo.db.historiales.insert_one(historial)

def get_historial(id):
    return mongo.db.historiales.find_one({"_id": ObjectId(id)})

def update_historial(id, actualizacion):
    return mongo.db.historiales.update_one({"_id": ObjectId(id)}, {"$set": actualizacion})

def delete_historial(id):
    return mongo.db.historiales.delete_one({"_id": ObjectId(id)})