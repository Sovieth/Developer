from .. import mongo

class Register:
    
    def register_new_user(self, signup):
        existing_user = mongo.db.new_admin.find_one({'email': signup['email']})
        if existing_user:
            return {'success': False, 'message': 'User already exists'}
        
        result = mongo.db.new_admin.insert_one(signup)
        if result.inserted_id:
            return {'success': True, 'message': 'User registered successfully'}
        else:
            return {'success': False, 'message': 'Registration failed'}

    def query_filter_by(self, email):
        user = mongo.db.new_admin.find_one({'email': email})
        return user


    
    
    
    
    