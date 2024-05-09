from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource 
from rest_api.swagger import api
from rest_api.abas.producao.models import Produto, Categoria

class ProducaoProduto(Resource):
    @api.doc(params={
        "produto": "Nome do produto",
        "categoria": "Categoria do produto",
        "ano": "Ano de produção do produto",
        "page": "Página",
        "per_page": "Resultados por página",
    })
    @api.doc(security='Bearer')
    @jwt_required()
    def get(self):
        produto = request.args.get('produto')
        categoria = request.args.get('categoria')
        ano = request.args.get('ano')
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)

        producao_produtos = Produto.execute_query(
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
                for produto in producao_produtos
            ],
            "pagination": {
                "count": producao_produtos.total,
                "page": page,
                "per_page": per_page,
                "pages": producao_produtos.pages,
            },
        }
        
class ProducaoCategoria(Resource):
    @api.doc(params={
        'categoria': 'Nome da categoria',
        'ano': 'Ano de produção da categoria do produto',
        "page": "Página",
        "per_page": "Resultados por página",
    })
    @api.doc(security='Bearer')
    @jwt_required()
    def get(self):
        categoria = request.args.get('categoria')
        ano = request.args.get('ano')
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=50, type=int)

        producao_categorias = Categoria.execute_query(categoria, ano)
        
        return {
            "data": [
                {
                    "categoria": producao_categoria.categoria,
                    "ano": producao_categoria.ano,
                    "quantidade_l": producao_categoria.quantidade_l
                } 
                for producao_categoria in producao_categorias
            ],
            "pagination": {
                "count": producao_categorias.total,
                "page": page,
                "per_page": per_page,
                "pages": producao_categorias.pages,
            },
        }