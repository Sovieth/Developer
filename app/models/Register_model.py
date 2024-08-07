from flask_bcrypt import Bcrypt
from .. import mongo

class user:
    def create_new(details):
        return mongo.db.user.insert_one(details)
    
    def login(details):
        return mongo.db.user.insert_one(details)