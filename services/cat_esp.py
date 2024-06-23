from flask import jsonify, request
from config.mysql import mysql
from functions.id_generator import id_generator


def get_categorias():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM especialidades")
        cat_esp = cursor.fetchall()
        cursor.close()
        return jsonify(cat_esp)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al obtener los datos"}), 400


def get_categoria_by_id(id_espe: str):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM especialidades WHERE id_espe = %s", (id_espe,))
        cat_esp = cursor.fetchone()
        cursor.close()
        return jsonify(cat_esp)
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al obtener los datos"}), 400


def add_categoria(data):
    try:
        cursor = mysql.connection.cursor()
        new_id = id_generator("cat")
        while get_categoria_by_id(new_id) is None:
            new_id = id_generator("cat")
        cursor.execute("INSERT INTO especialidades (id_espe, descripcion) VALUES (%s, %s)", (new_id, data['descripcion'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos cargados"}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al cargar los datos"}), 400


def modify_categoria(data):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE especialidades SET descripcion = %s WHERE id_espe = %s", (data['descripcion'], data['id_espe'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos modificados"}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al modificar los datos"}), 400


def categoria_delete():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM especialidades WHERE id_espe = %s", (data['id_espe'],))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Datos eliminados"}), 400
    except Exception as e:
        print(e)
        return jsonify({"message": "Error al eliminar los datos"}), 400
