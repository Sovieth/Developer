from flask import Blueprint
from ..controllers import ClientRegister_controllers

app = Blueprint('Register', __name__)

app.route('/signup', methods=['POST'])( ClientRegister_controllers.signup)
app.route('/login', methods=['POST'])( ClientRegister_controllers.login)
