from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from config.mysql import mysql
from functions.id_generator import id_generator
from functions.citas_x_turno import citas_x_turno

def citas_get():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM citas')
        data = cursor.fetchall()
        cursor.close()
        return jsonify(data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Uso interno
def cita(id_cita: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM citas WHERE id_cita = %s', (id_cita,))
        cita_data = cursor.fetchone()
        cursor.close()
        return cita_data
    except Exception as e:
        print(e)
        return None


# Servicio protegido
def get_cita(id_cita: str):
    try:
        current_user_id = get_jwt_identity()
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM citas WHERE id_cita = %s', (id_cita,))
        data = cursor.fetchone()
        cursor.close()
        if current_user_id[0] == data[2]:
            return jsonify(data), 200
        else:
            return jsonify({"message": "No autorizado"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def create_cita():
    try:
        current_user_id = get_jwt_identity()
        data = request.json
        if current_user_id[0] == data['id_paci']:
            cursor = mysql.connection.cursor()
            new_id = id_generator("cit")
            cantidad = cursor.execute('SELECT * FROM citas')
            if cantidad != 0:
                while cita(new_id) is not None:
                    new_id = id_generator("cit")
            if citas_x_turno(data['horario_cita'], data['id_disp']):
                cursor.execute('INSERT INTO citas (id_cita, id_disp, id_paci, horario_cita, asistio_cita) VALUES (%s, %s, %s, %s, %s)',
                               (new_id, data['id_disp'], data['id_paci'], data['horario_cita'], False), )
                mysql.connection.commit()
                cursor.close()
                return jsonify({"message": "Cita creada"}), 201
            else:
                return jsonify({"message": "Horario no disponible"}), 400
        else:
            return jsonify({"message": "No autorizado"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def cita_modify():
    try:
        cursor = mysql.connection.cursor()
        current_user_id = get_jwt_identity()
        data = request.json
        if current_user_id[0] == data['id_paci']:
            if citas_x_turno(data['horario_cita'], data['id_disp']):
                query = "UPDATE citas SET "
                for key in data:
                    if key != 'id_cita' and key != 'id_paci':
                        query += f"{key} = '{data[key]}', "
                query = query.replace("''", "' '")
                query = query[:-2]
                query += f" WHERE id_cita = '{data['id_cita']}'"
                cursor.execute(query)
                mysql.connection.commit()
                cursor.close()
                return jsonify({"message": "Datos modificados"}), 200
            else:
                return jsonify({"message": "Horario no disponible"}), 400
        else:
            return jsonify({"message": "No autorizado"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def cita_delete():
    try:
        cursor = mysql.connection.cursor()
        current_user_id = get_jwt_identity()
        data = request.json
        if current_user_id[0] == data['id_paci']:
            cursor.execute('DELETE FROM citas WHERE id_cita = %s', (data['id_cita'],))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Cita eliminada"}), 200
        else:
            return jsonify({"message": "No autorizado"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
