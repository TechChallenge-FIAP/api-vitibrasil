from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

importacao = Blueprint('importacao', __name__, url_prefix='/importacao')

@importacao.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    return jsonify({'message': 'Importação'})