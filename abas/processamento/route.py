from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

processamento = Blueprint('processamento', __name__, url_prefix='/processamento')

@processamento.route('/get_all', methods=['GET'])
@jwt_required()
def get_all():
    return jsonify({'message': 'Processamento'})