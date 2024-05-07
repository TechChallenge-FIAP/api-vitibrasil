from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from rest_api.swagger import api
from rest_api.abas.importacao.models import Importacao as ImportacaoModel

class Importacao(Resource):
    @api.doc(params={
        "pais": "País de origem da importação",
        "grupo": "Grupo da importação",
        "ano": "Ano da importação",
        "page": "Página",
        "per_page": "Resultados por página",
    })
    @api.doc(security='Bearer')
    @jwt_required()
    def get(self):
        pais = request.args.get('pais')
        grupo = request.args.get('grupo')
        ano = request.args.get('ano')
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)

        importacoes = ImportacaoModel.execute_query(
            page=page, per_page=per_page, pais=pais, grupo=grupo, ano=ano
        )
        
        return {
            "data": [
                {
                    "id": importacao.id,
                    "pais": importacao.pais,
                    "grupo": importacao.grupo,
                    "ano": importacao.ano,
                    "vl_dolar": importacao.vl_dolar,
                    "qtd_kg": importacao.qtd_kg,
                }
                for importacao in importacoes
            ],
            "pagination": {
                "count": importacoes.total,
                "page": page,
                "per_page": per_page,
                "pages": importacoes.pages,
            },
        }