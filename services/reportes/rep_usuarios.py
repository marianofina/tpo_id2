from flask_jwt_extended import get_jwt_identity

from config.mysql import mysql
from flask import jsonify


def get_citas_by_usuario(id_paci: str):
    try:
        current_user_id = get_jwt_identity()
        if current_user_id[0] == id_paci:
            cursor = mysql.connection.cursor()
            cursor.callproc('GetCitasByPaciente', (id_paci,))
            citas = cursor.fetchall()
            cursor.close()
            return jsonify(citas), 200
        else:
            return jsonify({"message": "No tienes permisos para ver estas citas"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def get_historial_by_usuario(id_paci: str):
    try:
        current_user_id = get_jwt_identity()
        if current_user_id[0] == id_paci:
            cursor = mysql.connection.cursor()
            cursor.callproc('GetHistorialByPaciente', (id_paci,))
            historial = cursor.fetchall()
            cursor.close()
            return jsonify(historial), 200
        else:
            return jsonify({"message": "No tienes permisos para ver este historial"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
