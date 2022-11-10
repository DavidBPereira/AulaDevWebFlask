import uuid

from flask import redirect, render_template, request, session, url_for, make_response

from Login import Login_bp

def validacao(dicionario,usuarios):
    for i in dicionario:
        if i == 'usuario':
            if dicionario[i] in usuarios.keys():
               continue
            else:
                return False 
        if i == 'senha':
            if dicionario[i] in usuarios.values():
                return True
            else:
                return False
                

@Login_bp.route('/', methods = ['GET'])
def get_login():
    return render_template('index.html')


@Login_bp.route('/', methods = ['POST'])
def post_login():
    id_sessao = str(uuid.uuid1())  # cria a chave da sessão
    nome = request.form['username']
    senha = request.form['pass']
    sessao = {'usuario': nome,
              'senha' : senha}
    # salva os dados pertinentes à aplicação no
    session.update({id_sessao : sessao})
    # objeto de sessão do flask
    usuarios = {'usuarioteste': 'teste@123'}
    v = validacao(sessao,usuarios)
    if v == True:
        resposta = make_response(redirect(url_for('Impacta.get_home')))
        resposta.set_cookie('id_sessao', id_sessao)
        return resposta
    else: 
         return redirect(url_for('.get_login')) 

    

@Login_bp.route('/logout', methods=['GET'])
def logout():
    id_sessao = request.cookies.get('id_sessao')
    session.pop(id_sessao, None)

    resposta = make_response(redirect(url_for('.get_login')))
    resposta.set_cookie('id_sessao', '')
    return resposta