from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from swagger import api
from services.database import create_connection

class Exportacao(Resource):
    @api.doc(security='Bearer')
    @jwt_required()
    def get(self):
        conn = create_connection()

        cursor = conn.cursor()

        query = f"select * from exportacao limit 10"

        rows = cursor.execute(query).fetchall()

        conn.commit()
        conn.close()

        return jsonify([dict(ix) for ix in rows])