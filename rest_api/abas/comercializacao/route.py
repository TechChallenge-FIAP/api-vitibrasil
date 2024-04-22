from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from rest_api.swagger import api
from services.database import create_connection


class Comercializacao(Resource):
    @api.doc(security="Bearer")
    @jwt_required()
    def get(self):
        conn = create_connection()

        cursor = conn.cursor()

        table = "categorias"

        query = f"select * from comercio_{table}"

        rows = cursor.execute(query).fetchall()

        conn.commit()
        conn.close()

        return jsonify([dict(ix) for ix in rows])
