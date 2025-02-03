from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user, login_user, logout_user

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from classes import *



@app.route("/index")
@login_required
def index():
    return render_template("index.html")

@app.route("/cadastrar")
@login_required
def cadastrar():
    return render_template("cadastro.html")
@app.route("/cadastro", methods=['GET','POST'])
@login_required
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
@login_required
def lista():
    pessoas = Pessoa.query.filter_by(conta_id=current_user.id)
    #pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas = pessoas)

@app.route("/excluir/<int:id>")
@login_required
def excluir(id):
    pessoa = Pessoa.query.filter_by(_id=id).first()

    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas = pessoas)

@app.route("/atualizar/<int:id>", methods=['GET','POST'])
@login_required
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

@app.route('/login', methods=['GET','POST'])
def login_post():

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Conta.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Verifique seus dados e tente novamente!')
        return redirect(url_for('login'))

    login_user(user)  # Faz login do usuário  --- E mantém os daods salvos
    return redirect(url_for('index'))


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['GET','POST'])
def signup_post():
    email = request.form.get('email')
    nome = request.form.get('nome')
    password = request.form.get('password')


    user = Conta.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('O e-mail indicado já está cadastrado!')
        return redirect(url_for('signup'))

    if nome and email and password:
        new_user = Conta(email=email, nome=nome,password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

@app.route('/recovery')
def recovery():
    return render_template('recovery.html')

@app.route("/recovery", methods=['GET','POST'])
def recovery_post():
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    conta = Conta.query.filter_by(email=email).first()

    if not conta: # if a user is found, we want to redirect back to signup page so user can try again
        flash('O e-mail indicado não possui cadastrado!')
        return redirect(url_for('login'))
    if password != password2:
        flash('As senhas não são iguais! Digite novamente.')
        return redirect(url_for('recovery'))


    conta.password = generate_password_hash(password, method='pbkdf2:sha256')
    db.session.commit()
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    logout_user()  # Faz logout do usuário
    flash('Você saiu da conta!', 'success')
    return redirect(url_for('login'))  # Redireciona para a página de login

@app.route("/")
def base():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)




