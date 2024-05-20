from rest_api.database import db


class Categorias(db.Model):

    __tablename__ = "processamento_categorias"

    id = db.Column(db.Integer, primary_key=True)
    grupo = db.Column(db.String(120), nullable=False)
    sub_categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_kg = db.Column(db.Integer, nullable=False)

    @classmethod
    def execute_query(
        self,
        page: int,
        per_page: int,
        grupo: str = None,
        sub_categoria: str = None,
        ano: str = None,
    ):
        result = self.query
            
        if grupo is not None:
            result = result.filter("%" + grupo + "%")
        
        if sub_categoria is not None:
            result = result.filter("%" + sub_categoria + "%")
                
        if ano is not None:
            result = result.filter_by(ano=ano)

        return result.paginate(page=page, per_page=per_page)
