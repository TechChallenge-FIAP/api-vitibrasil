from rest_api.database import db


class Categoria(db.Model):

    __tablename__ = "comercio_categorias"

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(self, categoria: str = None, ano: str = None):
        query = self.query

        if categoria is not None:
            query = query.filter("%" + categoria + "%")
        if ano is not None:
            query = query.filter_by(ano=ano)

        return query.all()
