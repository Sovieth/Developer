from flask import Blueprint
from ..controllers import AdminRegister_controllers

app = Blueprint('AdminRegister', __name__)

app.route('admin_signup', method=['POST'])(AdminRegister_controllers.Adminsignup)
app.route('admin_login', method=['POST'])(AdminRegister_controllers.Adminsignup)