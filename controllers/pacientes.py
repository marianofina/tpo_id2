from flask import Blueprint
from flask_jwt_extended import jwt_required

from services.pacientes import *

pacientes_bp = Blueprint('pacientes_bp', __name__)


@pacientes_bp.route('/pacientes', methods=['GET'])
@jwt_required()
def get_paciente():
    return get_paciente_by_id(request.json['id_paci'])


@pacientes_bp.route('/pacientes', methods=['POST'])
@jwt_required()
def add_paciente():
    return create_paciente()


@pacientes_bp.route('/pacientes', methods=['PUT'])
@jwt_required()
def modify_paciente():
    return paciente_modify()


@pacientes_bp.route('/pacientes', methods=['DELETE'])
@jwt_required()
def delete_paciente():
    return paciente_delete()
