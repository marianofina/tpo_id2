from flask import Blueprint
from services.citas import *

citas_bp = Blueprint('citas', __name__)


@citas_bp.route('/citas', methods=['GET'])
def get_citas_by_id():
    return get_cita(request.json['id_cita'])


@citas_bp.route('/citas', methods=['POST'])
def add_cita():
    return create_cita()


@citas_bp.route('/citas', methods=['PUT'])
def modify_cita():
    return cita_modify()
