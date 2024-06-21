from flask import Blueprint
from services.cat_esp import *

categorias_bp = Blueprint('categorias', __name__)


@categorias_bp.route('/categoria', methods=['GET'])
def categoria_by_id():
    return get_categoria_by_id(request.json["id_espe"])


@categorias_bp.route('/categoria', methods=['POST'])
def categorias_add():
    return add_categoria(request.json)


@categorias_bp.route('/categorias', methods=['GET'])
def categorias_get():
    return get_categorias()


@categorias_bp.route('/categoria', methods=['PUT'])
def categorias_modify():
    return modify_categoria(request.json)
