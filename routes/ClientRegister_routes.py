from flask import Blueprint
from ..controllers import Register_controllers

app = Blueprint('Register', __name__)

app.route('signup', method=['POST'])(Register_controllers.signup)
app.route('login', method=['POST'])(Register_controllers.login)