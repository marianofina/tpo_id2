from flask import jsonify, request
from config.mysql import mysql
from functions.id_generator import id_generator


def get_meep():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM medicos_especialidad")
        meep = cursor.fetchall()
        cursor.close()
        return jsonify(meep)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 400


def get_meep_by_id(id_meep: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM medicos_especialidad WHERE id_meep = %s", (id_meep,))
        meep = cursor.fetchone()
        cursor.close()
        return jsonify(meep)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 400


def add_meep():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        new_id = id_generator("mep")
        while get_meep_by_id(new_id) is None:
            new_id = id_generator("mep")
        cursor.execute("INSERT INTO medicos_especialidad (id_meep, id_medico, id_especialidad) VALUES (%s, %s, %s)", (new_id, data['id_medico'], data['id_especialidad'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos cargados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 400


# Modifica la especialidad del médico
def meep_modify():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        if 'id_meep' and 'id_especialidad' in data:
            cursor.execute("UPDATE medicos_especialidad SET id_especialidad = %s WHERE id_meep = %s", (data['id_especialidad'], data['id_meep'],))
            mysql.connection.commit()
            cursor.close()
        return jsonify({"message": "Datos modificados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 400


def meep_delete():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM medicos_especialidad WHERE id_meep = %s", (data['id_meep'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos eliminados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 400
