from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='/static')
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

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


class Conta(db.Model):

    __tablename__ = 'conta'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    email = db.Column(db.String,unique=True)
    password = db.Column(db.String(100))

    def __init__(self, nome, email,password):
        self.nome = nome
        self.email = email
        self.password = password

db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")
@app.route("/cadastro", methods=['GET','POST'])
def cadastro():
    if(request.method == "POST"):
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        email = request.form.get("email")

        if nome and telefone and cpf and email:
            p = Pessoa(nome, telefone, cpf, email)
            db.session.add(p)
            db.session.commit()
    return redirect(url_for("index"))

@app.route("/lista")
def lista():
    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas = pessoas)

@app.route("/excluir/<int:id>")
def excluir(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas = pessoas)

@app.route("/atualizar/<int:id>", methods=['GET','POST'])
def atualizar(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    if(request.method == "POST"):
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        email = request.form.get("email")

        if nome and telefone and email:
            pessoa.nome = nome
            pessoa.telefone = telefone
            pessoa.email = email

            db.session.commit()

            return redirect(url_for("lista"))
    return render_template("atualizar.html",pessoa=pessoa)


@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    nome = request.form.get('nome')
    password = request.form.get('password')


    user = Conta.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('signup'))

    if nome and email and password:
        new_user = Conta(email=email, nome=nome,password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))










@app.route("/")
def base():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)




