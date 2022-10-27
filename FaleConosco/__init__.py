from flask import Blueprint

FaleConosco_bp = Blueprint(
    'FaleConosco',
    __name__,
    template_folder='templates'
)

from . import controles