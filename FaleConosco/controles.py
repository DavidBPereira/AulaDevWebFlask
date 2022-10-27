from FaleConosco import FaleConosco_bp
from flask import render_template, session, request


@FaleConosco_bp.route('/')
def get_home():
    print('chamou o get')
    return render_template('FaleConosco.html')


@FaleConosco_bp.route('/', methods=['POST'])
def post_home():
    print('chamou o post')
    dicionario = {'nome': request.form["name"],
                  'email': request.form["e-mail"],
                  'telefone': request.form["telefone"],
                  'Como nos conheceu': request.form["question"]
                  }
    print(dicionario)
    return render_template('FaleConosco.html',**dicionario)
