from flask import Blueprint
from flask_jwt_extended import jwt_required

from services.contactos_eme import *

contactos_eme_bp = Blueprint('contactos_eme', __name__)


@contactos_eme_bp.route('/contactos_eme', methods=['GET'])
@jwt_required()
def get_contacto_by():
    return get_contacto_by_id(request.json['id_cpe'])


@contactos_eme_bp.route('/contactos_eme', methods=['POST'])
@jwt_required()
def add_contacto():
    return create_contacto()


@contactos_eme_bp.route('/contactos_eme', methods=['PUT'])
@jwt_required()
def modify_contacto():
    return contacto_modify()


@contactos_eme_bp.route('/contactos_eme', methods=['DELETE'])
@jwt_required()
def delete_contacto():
    return contacto_delete()
