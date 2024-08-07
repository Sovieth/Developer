from flask import Blueprint
from ..controllers import Register_controllers

app = Blueprint('Register', __name__)

app.route('/signup', methods=['POST'])( Register_controllers.signup)
app.route('/login', methods=['POST'])(Register_controllers.login)
