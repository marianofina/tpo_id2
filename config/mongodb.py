from flask_app import app
from flask_pymongo import PyMongo


# Configura la URI de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/db_mongo"

# Inicializa PyMongo
mongo = PyMongo(app)
