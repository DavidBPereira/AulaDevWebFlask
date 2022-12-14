
from flask import Flask
from Login import Login_bp

from Impacta import Impacta_bp
app = Flask(__name__)
app.config.from_object('app.config.Configuracao')


app.register_blueprint(Impacta_bp,url_prefix= '/Impacta')
app.register_blueprint(Login_bp,url_prefix= '/Login')