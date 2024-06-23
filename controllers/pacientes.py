from flask import Blueprint
from services.pacientes import *

pacientes_bp = Blueprint('pacientes_bp', __name__)


@pacientes_bp.route('/pacientes', methods=['GET'])
def get_paciente():
    return get_paciente_by_id(request.json['id_paci'])


@pacientes_bp.route('/pacientes', methods=['POST'])
def add_paciente():
    return create_paciente()


@pacientes_bp.route('/pacientes', methods=['PUT'])
def modify_paciente():
    return paciente_modify()


@pacientes_bp.route('/pacientes', methods=['DELETE'])
def delete_paciente():
    return paciente_delete()
