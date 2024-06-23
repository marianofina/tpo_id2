from flask import Blueprint
from services.contactos_eme import *

contactos_eme_bp = Blueprint('contactos_eme', __name__)


@contactos_eme_bp.route('/contactos_eme', methods=['GET'])
def get_contacto_by():
    return get_contacto_by_id(request.json['id_cpe'])


@contactos_eme_bp.route('/contactos_eme', methods=['POST'])
def add_contacto():
    return create_contacto()


@contactos_eme_bp.route('/contactos_eme', methods=['PUT'])
def modify_contacto():
    return contacto_modify()


@contactos_eme_bp.route('/contactos_eme', methods=['DELETE'])
def delete_contacto():
    return contacto_delete()
