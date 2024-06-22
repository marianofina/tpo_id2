from flask import request, jsonify
from config.mysql import mysql


def get_paciente_by_id(id_paci: str):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE id_paci = %s", (id_paci,))
    paciente = cursor.fetchone()
    cursor.close()
    return jsonify(paciente)


def create_paciente():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO pacientes (id_paci, credencial_paci, apellido_paci, nombre_paci, nacimiento_paci, provincia_dom_paci, localidad_dom_paci, calle_dom_paci, num_dom_paci, numero_emer_paci, correo_paci) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['id_paci'], data['credencial_paci'], data['apellido_paci'], data['nombre_paci'], data['nacimiento_paci'], data['provincia_dom_paci'], data['localidad_dom_paci'], data['calle_dom_paci'], data['num_dom_paci'], data['numero_emer_paci'], data['correo_paci'],))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Paciente creado"}), 201


def paciente_modify():
    cursor = mysql.connection.cursor()
    data = request.json
    if 'id_paci' in data:
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
