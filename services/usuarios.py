from flask import request, jsonify
from config.mysql import mysql
from functions.id_generator import id_generator


# Uso interno
def get_usuario_by_username(usuario: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE user_usua = %s", (usuario,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
    except Exception as e:
        print(e)
        return None


# Uso interno
def get_usuario_by_id(id_usua: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE pacientes_id_paci = %s", (id_usua,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
    except Exception as e:
        print(e)
        return None


def create_usuario():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        new_id = id_generator("usu")
        while get_usuario_by_id(new_id) is not None:
            new_id = id_generator("usu")
        cursor.execute("INSERT INTO usuarios (pacientes_id_paci, user_usua, password_usua) VALUES (%s, %s, %s)", (new_id, data['user_usua'], data['password_usua'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Usuario creado"}), 201
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al crear usuario"}), 500


def get_id_by_username_and_password():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT pacientes_id_paci FROM usuarios WHERE user_usua = %s AND password_usua = %s", (data['user_usua'], data['password_usua'],))
        id_user = cursor.fetchone()
        cursor.close()
        return jsonify(id_user), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al obtener usuario"}), 400


def user_modify():
    try:
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
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al modificar datos"}), 400


def user_delete():
    try:
        cursor = mysql.connection.cursor()
        data = request.json
        cursor.execute("DELETE FROM usuarios WHERE pacientes_id_paci = %s", (data['pacientes_id_paci'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Usuario eliminado"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al eliminar usuario"}), 400
