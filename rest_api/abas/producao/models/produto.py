from rest_api.database import db


class Produto(db.Model):

    __tablename__ = "producao_produtos"

    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_produto(self, produto):
        return self.query.filter_by(produto=produto).all()

    @classmethod
    def find_by_categoria(self, categoria):
        return self.query.filter_by(categoria=categoria).all()

    @classmethod
    def find_by_ano(self, ano):
        return self.query.filter_by(ano=ano).all()

    @classmethod
    def find_by_produto_and_categoria(self, produto, categoria):
        return self.query.filter(
            self.produto.like("%" + produto + "%"),
            self.categoria.like("%" + categoria + "%"),
        ).all()

    @classmethod
    def find_by_produto_and_ano(self, produto, ano):
        return self.query.filter(
            self.produto.like("%" + produto + "%"), self.ano.like(ano)
        ).all()

    @classmethod
    def find_by_categoria_and_ano(self, categoria, ano):
        return self.query.filter(
            self.categoria.like("%" + categoria + "%"), self.ano.like(ano)
        ).all()

    @classmethod
    def find_by_produto_and_categoria_and_ano(self, produto, categoria, ano):
        return self.query.filter(
            self.produto.like("%" + produto + "%"),
            self.categoria.like("%" + categoria + "%"),
            self.ano.like(ano),
        ).all()

    @classmethod
    def all_produto(self):
        return self.query.all()
