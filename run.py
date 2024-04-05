from flask import Flask
from flask_jwt_extended import JWTManager
from database import db
from auth import auth
from abas import (
    comercializacao, 
    exportacao, 
    importacao, 
    processamento, 
    producao
)

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(comercializacao)
app.register_blueprint(exportacao)
app.register_blueprint(importacao)
app.register_blueprint(processamento)
app.register_blueprint(producao)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'banana'

db.init_app(app)

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run('localhost', 5000, use_reloader=True, use_debugger=True)

# Para criar o banco de dados sqlite
# comente as 2 linhas acima, descomente as linha abaixo e execute o arquivo.

#def create_db():
#    with app.app_context():
#        db.create_all()
# 
#if __name__ == "__main__":
#    from auth.models.user import User
#    create_db()