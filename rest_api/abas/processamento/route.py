from flask import request
from flask_jwt_extended import jwt_required
from rest_api.swagger import api
from flask_restx import Resource
from rest_api.abas.processamento.models import Categorias
from rest_api.abas.processamento.models import Tipouva

@api.doc(description="Este endpoint realiza a busca da Quantidade de uvas processadas no Rio Grande do Sul. Se nenhum parâmetro for passado irá trazer a base completa")
class ProcessamentoCategoria(Resource):
    @api.doc(params={
            "grupo": "Nome do grupo",
            "sub_categoria": "sub_categoria do produto",
            "ano": "Ano de produção do produto",
            "page": "Página",
            "per_page": "Resultados por Página",
            })
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        grupo = request.args.get("grupo", type=str)
        sub_categoria = request.args.get("sub_categoria", type=str)
        ano = request.args.get("ano", type=int)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)
        processamento_categoria = Categorias.execute_query(
            page=page, per_page=per_page, grupo=grupo,sub_categoria=sub_categoria, ano=ano
        )
        return {
            "data": [
                {
                    "id": sub_categoria.id,
                    "grupo": sub_categoria.grupo,
                    "sub_categoria": sub_categoria.sub_categoria,
                    "ano": sub_categoria.ano,
                    "quantidade_kg": sub_categoria.quantidade_kg
                }
                for sub_categoria in processamento_categoria
            ],
            "pagination": {
                "count": processamento_categoria.total,
                "page": page,
                "per_page": per_page,
                "pages": processamento_categoria.pages
            },
        }

@api.doc(description="Este endpoint realiza a busca Tipo de uvas processadas no Rio Grande do Sul. Se nenhum parâmetro for passado irá trazer a base completa.")
class ProcessamentoTipo(Resource):
    @api.doc(params={
            "grupo": "Nome do grupo",
            "sub_categoria": "sub_categoria do produto",
            "tipo_uva": "Tipo da uva",
            "ano": "Ano de produção do produto",
            "page": "Página",
            "per_page": "Resultados por Página",
            })
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        grupo = request.args.get("grupo", type=str)
        sub_categoria = request.args.get("sub_categoria", type=str)
        tipo_uva = request.args.get("tipo_uva", type=str)
        ano = request.args.get("ano", type=int)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)
        processamento_tipos = Tipouva.execute_query(
            page=page, per_page=per_page, grupo=grupo,sub_categoria=sub_categoria,tipo_uva=tipo_uva, ano=ano
        )
        return {
            "data": [
                {
                    "id": processamento_tipo.id,
                    "grupo": processamento_tipo.grupo,
                    "sub_categoria": processamento_tipo.sub_categoria,
                    "tipo_uva": processamento_tipo.sub_categoria,
                    "ano": processamento_tipo.ano,
                    "quantidade_kg": processamento_tipo.quantidade_kg
                }
                for processamento_tipo in processamento_tipos
            ],
            "pagination": {
                "count": processamento_tipos.total,
                "page": page,
                "per_page": per_page,
                "pages": processamento_tipos.pages
            },
        }
