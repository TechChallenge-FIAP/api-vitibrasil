from rest_api.database import db


class Produto(db.Model):

    __tablename__ = "producao_produtos"

    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(
        self,
        page: int,
        per_page: int,
        produto: str = None,
        categoria: str = None,
        ano: str = None,
    ):
        result = self.query

        if produto is not None:
            result = result.filter(self.produto.like("%" + produto + "%"))
        if categoria is not None:
            result = result.filter(self.categoria.like("%" + categoria + "%"))
        if ano is not None:
            result = result.filter_by(ano=ano)

        return result.paginate(page=page, per_page=per_page)
