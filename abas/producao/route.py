from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

producao = Blueprint('producao', __name__, url_prefix='/producao')

@producao.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    return jsonify({'message': 'Produção'})