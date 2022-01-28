from flask import Flask # flask em si
from flask_sqlalchemy import SQLAlchemy # banco de dados
from flask_bcrypt import Bcrypt # criptografar senhas
from flask_login import LoginManager # fazer login

app = Flask(__name__)

# token seguro para formulários
app.config['SECRET_KEY'] = 'ec8a496147f41cf2ca2a3a74544c43bd'
# instanciar a criação do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

# criação do banco
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


# embaixo pq routes precisam do app para funcionar
from projetoflask import routes
