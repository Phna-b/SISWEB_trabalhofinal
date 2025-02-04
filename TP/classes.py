from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user,LoginManager,UserMixin

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,mapped_column
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
    conta_id = mapped_column(ForeignKey("conta.id"))

    conta = relationship("Conta", back_populates="pessoa")

    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.conta_id = current_user.id

class Conta(db.Model, UserMixin):

    __tablename__ = 'conta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    email = db.Column(db.String,unique=True)
    password = db.Column(db.String(100))
    pessoa = relationship("Pessoa", back_populates="conta")
    atividade = relationship("Atividade", back_populates="conta")
    treino = relationship("Treino", back_populates="conta")

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


class Atividade(db.Model):

    __tablename__ = 'atividade'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    carga = db.Column(db.Float)
    series = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer)
    conta_id = mapped_column(ForeignKey("conta.id"))

    conta = relationship("Conta", back_populates="atividade")

    def __init__(self, nome, carga, series, repeticoes):
        self.nome = nome
        self.carga = carga
        self.series = series
        self.repeticoes = repeticoes
        self.conta_id = current_user.id


class Treino(db.Model):

    __tablename__ = 'treino'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    data = db.Column(db.Date)
    conta_id = mapped_column(ForeignKey("conta.id"))

    conta = relationship("Conta", back_populates="treino")

    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.conta_id = current_user.id

db.create_all()