from Impacta import Impacta_bp
from flask import render_template, session, request


@Impacta_bp.route('/')
def get_home():
    print('chamou o get')
    return render_template('Impacta.html')


@Impacta_bp.route('/', methods=['POST'])
def post_home():
    print('chamou o post')
    return render_template('Impacta.html')
