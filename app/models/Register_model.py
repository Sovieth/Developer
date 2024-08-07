from flask_bcrypt import Bcrypt
from .. import mongo

class User:
    def create_new(details):
        return mongo.db.user.insert_one(details)