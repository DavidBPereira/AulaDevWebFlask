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

@Impacta_bp.route('/bd.html')
def get_bd():
    return render_template('bd.html')

@Impacta_bp.route('/defesa-cibernetica.html')
def get_def():
    return render_template('defesa-cibernetica.html')

@Impacta_bp.route('/eng-compute.html')
def get_end():
    return render_template('eng-compute.html')

@Impacta_bp.route('/sistema-info.html')
def get_si():
    return render_template('sistema-info.html')

@Impacta_bp.route('/ads.html')
def get_ads():
    return render_template('ads.html')

@Impacta_bp.route('/index.html')
def get_index():
    return redirect(url_for('.get_home'))
    