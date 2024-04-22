import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restx import Resource 
from rest_api.swagger import api
from rest_api.abas.producao.models import Produto, Categoria

class ProducaoProduto(Resource):
    @api.doc(params={
        'produto': 'Nome do produto',
        'categoria': 'Categoria do produto',
        'ano': 'Ano de produção do produto'
    })
    @api.doc(security='Bearer')
    @jwt_required()
    def get(self):
        produto = request.args.get('produto')
        categoria = request.args.get('categoria')
        ano = request.args.get('ano')

        if produto and categoria and ano:
            producao_produtos = Produto.find_by_produto_and_categoria_and_ano(produto, categoria, ano)
        elif produto and categoria:
            producao_produtos = Produto.find_by_produto_and_categoria(produto, categoria)
        elif produto and ano:
            producao_produtos = Produto.find_by_produto_and_ano(produto, ano)
        elif categoria and ano:
            producao_produtos = Produto.find_by_categoria_and_ano(categoria, ano)
        elif produto:
            producao_produtos = Produto.find_by_produto(produto)
        elif categoria:
            producao_produtos = Produto.find_by_categoria(categoria)
        elif ano:
            producao_produtos = Produto.find_by_ano(ano)
        else:
            producao_produtos = Produto.all_produto()
        
        return {
            "data": [{
                "produto": producao_produto.produto,
                "categoria": producao_produto.categoria,
                "ano": producao_produto.ano,
                "quantidade_l": producao_produto.quantidade_l
            } for producao_produto in producao_produtos]
        }
        
class ProducaoCategoria(Resource):
    @api.doc(params={
        'categoria': 'Nome da categoria',
        'ano': 'Ano de produção da categoria do produto'
    })
    @api.doc(security='Bearer')
    @jwt_required()
    def get(self):
        categoria = request.args.get('categoria')
        ano = request.args.get('ano')

        if categoria and ano:
            producao_categorias = Categoria.find_by_categoria_and_ano(categoria)
        elif categoria:
            producao_categorias = Categoria.find_by_categoria(categoria)
        elif ano:
            producao_categorias = Categoria.find_by_ano(ano)
        else:
            producao_categorias = Categoria.all_categoria()
        
        return {
            "data": [{
                "categoria": producao_categoria.categoria,
                "ano": producao_categoria.ano,
                "quantidade_l": producao_categoria.quantidade_l
            } for producao_categoria in producao_categorias]
        }