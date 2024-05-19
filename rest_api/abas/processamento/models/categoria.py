from rest_api.database import db


class Categorias(db.Model):

    __tablename__ = "processamento_categorias"

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(
        self,
        page: int,
        per_page: int,
        categoria: str = None,
        ano: str = None,
    ):
        result = self.query

        if categoria is not None:
            result = result.filter("%" + categoria + "%")
        if ano is not None:
            result = result.filter_by(ano=ano)

        return result.paginate(page=page, per_page=per_page)
