# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session


app = Flask(__name__)

app.secret_key = b'079ab6347ca7076405b152dba3bc593c2032318ad1069892272ab52d4df1c9a6'


@app.route('/', methods=["GET", "POST"])
def home():
    msg = ''
    if request.method == "POST":
        senha_atual = session.get('senha', 0)
        session.update(senha=senha_atual+1)
        msg = f'Olá {request.form["x"]}, sua senha é {session["senha"]}!'

    print(dict(request.form))
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
