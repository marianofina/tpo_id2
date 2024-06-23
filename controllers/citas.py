from flask import Blueprint
from flask_jwt_extended import jwt_required

from services.citas import *

citas_bp = Blueprint('citas', __name__)


@citas_bp.route('/citas', methods=['GET'])
@jwt_required()
def get_citas_by_id():
    return get_cita(request.json['id_cita'])


@citas_bp.route('/citas', methods=['POST'])
@jwt_required()
def add_cita():
    return create_cita()


@citas_bp.route('/citas', methods=['PUT'])
@jwt_required()
def modify_cita():
    return cita_modify()


@citas_bp.route('/citas', methods=['DELETE'])
@jwt_required()
def delete_cita():
    return cita_delete()
