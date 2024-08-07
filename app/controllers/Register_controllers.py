from flask import Flask, url_for, redirect, Response, request, render_template,flash, jsonify
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt
from..models.Register_model import user
from bson.objectid import ObjectId 

def signup():
    if request.method == 'POST':
        # Extract form data
        name = request.json.get('name')
        surname = request.json.get('surnamename')
        email = request.json.get('email')
        password = request.json.get('password')
        
        details = {'name': name, 'surname': surname,'email': email, 'password': password}
        user.create_new(details)
        
        return jsonify({"message": "successfully signup"})
    
def login():
     if request.method == 'POST':
       details =  {
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    
     user.create_new(details)
     return jsonify({"message": "successfully login"})
    
#     user = User.query.filter_by(email=login_data['email']).first()
#     if user and bcrypt.checkpw(login_data['password'].encode('utf-8'), user.password.encode('utf-8')):
#         access_token = create_access_token(identity=user.id)
#         return jsonify({'message': 'login success', 'access_token': access_token})
#     else:
#         return jsonify({'message': 'login failed'}), 400
