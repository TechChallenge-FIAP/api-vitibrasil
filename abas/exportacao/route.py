from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

exportacao = Blueprint('exportacao', __name__, url_prefix='/exportacao')

@exportacao.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    return jsonify({'message': 'Exportação'})