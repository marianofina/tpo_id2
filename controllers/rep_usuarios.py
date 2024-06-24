from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from services.reportes.rep_usuarios import *

rep_usuarios_bp = Blueprint('rep_usuarios', __name__)


@rep_usuarios_bp.route('/citas_por_paciente', methods=['GET'])
@jwt_required()
def get_citas():
    return get_citas_by_usuario(request.json['id_paci'])


@rep_usuarios_bp.route('/historial_por_paciente', methods=['GET'])
@jwt_required()
def get_historial():
    return get_historial_by_usuario(request.json['id_paci'])
