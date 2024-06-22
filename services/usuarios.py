from flask import request, jsonify
from config.mysql import mysql
from functions.id_generator import id_generator


def get_usuario_by_username(usuario: str):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE user_usua = %s", (usuario,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario


def get_usuario_by_id(id_usua: str):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE pacientes_id_paci = %s", (id_usua,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario


def create_usuario():
    data = request.json
    cursor = mysql.connection.cursor()
    new_id = id_generator("usu")
    while get_usuario_by_id(new_id) is not None:
        new_id = id_generator("usu")
    cursor.execute("INSERT INTO usuarios (pacientes_id_paci, user_usua, password_usua) VALUES (%s, %s, %s)", (new_id, data['user_usua'], data['password_usua'],))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Usuario creado"}), 201


def get_id_by_username_and_password():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT pacientes_id_paci FROM usuarios WHERE user_usua = %s AND password_usua = %s", (data['user_usua'], data['password_usua'],))
    id_user = cursor.fetchone()
    cursor.close()
    return jsonify(id_user)


def user_modify():
    cursor = mysql.connection.cursor()
    data = request.json
    if 'pacientes_id_paci' in data:
        query = "UPDATE usuarios SET "
        for key in data:
            if key != 'pacientes_id_paci':
                query += f"{key} = '{data[key]}', "
        query = query.replace("''", "' '")
        query = query[:-2]
        query += f" WHERE pacientes_id_paci = '{data['pacientes_id_paci']}'"
        cursor.execute(query)
        mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Datos modificados"}), 200
