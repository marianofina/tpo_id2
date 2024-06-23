from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from config.mysql import mysql


# Uso interno
def paciente_by_id(id_paci: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM pacientes WHERE id_paci = %s", (id_paci,))
        paciente = cursor.fetchone()
        cursor.close()
        return paciente
    except Exception as e:
        print(e)
        return None


# Servicio protegido
def get_paciente_by_id(id_paci: str):
    try:
        current_user_id = get_jwt_identity()
        if current_user_id[0] == id_paci:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM pacientes WHERE id_paci = %s", (id_paci,))
            paciente = cursor.fetchone()
            cursor.close()
            return jsonify(paciente)
        else:
            return jsonify({"message": "No tienes permisos para ver este usuario"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def create_paciente():
    try:
        current_user_id = get_jwt_identity()
        data = request.json
        if current_user_id[0] == data['id_paci']:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO pacientes (id_paci, credencial_paci, apellido_paci, nombre_paci, nacimiento_paci, provincia_dom_paci, localidad_dom_paci, calle_dom_paci, num_dom_paci, numero_emer_paci, correo_paci) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['id_paci'], data['credencial_paci'], data['apellido_paci'], data['nombre_paci'], data['nacimiento_paci'], data['provincia_dom_paci'], data['localidad_dom_paci'], data['calle_dom_paci'], data['num_dom_paci'], data['numero_emer_paci'], data['correo_paci'],))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Paciente creado"}), 201
        else:
            return jsonify({"message": "No tienes permisos para crear este usuario"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def paciente_modify():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        current_user_id = get_jwt_identity()
        if current_user_id[0] == data['id_paci']:
            query = "UPDATE pacientes SET "
            for key in data:
                if key != 'id_paci':
                    query += f"{key} = '{data[key]}', "
            query = query.replace("''", "' '")
            query = query[:-2]
            query += f" WHERE id_paci = '{data['id_paci']}'"
            cursor.execute(query)
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Datos modificados"}), 200
        else:
            return jsonify({"message": "No tienes permisos para modificar estos datos"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def paciente_delete():
    try:
        data = request.json
        current_user_id = get_jwt_identity()
        if current_user_id[0] == data['id_paci']:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM pacientes WHERE id_paci = %s", (data['id_paci'],))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Paciente eliminado"}), 200
        else:
            return jsonify({"message": "No tienes permisos para eliminar este usuario"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
