from flask import Blueprint
from services.medicos import *

medicos_bp = Blueprint('medicos', __name__)


@medicos_bp.route('/medicos', methods=['GET'])
def medicos_get():
    return get_medicos()


@medicos_bp.route('/medicos', methods=['POST'])
def medico_add():
    return add_medico()
