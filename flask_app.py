# -*- coding: utf-8 -*-
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'

# Configuración de la base de datos MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/db_mongo"
mongo = PyMongo(app)

# Configuración JWT
app.config['JWT_SECRET_KEY'] = 'grupo-8'
jwt = JWTManager(app)
