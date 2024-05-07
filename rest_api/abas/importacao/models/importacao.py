from rest_api.database import db


class Importacao(db.Model):

    __tablename__ = "importacao"

    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(120), nullable=False)
    grupo = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    vl_dolar = db.Column(db.Double, nullable=False)
    qtd_kg = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(
        self,
        page: int,
        per_page: int,
        pais: str = None,
        grupo: str = None,
        ano: str = None,
    ):
        result = self.query

        if pais is not None:
            result = result.filter(self.pais.like("%" + pais + "%"))
        if grupo is not None:
            result = result.filter(self.grupo.like("%" + grupo + "%"))
        if ano is not None:
            result = result.filter_by(ano=ano)

        return result.paginate(page=page, per_page=per_page)
