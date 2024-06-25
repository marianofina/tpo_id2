from flask_app import app
from flask_pymongo import PyMongo
from pymongo import MongoClient

# Configura la URI de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/db_mongo"

# Inicializa PyMongo
mongo = PyMongo(app)

# Conectar a MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()