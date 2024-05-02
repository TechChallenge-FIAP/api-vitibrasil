from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from rest_api.swagger import api
from services.database import create_connection
from rest_api.abas.exportacao.models import exportacao

class Exportacao(Resource):
     @api.doc(
        params={
            "grupo": "Nome do grupo",
            "pais": "Pais",
            "ano": "Ano de produção do produto",
            })
     @api.doc(security="Bearer")
     @jwt_required()
     def get(self):
        grupo = request.args.get("grupo")
        pais = request.args.get("pais")
        ano = request.args.get("ano")
        
        exportacao = exportacao.execute_query(
            grupo=grupo, pais=pais, ano=ano
            )
        return {
            "data": [
                {
                    "id": exportacao.id,
                    "grupo": exportacao.grupo,
                    "pais": exportacao.pais,
                    "ano": exportacao.ano,
                }
                for exportacao in exportacao
            ]
            }