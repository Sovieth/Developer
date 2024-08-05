from .. import mongo
from flask import request, redirect, url_for, render_template

class Register:
    
    def register_new_user(signup):
        
        existing_user = mongo.db.new_admin.find_one({'email': signup['email']})
        if existing_user:
            return True
        
        result = mongo.db.new_admin.insert_one(signup)
        return False if result.inserted_id else True
    
    def queryfilter_by(email):
        user = mongo.db.new_admin.find_one({'email': email})
        return user