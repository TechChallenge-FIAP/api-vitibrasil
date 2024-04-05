from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

comercializacao = Blueprint('comercializacao', __name__, url_prefix='/comercializacao')

@comercializacao.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    return jsonify({'message': 'Comercialização'})