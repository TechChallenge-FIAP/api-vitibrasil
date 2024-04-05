import json
from flask import Blueprint, request
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)
from auth.models.user import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
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

@auth.route('/user', methods=['GET'])
@jwt_required()
def user():
    # Searching user by email
    current_user = User.query.filter_by(email=get_jwt_identity()).first()
    return {
        "email": current_user.email,
        "username": current_user.username,
    }

@auth.route('/singup', methods=['POST'])
def singup():
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