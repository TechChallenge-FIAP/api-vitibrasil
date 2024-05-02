from rest_api.database import db

class Exportacao(db.Model):

    __tablename__ = 'exportacao'

    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(120), nullable=False)
    grupo = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def find_by_grupo(self, grupo):
        return self.query.filter_by(grupo=grupo).all()
    
    @classmethod
    def find_by_ano(self, ano):
        return self.query.filter_by(ano=ano).all()
    
    @classmethod
    def find_by_pais(self, pais):
        return self.query.filter_by(pais=pais).all()
    
    @classmethod
    def find_by_grupo_and_ano(self, grupo, ano):
        return self.query.filter(
            self.grupo.like("%" + grupo + "%"), 
            self.ano.like(ano)
        ).all()

    @classmethod
    def all_grupo(self):
        return self.query.all()