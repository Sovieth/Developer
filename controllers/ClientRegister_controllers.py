from flask import request, jsonify
from ..models.ClientRegister_model import User
import bcrypt
from flask import get_jwt_identity, create_access_token  # Assuming you're using Flask-JWT-Extended

def signup(): 
    user_data = {
        'name': request.json.get('name'),
        'surname': request.json.get('surname'),
        'email': request.json.get('email'),
        'password': bcrypt.hashpw(request.json.get('password').encode('utf-8'), bcrypt.gensalt())
    }
    
    user_id = get_jwt_identity()
    if user_id is None:
        existing_user = User.query.filter_by(email=user_data['email']).first()
        if existing_user is None:
            new_user = User(**user_data)
            new_user.save()  # Assuming you have a save method in your User model
            return jsonify({'message': 'signup success'})
        else:
            return jsonify({'message': 'signup failed, user already exists'}), 400
    else:
        return jsonify({'message': 'you are already signed up'}), 400
    
def login():
    login_data = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    
    user = User.query.filter_by(email=login_data['email']).first()
    if user and bcrypt.checkpw(login_data['password'].encode('utf-8'), user.password.encode('utf-8')):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'login success', 'access_token': access_token})
    else:
        return jsonify({'message': 'login failed'}), 400
