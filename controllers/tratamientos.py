from flask import Blueprint
from services.tratamientos import *

tratamientos_bp = Blueprint('tratamientos', __name__)


@tratamientos_bp.route('/tratamientos', methods=['POST'])
def set_tratamiento():
    return set_tratamiento_service()


@tratamientos_bp.route('/tratamientos', methods=['GET'])
def get_tratamientos():
    return get_tratamientos_service()
