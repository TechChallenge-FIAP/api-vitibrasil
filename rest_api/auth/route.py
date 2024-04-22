import json
from flask import request, jsonify
from flask_restx import Resource, fields
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)
from rest_api.swagger import api
from rest_api.auth.models.user import User

class Singup(Resource):
    @api.expect(api.model('Singup', {
        'username': fields.String(required=True, description='Nome do usuário'),
        'email': fields.String(required=True, description='E-mail do usuário'),
        'password': fields.String(required=True, description='Senha do usuário')
    }))
    def post(self):
        data = json.loads(request.data)
        username = data['username']
        email = data['email']
        password = data['password']

        # Searching user by email
        current_user = User.find_by_email(email)
            
        if current_user:
            return f'O usuário com e-mail {email} já existe|', 400
            
        user = User(
            username=username, 
            email=email,
            password=password,
        )

        User.save(user)

        return 'Usuario criado'

class Login(Resource):
    @api.doc(security='Bearer')
    @jwt_required()
    def get(self):
        try:
            # Searching user by email
            current_user = User.query.filter_by(email=get_jwt_identity()).first()
            return {
                "email": current_user.email,
                "username": current_user.username,
            }
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @api.expect(api.model('Login', {
        'email': fields.String(required=True, description='E-mail do usuário'),
        'password': fields.String(required=True, description='Senha do usuário')
    }))
    def post(self):
        data = json.loads(request.data)
        email = data['email']

        # Searching user by email
        current_user = User.find_by_email(email)
            
        if not current_user:
            return f'O usuário com e-mail {email} não existe|', 400
            
        # user exists, comparing password and hash
        if User.verify_hash(data['password'], current_user.password):
            # generating access token and refresh token
            access_token = create_access_token(identity=email)
        
            return {
                'token': access_token
            }

        else:
            return "Senha invalida!", 400
