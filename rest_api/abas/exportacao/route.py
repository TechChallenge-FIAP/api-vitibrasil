from flask import request
from flask_jwt_extended import jwt_required
from rest_api.swagger import api
from flask_restx import Resource
from rest_api.abas.exportacao.models import ExportacaoEmbrapa

class Exportacao(Resource):
    @api.doc(
        params={
            "grupo": "Nome do grupo exportação",
            "pais": "País de origem da exportação",
            "ano": "Ano da exportação",
            "page": "Página",
            "per_page": "Resultados por página"
        })
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        grupo = request.args.get("grupo", type=str)
        pais = request.args.get("pais", type=str)
        ano = request.args.get("ano", type=int)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)
        
        exportacoes = ExportacaoEmbrapa.execute_query(
            grupo=grupo,pais=pais,ano=ano,page=page, per_page=per_page
            )


        return {
            "data": [
                {
                    "id": exportacao.id,
                    "grupo": exportacao.grupo,
                    "pais": exportacao.pais,
                    "ano": exportacao.ano,
                    "vl_dolar": exportacao.vl_dolar,
                    "qtd_kg": exportacao.qtd_kg
                }
                for exportacao in exportacoes
            ],
            "pagination": {
             "count": exportacoes.total,
             "page": page,
             "per_page": per_page,
             "pages": exportacoes.pages,
            },
        }

