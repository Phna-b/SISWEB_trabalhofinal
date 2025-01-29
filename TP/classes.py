from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user,LoginManager,UserMixin

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='/static')
app.app_context().push()
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

#Configuração para impedir acesso das páginas sem login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user):
    return Conta.query.get(int(user))

########

class Pessoa(db.Model):

    __tablename__ = 'cliente'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    cpf = db.Column(db.String)
    email = db.Column(db.String,unique=True)


    def __init__(self, nome, telefone, cpf, email,password):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email


class Conta(db.Model, UserMixin):

    __tablename__ = 'conta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    email = db.Column(db.String,unique=True)
    password = db.Column(db.String(100))

    def __init__(self, nome, email,password):
        self.nome = nome
        self.email = email
        self.password = password


    def get_id(self):
        return str(self.id)  # Retorna o ID como string (requerido pelo Flask-Login)

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

db.create_all()