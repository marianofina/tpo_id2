from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'


# Configuración JWT
app.config['JWT_SECRET_KEY'] = 'grupo-8'
jwt = JWTManager(app)
