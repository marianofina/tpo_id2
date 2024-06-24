import csv
import io
import os

from flask import send_file
from flask_app import app


def generate_csv(data):
    # Para un lugar en memoria
    si = io.StringIO()

    # Creamos un escritor de CSV
    cw = csv.writer(si)

    # Grabamos los datos en el CSV
    cw.writerows(data)

    # Obtenemos el contenido del CSV
    csv_content = si.getvalue()

    # Definimos la ruta donde se guardará en el servidor
    folder_path = os.path.join(app.root_path, 'csv')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Definimos el nombre del archivo
    file_path = os.path.join(folder_path, 'data.csv')

    # Guardar el contenido del CSV en el archivo
    with open(file_path, 'w', newline='') as csvfile:
        csvfile.write(csv_content)

    # Envía el archivo como respuesta
    return send_file(file_path, as_attachment=True)
