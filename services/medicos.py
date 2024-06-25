from flask import jsonify, request
from config.mysql import mysql
from functions.id_generator import id_generator


def get_medicos():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM medicos")
        medicos = cursor.fetchall()
        cursor.close()
        return jsonify(medicos)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def get_medico_by_id(id_medi: str):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM medicos WHERE id_medi = %s", (id_medi,))
    medico = cursor.fetchone()
    cursor.close()
    return medico


def add_medico():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        new_id = id_generator("med")
        while get_medico_by_id(new_id) is not None:
            new_id = id_generator("med")
        cursor.execute("INSERT INTO medicos (id_medi, legajo_medi, nombre_med, apellido_med, nacimiento_med, ingreso_med) VALUES (%s, %s, %s, %s, %s, %s)", (new_id, data['legajo'], data['nombre'], data['apellido'], data['nacimiento'], data['ingreso'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos cargados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def medico_modify():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        if 'id_medi' in data:
            query = "UPDATE medicos SET "
            for key in data:
                if key != 'id_medi':
                    query += f"{key} = '{data[key]}', "
            query = query.replace("''", "' '")
            query = query[:-2]
            query += f" WHERE id_medi = '{data['id_medi']}'"
            cursor.execute(query)
            mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos modificados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def medico_delete():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM medicos WHERE id_medi = %s", (data['id_medi'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos eliminados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500

