from Impacta import Impacta_bp
from flask import render_template, session, request, redirect, url_for


@Impacta_bp.route('/')
def get_home():
    id_sessao = request.cookies.get('id_sessao')
    sessao = session.get(id_sessao)
    print(sessao)

    if sessao is None:
        print('usuário não autenticado, redirecionando...')
        return redirect(url_for('Login.get_login'))

    print(f'GET: O cookie enviado pelo navegador é: {id_sessao}')
    return render_template('Impacta.html')



@Impacta_bp.route('/', methods=['POST'])
def post_home():
    print('chamou o post')
    return render_template('Impacta.html')
