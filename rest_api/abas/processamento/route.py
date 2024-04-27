from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from rest_api.swagger import api


class Processamento(Resource):
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        return jsonify({"message": "Processamento"})
