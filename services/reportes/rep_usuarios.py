import json

from flask_jwt_extended import get_jwt_identity

from config.mysql import mysql
from flask import jsonify

from functions.csv_generator import generate_csv

from services.medicos import get_medico_by_id
from services.comentarios_trat import get_comentarios_by_medico


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


# Servicio NO protegido
def get_citas_by_usuario(id_paci: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('GetCitasByPaciente', (id_paci,))
        data = cursor.fetchall()
        return generate_csv(data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio NO protegido
def get_historial_by_usuario(id_paci: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.callproc('GetHistorialByPaciente', (id_paci,))
        data = cursor.fetchall()
        return generate_csv(data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio NO protegido
def get_comentarios_por_medico(id_medi: str):
    try:
        comentarios = get_comentarios_by_medico(id_medi)
        rta = []
        medico = get_medico_by_id(id_medi)
        for _c in comentarios:
            rta.append({medico[2], _c['comentario'], _c['fecha']})
        return generate_csv(rta), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
