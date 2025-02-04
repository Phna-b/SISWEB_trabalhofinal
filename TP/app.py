from datetime import datetime

from flask import Flask, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from classes import *
from login import *

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

@app.route("/")
def base():
    return render_template("login.html")


####################################################### Atividades

@app.route("/cadastrarAtividadePagina")
@login_required
def cadastrarAtividadePagina():
    return render_template("cadastroAtv.html")

@app.route("/cadastrarAtividade", methods=['GET','POST'])
@login_required
def cadastrarAtividade():
    if(request.method == "POST"):
        nome = request.form.get("nome")
        carga = request.form.get("carga")
        series = request.form.get("series")
        repeticoes = request.form.get("repeticoes")

        if nome and carga and series and repeticoes:
            p = Atividade(nome, carga, series, repeticoes)
            db.session.add(p)
            db.session.commit()
    return redirect(url_for("index"))

##Adicionar página do dia de treino, adicionar atividades a esse objeto


@app.route("/novoTreinoPagina")
@login_required
def novoTreinoPagina():
    return render_template("novoTreino.html")

@app.route("/novoTreino", methods=['GET','POST'])
@login_required
def novoTreino():
    if(request.method == "POST"):
        nome = request.form.get("nome")
        data = request.form.get("data")

        expiration_year = int(data[:4])
        expiration_month = int(data[5:7])
        expiration_date = int(data[8:10])
        expiration_date = datetime(expiration_year, expiration_month, expiration_date)

        if nome and data:
            p = Treino(nome, expiration_date)
            db.session.add(p)
            db.session.commit()
    return redirect(url_for("index"))

@app.route("/listaDeTreinos")
@login_required
def listaDeTreinos():
    treinos = Treino.query.filter_by(conta_id=current_user.id)
    return render_template("treino/lista.html", treinos = treinos)






if __name__ == "__main__":
    app.run(debug=True)




