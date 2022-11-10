from flask import Blueprint

Login_bp = Blueprint(
    'Login',
    __name__,
    template_folder= 'templates'
)
from . import controles