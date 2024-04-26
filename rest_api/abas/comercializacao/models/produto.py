from rest_api.database import db


class Produto(db.Model):

    __tablename__ = "comercio_produto"

    id = db.Column(db.Integer, primary_key=True)
    produtos = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(
        self, produto: str = None, categoria: str = None, ano: str = None
    ):
        query = self.query

        if produto is not None:
            query = query.filter("%" + produto + "%")
        if categoria is not None:
            query = query.filter("%" + categoria + "%")
        if ano is not None:
            query = query.filter_by(ano=ano)

        return query.all()
