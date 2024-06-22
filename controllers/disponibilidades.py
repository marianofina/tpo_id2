from flask import Blueprint
from services.disponibilidades import *

disponibilidades_bp = Blueprint('disponibilidades', __name__)


@disponibilidades_bp.route('/disponibilidades', methods=['GET'])
def get_all_disponibilidades():
    return disponibilidades_get()


@disponibilidades_bp.route('/disponibilidad', methods=['GET'])
def get_disponibilidad():
    return get_disponibilidad_by_id(request.json['id_disp'])


@disponibilidades_bp.route('/disponibilidades', methods=['POST'])
def add_disponibilidad():
    return disponibilidad_add()


@disponibilidades_bp.route('/disponibilidades', methods=['PUT'])
def modify_disponibilidad():
    return disponibilidad_modify()
