from flask_jwt_extended import get_jwt_identity

from config.mysql import mysql
from flask import jsonify

from functions.csv_generator import generate_csv


# Servicio protegido
def get_citas_by_usuario_p(id_paci: str):
    try:
        current_user_id = get_jwt_identity()
        if current_user_id[0] == id_paci:
            cursor = mysql.connection.cursor()
            cursor.callproc('GetCitasByPaciente', (id_paci,))
            data = cursor.fetchall()
            return generate_csv(data), 200
        else:
            return jsonify({"message": "No tienes permisos para ver estas citas"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def get_historial_by_usuario_p(id_paci: str):
    try:
        current_user_id = get_jwt_identity()
        if current_user_id[0] == id_paci:
            cursor = mysql.connection.cursor()
            cursor.callproc('GetHistorialByPaciente', (id_paci,))
            data = cursor.fetchall()
            return generate_csv(data), 200
        else:
            return jsonify({"message": "No tienes permisos para ver este historial"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def get_citas_by_usuario(id_paci: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('GetCitasByPaciente', (id_paci,))
        data = cursor.fetchall()
        return generate_csv(data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def get_historial_by_usuario(id_paci: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('GetHistorialByPaciente', (id_paci,))
        data = cursor.fetchall()
        return generate_csv(data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
