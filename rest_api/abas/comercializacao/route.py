from flask import request
from flask_jwt_extended import jwt_required
from rest_api.swagger import api
from flask_restx import Resource
from rest_api.abas.comercializacao.models import Produto, Categoria


class ComercializacaoProduto(Resource):
    @api.doc(
        params={
            "produto": "Nome do produto",
            "categoria": "Categoria do produto",
            "ano": "Ano de produção do produto",
            "page": "Página",
            "per_page": "Resultados por página",
        }
    )
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        produto = request.args.get("produto", type=str)
        categoria = request.args.get("categoria", type=str)
        ano = request.args.get("ano", type=int)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)

        comercializacao_produtos = Produto.execute_query(
            page=page, per_page=per_page, produto=produto, categoria=categoria, ano=ano
        )

        return {
            "data": [
                {
                    "id": produto.id,
                    "produto": produto.produto,
                    "categoria": produto.categoria,
                    "ano": produto.ano,
                    "quantidade_l": produto.quantidade_l,
                }
                for produto in comercializacao_produtos
            ],
            "pagination": {
                "count": comercializacao_produtos.total,
                "page": page,
                "per_page": per_page,
                "pages": comercializacao_produtos.pages,
            },
        }


class ComercializacaoCategoria(Resource):
    @api.doc(
        params={
            "categoria": "Categoria do produto",
            "ano": "Ano de produção do produto",
            "page": "Página",
            "per_page": "Resultados por página",
        }
    )
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        categoria = request.args.get("categoria", type=str)
        ano = request.args.get("ano", type=int)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)

        comercializacao_categorias = Categoria.execute_query(
            page=page, per_page=per_page, categoria=categoria, ano=ano
        )

        return {
            "data": [
                {
                    "id": categoria.id,
                    "produto": categoria.produto,
                    "categoria": categoria.categoria,
                    "ano": categoria.ano,
                    "quantidade_l": categoria.quantidade_l,
                }
                for categoria in comercializacao_categorias
            ]
        }
