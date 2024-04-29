from flask import Flask
from flask_jwt_extended import JWTManager
from rest_api.database import db
from rest_api.swagger import api
from flask_migrate import Migrate
from rest_api.auth import Singup, Login
from rest_api.abas import (
    ProducaoProduto,
    ProducaoCategoria,
    Processamento,
    Importacao,
    Exportacao,
    ComercializacaoProduto,
    ComercializacaoCategoria,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "banana"
app.config["PROPAGATE_EXCEPTIONS"] = True

api.add_resource(Singup, "/auth/singup")
api.add_resource(Login, "/auth/login")
api.add_resource(ProducaoProduto, "/producao/produto")
api.add_resource(ProducaoCategoria, "/producao/categoria")
api.add_resource(Processamento, "/processamento")
api.add_resource(Importacao, "/importacao")
api.add_resource(Exportacao, "/exportacao")
api.add_resource(ComercializacaoProduto, "/comercializacao/produto")
api.add_resource(ComercializacaoCategoria, "/comercializacao/categoria")
api.init_app(app)

# configure Flask App with JWT support
jwt = JWTManager(app)

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
