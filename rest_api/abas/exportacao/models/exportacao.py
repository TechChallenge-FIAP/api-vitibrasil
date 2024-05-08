from rest_api.database import db

class ExportacaoEmbrapa(db.Model):

    __tablename__ = 'exportacao'

    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(120), nullable=False)
    grupo = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    vl_dolar = db.Column(db.Integer, nullable=False)
    qtd_kg = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def execute_query(
        self,
        page: int,
        per_page: int,
        pais: str = None,
        ano: str = None,
        grupo: str = None):

        print(pais)
        print(ano)
        print(grupo)

        result = self.query

        if pais is not None:
            result.filter(self.pais.like("%" + pais + "%"))
        if ano is not None:
            result = result.filter_by(ano=ano)
        if grupo is not None:
            result = result.filter(self.grupo.like("%" + grupo + "%"))
        return result.paginate(page=page, per_page=per_page)