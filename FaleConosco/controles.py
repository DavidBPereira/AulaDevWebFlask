from FaleConosco import FaleConosco_bp
from flask import render_template, session, request


@FaleConosco_bp.route('/')
def get_home():
    print('chamou o get')
    return render_template('FaleConosco.html')


@FaleConosco_bp.route('/', methods=['POST'])
def post_home():
    print('chamou o post', dict(request.form))
    return render_template('FaleConosco.html')
