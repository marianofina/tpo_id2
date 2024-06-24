# Flask API Project

Este proyecto es una API construida utilizando el framework Flask en Python. La API cuenta con una capa de servicios y controladores, y se conecta tanto a MySQL como a MongoDB para la gestión de datos. Además, utiliza JWT para autenticación y autorización.


## Descripción de Carpetas y Archivos

- `tpo_id2/`: Carpeta principal de la aplicación.
  - `controllers/`: Contiene los controladores que manejan las rutas y las solicitudes HTTP.
  - `services/`: Contiene la lógica de negocio y los servicios utilizados por los controladores.
  - `functions/`: Contiene funciones auxiliares y validaciones como la gestión de horarios, generación de archivos CSV para reportes y generación de IDs para las tablas de MySQL.
  - `config/`: Contiene la configuración de la base de datos y scripts SQL para inicializar las tablas, vistas y procedimientos almacenados en MySQL.
- `app.py`: Archivo principal de la aplicación Flask.  
- `main.py`: Inicializador de la API, se encuentra el host y puerto.
- `README.md`: Este archivo, que proporciona una descripción del proyecto y sus instrucciones de uso.

## Dependencias

Las dependencias del proyecto incluyen:

- Flask
- PyJWT
- Flask-JWT-Extended
- Flask-PyMongo
- flask-mysqldb
- random
- csv
- io
- os
- datetime

El archivo config/Script.sql contiene los scripts necesarios para crear las tablas, vistas y procedimientos almacenados en MySQL. 

## Iniciar la API

Posicionándose sobre la ruta principal y ejecutando el comando:
py main.py
debería correr en localhost:5000
