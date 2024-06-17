from flask import jsonify, request
from config.mysql import mysql
from functions.id_generator import id_generator


def get_categorias():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM categorias_especialidades")
    cat_esp = cursor.fetchall()
    cursor.close()
    return jsonify(cat_esp)


def get_categoria_by_id(id: str):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM categorias_especialidades WHERE id_esca = %s", (id,))
    cat_esp = cursor.fetchone()
    cursor.close()
    return jsonify(cat_esp)


def add_categoria(data):
    cursor = mysql.connection.cursor()
    new_id = id_generator("cat")
    while get_categoria_by_id(new_id) is None:
        new_id = id_generator("cat")
    cursor.execute("INSERT INTO categorias_especialidades (id_esca, categoria) VALUES (%s, %s)", (new_id, data['categoria'],))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Datos cargados"}), 400
