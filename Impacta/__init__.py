from flask import Blueprint

Impacta_bp = Blueprint(
    'Impacta',
    __name__,
    template_folder= 'templates'
)
from . import controles