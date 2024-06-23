from flask import request, jsonify
from config.mysql import mysql
from functions.id_generator import id_generator


def get_contacto_by_id(id_cpe: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM contactos_paci_emergencia WHERE id_cpe = %s", (id_cpe,))
        contacto = cursor.fetchone()
        cursor.close()
        return jsonify(contacto)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def create_contacto():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        new_id = id_generator("con")
        cantidad = cursor.execute("SELECT * FROM contactos_paci_emergencia")
        if cantidad != 0:
            while get_contacto_by_id(new_id) is not None:
                new_id = id_generator("con")
        cursor.execute("INSERT INTO contactos_paci_emergencia (id_cpe, nombrecompleto_cpe, relacion_cpe, numero) VALUES (%s, %s, %s, %s)", (new_id, data['nombrecompleto_cpe'], data['relacion_cpe'], data['numero'],))
        cursor.execute("UPDATE pacientes SET id_contactoemergencia = %s WHERE id_paci = %s", (new_id, data['id_paci'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Contacto creado"}), 201
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def contacto_modify():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        if 'id_cpe' in data:
            query = "UPDATE contactos_paci_emergencia SET "
            for key in data:
                if key != 'id_cpe':
                    query += f"{key} = '{data[key]}', "
            query = query.replace("''", "' '")
            query = query[:-2]
            query += f" WHERE id_cpe = '{data['id_cpe']}'"
            cursor.execute(query)
            mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos modificados"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500


def contacto_delete():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM contactos_paci_emergencia WHERE id_cpe = %s", (data['id_cpe'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Contacto eliminado"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error"}), 500
