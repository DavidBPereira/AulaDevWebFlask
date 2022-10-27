
from flask import Flask
from senha import senha_bp
from FaleConosco import FaleConosco_bp

app = Flask(__name__)
app.config.from_object('app.config.Configuracao')

app.register_blueprint(senha_bp, url_prefix='/senha')
app.register_blueprint(FaleConosco_bp, url_prefix='/FaleConosco')
