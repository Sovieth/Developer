from flask import request, jsonify
from ..models.ClientRegister_model import User
import bcrypt
from flask_jwt_extended import get_jwt_identity, create_access_token  # Assuming you're using Flask-JWT-Extended

def signup(): 
    user_collection = {
        'name': request.json.get('name'),
        'surname': request.json.get('surname'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    
    user_id = get_jwt_identity() 
    if user_id is None:
        if not user_collection.register_new_user(user_collection): 
            return jsonify({'message': 'signup success'})
        else:
            return jsonify({'message': 'signup failed'}), 400
    else:
        return jsonify({'message': 'you are already signed up'}), 400
    
def login():
    login = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    
    user = login.query.filter_by(email=login['email']).first()
    if user and bcrypt.check_password_hash(user.password, login['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'login success', 'access_token': access_token})
    else:
        return jsonify({'message': 'login failed'}), 400
