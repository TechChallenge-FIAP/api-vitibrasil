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
        }
    )
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        produto = request.args.get("produto")
        categoria = request.args.get("categoria")
        ano = request.args.get("ano")

        comercializacao_produtos = Produto.execute_query(produto, categoria, ano)

        return {
            "data": [
                {
                    "produto": produto.produto,
                    "categoria": produto.categoria,
                    "ano": produto.ano,
                    "quantidade_l": produto.quantidade_l,
                }
                for produto in comercializacao_produtos
            ]
        }


class ComercializacaoCategoria(Resource):
    @api.doc(
        params={
            "categoria": "Categoria do produto",
            "ano": "Ano de produção do produto",
        }
    )
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        categoria = request.args.get("categoria")
        ano = request.args.get("ano")

        comercializacao_categorias = Categoria.execute_query(categoria, ano)

        return {
            "data": [
                {
                    "produto": categoria.produto,
                    "categoria": categoria.categoria,
                    "ano": categoria.ano,
                    "quantidade_l": categoria.quantidade_l,
                }
                for categoria in comercializacao_categorias
            ]
        }
