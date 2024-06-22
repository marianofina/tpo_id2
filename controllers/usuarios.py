from flask import Blueprint
from services.usuarios import *

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/usuario', methods=['GET'])
def get_usuario():
    return get_id_by_username_and_password()


@usuarios_bp.route('/usuario', methods=['POST'])
def add_usuario():
    return create_usuario()


@usuarios_bp.route('/usuario', methods=['PUT'])
def modify_usuario():
    return user_modify()
