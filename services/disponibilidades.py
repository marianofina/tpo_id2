from flask import jsonify, request
from config.mysql import mysql
from functions.id_generator import id_generator


def disponibilidades_get():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM disponibilidades")
        disponibilidades = cursor.fetchall()
        cursor.close()
        return jsonify(disponibilidades)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al obtener los datos"}), 500


def get_disponibilidad_by_id(id_disp: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM disponibilidades WHERE id_disp = %s", (id_disp,))
        disponibilidad = cursor.fetchone()
        cursor.close()
        return jsonify(disponibilidad)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al obtener los datos"}), 500


def disponibilidad_add():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        new_id = id_generator('dis')
        while get_disponibilidad_by_id(new_id) is None:
            new_id = id_generator("med")
        cursor.execute("INSERT INTO disponibilidades (id_disp, horainicio_disp, horafin_disp, id_meep, dia_disp) VALUES (%s, %s, %s, %s, %s)", (new_id, data['horainicio_disp'], data['horafin_disp'], data['id_meep'], data['dia_disp']))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos cargados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al cargar los datos"}), 500


def disponibilidad_modify():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        if 'id_disp' in data:
            query = "UPDATE disponibilidades SET "
            for key in data:
                if key != 'id_disp':
                    query += f"{key} = '{data[key]}', "
            query = query.replace("''", "' '")
            query = query[:-2]
            query += f" WHERE id_disp = '{data['id_disp']}'"
            cursor.execute(query)
            mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos modificados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al modificar los datos"}), 500


def disponibilidad_delete():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM disponibilidades WHERE id_disp = %s", (data['id_disp'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos eliminados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al eliminar los datos"}), 500
