from flask import request, jsonify
from ..models.AdminRegister_model import Register
import bcrypt
from flask_jwt_extended import get_jwt_identity, create_access_token  # Assuming you're using Flask-JWT-Extended

def admin_signup(): 
    admin_collection = {
        'name': request.json.get('name'),
        'surname': request.json.get('surname'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    
    admin_user_id = get_jwt_identity() 
    if admin_user_id is None:
        if not get_admin.register_new_user(admin_collection): 
            return jsonify({'message': 'signup success'})
        else:
            return jsonify({'message': 'signup failed'}), 400
    else:
        return jsonify({'message': 'you are already signed up'}), 400
    
def admin_login():
    admin_login = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    
    user = get_admin.query.filter_by(email=admin_login['email']).first()
    if user and bcrypt.check_password_hash(user.password, admin_login['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'login success', 'access_token': access_token})
    else:
        return jsonify({'message': 'login failed'}), 400
