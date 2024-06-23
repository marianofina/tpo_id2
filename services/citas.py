from flask import request, jsonify
from config.mysql import mysql
from functions.id_generator import id_generator


def citas_get():
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM citas')
        data = cursor.fetchall()
        cursor.close()
        return jsonify(data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def get_cita(id_cita: str):
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM citas WHERE id_cita = %s', (id_cita,))
        data = cursor.fetchall()
        cursor.close()
        return jsonify(data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def create_cita():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        new_id = id_generator("cit")
        cantidad = cursor.execute('SELECT * FROM citas')
        if cantidad != 0:
            while get_cita(new_id) is not None:
                new_id = id_generator("cit")
        cursor.execute('INSERT INTO citas (id_cita, id_disp, id_paci, dia_cita, horario_cita, asistio_cita) VALUES (%s, %s, %s, %s, %s, %s)',
                       (new_id, data['id_disp'], data['id_paci'], data['dia_cita'], data['horario_cita'], False), )
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Cita creada"}), 201
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def cita_modify():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        if 'id_cita' in data:
            query = "UPDATE citas SET "
            for key in data:
                if key != 'id_cita':
                    query += f"{key} = '{data[key]}', "
            query = query.replace("''", "' '")
            query = query[:-2]
            query += f" WHERE id_cita = '{data['id_cita']}'"
            cursor.execute(query)
            mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos modificados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def cita_delete():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM citas WHERE id_cita = %s', (data['id_cita'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Cita eliminada"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
