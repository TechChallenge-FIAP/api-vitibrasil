from rest_api.database import db


class Produto(db.Model):

    __tablename__ = "comercio_produtos"

    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(
        self, produto: str = None, categoria: str = None, ano: str = None
    ):
        result = self.query

        print(produto)
        print(categoria)
        print(ano)

        if produto is not None:
            result = result.filter(self.produto.like("%" + produto + "%"))
        if categoria is not None:
            result = result.filter(self.categoria.like("%" + categoria + "%"))
        if ano is not None:
            result = result.filter_by(ano=ano)

        return result.all()
