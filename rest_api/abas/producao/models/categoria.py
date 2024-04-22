from rest_api.database import db

class Categoria(db.Model):

    __tablename__ = 'producao_categorias'

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    quantidade_l = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def find_by_categoria(self, categoria):
        return self.query.filter_by(categoria=categoria).all()
    
    @classmethod
    def find_by_ano(self, ano):
        return self.query.filter_by(ano=ano).all()
    
    @classmethod
    def find_by_categoria_and_ano(self, categoria, ano):
        return self.query.filter(
            self.categoria.like("%" + categoria + "%"), 
            self.ano.like(ano)
        ).all()

    @classmethod
    def all_categoria(self):
        return self.query.all()