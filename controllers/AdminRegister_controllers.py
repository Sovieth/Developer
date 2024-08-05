from flask import request, jsonify
from ..models.AdminRegister_model import Register
import bcrypt
from flask_jwt_extended import get_jwt_identity, create_access_token  # Assuming you're using Flask-JWT-Extended

def admin_signup():
    admin_data = {
        'name': request.json.get('name'),
        'surname': request.json.get('surname'),
        'email': request.json.get('email'),
        'password': bcrypt.hashpw(request.json.get('password').encode('utf-8'), bcrypt.gensalt())
    }
    
    admin_user_id = get_jwt_identity()
    if admin_user_id is None:
        existing_admin = Register.query.filter_by(email=admin_data['email']).first()
        if existing_admin is None:
            new_admin = Register(**admin_data)
            new_admin.save()  # Assuming you have a save method in your Register model
            return jsonify({'message': 'signup success'})
        else:
            return jsonify({'message': 'signup failed, admin already exists'}), 400
    else:
        return jsonify({'message': 'you are already signed up'}), 400

def admin_login():
    login_data = {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    
    user = Register.query.filter_by(email=login_data['email']).first()
    if user and bcrypt.checkpw(login_data['password'].encode('utf-8'), user.password.encode('utf-8')):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'login success', 'access_token': access_token})
    else:
        return jsonify({'message': 'login failed'}), 400
