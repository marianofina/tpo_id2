from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

from config.mysql import mysql
from functions.id_generator import id_generator

from services.pacientes import paciente_by_id


# Uso interno
def contacto_by_id(id_cpe: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM contactos_paci_emergencia WHERE id_cpe = %s", (id_cpe,))
        contacto = cursor.fetchone()
        cursor.close()
        return contacto
    except Exception as e:
        print(e)
        return None


# Servicio protegido
def get_contacto_by_id(id_cpe: str):
    try:
        current_user_id = get_jwt_identity()
        paciente = paciente_by_id(current_user_id[0])
        if paciente is not None and paciente[11] == id_cpe:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM contactos_paci_emergencia WHERE id_cpe = %s", (id_cpe,))
            contacto = cursor.fetchall()
            cursor.close()
            return jsonify(contacto)
        else:
            return jsonify({"message": "No tienes permisos para ver este contacto"}), 403
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def create_contacto():
    try:
        current_user_id = get_jwt_identity()
        data = request.json
        paciente = paciente_by_id(current_user_id[0])
        if paciente is not None and paciente[0] == data['id_paci']:
            cursor = mysql.connection.cursor()
            new_id = id_generator("con")
            cantidad = cursor.execute("SELECT * FROM contactos_paci_emergencia")
            if cantidad != 0:
                while contacto_by_id(new_id) is not None:
                    print(contacto_by_id(new_id))
                    new_id = id_generator("con")
            cursor.execute("INSERT INTO contactos_paci_emergencia (id_cpe, nombrecompleto_cpe, relacion_cpe, numero) VALUES (%s, %s, %s, %s)", (new_id, data['nombrecompleto_cpe'], data['relacion_cpe'], data['numero'],))
            cursor.execute("UPDATE pacientes SET id_contactoemergencia = %s WHERE id_paci = %s", (new_id, data['id_paci'],))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Contacto creado"}), 201
        else:
            return jsonify({"message": "No tienes permisos para crear este contacto"}), 403
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


# Servicio protegido
def contacto_modify():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        current_user_id = get_jwt_identity()
        paciente = paciente_by_id(current_user_id[0])
        if paciente is not None and paciente[0] == data['id_paci'] and paciente[11] == data['id_cpe']:
            query = "UPDATE contactos_paci_emergencia SET "
            for key in data:
                if key != 'id_cpe' and key != 'id_paci':
                    query += f"{key} = '{data[key]}', "
            query = query.replace("''", "' '")
            query = query[:-2]
            query += f" WHERE id_cpe = '{data['id_cpe']}'"
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
def contacto_delete():
    try:
        data = request.json
        current_user_id = get_jwt_identity()
        paciente = paciente_by_id(current_user_id[0])
        if paciente is not None and paciente[0] == data['id_paci'] and paciente[11] == data['id_cpe']:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE pacientes SET id_contactoemergencia = NULL WHERE id_paci = %s", (data['id_paci'],))
            cursor.execute("DELETE FROM contactos_paci_emergencia WHERE id_cpe = %s", (data['id_cpe'],))
            mysql.connection.commit()
            cursor.close()
            return jsonify({"message": "Contacto eliminado"}), 200
        else:
            return jsonify({"message": "No tienes permisos para eliminar este contacto"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
