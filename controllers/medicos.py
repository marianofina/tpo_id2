from flask import Blueprint
from services.medicos import *

medicos_bp = Blueprint('medicos', __name__)


@medicos_bp.route('/medicos', methods=['GET'])
def medicos_get():
    return get_medicos()


@medicos_bp.route('/medico', methods=['GET'])
def medico_by_id():
    return get_medico_by_id(request.json["id_medi"])


@medicos_bp.route('/medico', methods=['POST'])
def medico_add():
    return add_medico()


@medicos_bp.route('/medico', methods=['PUT'])
def modify_medico():
    return medico_modify()

