from FaleConosco import FaleConosco_bp
from flask import render_template, session, request


@FaleConosco_bp.route('/')
def get_home():
    print('chamou o get')
    return render_template('FaleConosco.html')


@FaleConosco_bp.route('/', methods=['POST'])
def post_home():
    nome = f"Olá {request.form['name']} recebemos sua mensagem e em breve alguém da nossa equipe entrará em contato."
    print (request.form)
    return render_template('FaleConosco.html', nome=nome)
