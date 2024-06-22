from flask import Blueprint
from services.medicos_esp import *

medicos_esp_bp = Blueprint('medicos_esp', __name__)


@medicos_esp_bp.route('/medicos_esp', methods=['GET'])
def medicos_esp_get():
    return get_meep()


@medicos_esp_bp.route('/medico_esp', methods=['GET'])
def medicos_esp_get_by_id():
    return get_meep_by_id(request.json['id_meep'])


@medicos_esp_bp.route('/medicos_esp', methods=['POST'])
def medicos_esp_add():
    return add_meep()


@medicos_esp_bp.route('/medicos_esp', methods=['PUT'])
def medicos_esp_modify():
    return meep_modify()

