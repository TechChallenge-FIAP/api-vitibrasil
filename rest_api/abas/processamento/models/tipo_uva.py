from rest_api.database import db


class Tipouva(db.Model):

    __tablename__ = "processamento_tipo_uva"

    id = db.Column(db.Integer, primary_key=True)
    grupo = db.Column(db.String(120), nullable=False)
    sub_categoria = db.Column(db.String(120), nullable=False)
    tipo_uva = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(
        self,
        page: int,
        per_page: int,
        grupo: str = None,
        sub_categoria: str = None,
        tipo_uva: str = None,
        ano: str = None,
    ):
        result = self.query

        if grupo is not None:
            result = result.filter(self.grupo.like("%" + grupo + "%"))
        if sub_categoria is not None:
            result = result.filter(self.sub_categoria.like("%" + sub_categoria + "%"))
        if tipo_uva is not None:
            result = result.filter(self.tipo_uva.like("%" + tipo_uva + "%"))
        if ano is not None:
            result = result.filter_by(ano=ano)

        return result.paginate(page=page, per_page=per_page)
