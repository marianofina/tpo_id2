from flask import jsonify, request
from config.mysql import mysql


def get_medicos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM medicos")
    medicos = cursor.fetchall()
    cursor.close()
    return jsonify(medicos)


def add_medico():
    cursor = mysql.connection.cursor()
    data = request.json
    cant = len(data)

