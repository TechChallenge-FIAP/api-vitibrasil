from flask import Flask
from flask_jwt_extended import JWTManager
from database import db
from swagger import api
from auth import Singup, Login
from abas import Producao, Processamento, Importacao, Exportacao, Comercializacao

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'banana'
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)

api.add_resource(Singup, '/auth/singup')
api.add_resource(Login, '/auth/login')
api.add_resource(Producao, '/producao')
api.add_resource(Processamento, '/processamento')
api.add_resource(Importacao, '/importacao')
api.add_resource(Exportacao, '/exportacao')
api.add_resource(Comercializacao, '/comercializacao')
api.init_app(app)

# configure Flask App with JWT support
jwt = JWTManager(app) 

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run('localhost', 5000, use_reloader=True, use_debugger=True)
