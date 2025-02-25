from datetime import datetime
import os
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

@app.route("/")
def base():
    return render_template("login/login.html")


##Adicionar página do dia de treino, adicionar atividades a esse objeto


@app.route("/novoTreinoPagina")
@login_required
def novoTreinoPagina():
    return render_template("treino/novoTreino.html")

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

@app.route("/listarTreino/<int:id>", methods=['GET','POST'])
@login_required
def listarTreino(id):
    atividades = Atividade.query.filter_by(treino_id=id)
    treino = Treino.query.filter_by(_id=id).first()

    if(request.method == "POST"):
        nome = request.form.get("nome")
        carga = request.form.get("carga")
        series = request.form.get("series")
        repeticoes = request.form.get("repeticoes")
        idtreino = id

        if nome and carga and series and repeticoes:
            p = Atividade(nome, carga, series, repeticoes,idtreino)
            db.session.add(p)
            db.session.commit()


    return render_template("treino/listarTreino.html", treino=treino, atividades=atividades)


@app.route("/atualizarAtividadesTreino/<int:id>", methods=['GET','POST'])
@login_required
def atualizarAtvTreino(id):
    atividade  = Atividade.query.filter_by(_id=id).first()

    if(request.method == "POST"):
        nome = request.form.get("nome")
        carga = request.form.get("carga")
        repeticoes = request.form.get("repeticoes")
        series = request.form.get("series")

        if nome and carga and series and repeticoes:
            atividade.nome = nome
            atividade.carga = carga
            atividade.series = series
            atividade.repeticoes = repeticoes
            db.session.commit()

            return redirect(url_for("listarTreino", id=atividade.treino_id))
    return render_template("treino/atualizarAtividadesTreino.html",atividade=atividade)



@app.route("/excluirAtvTreino/<int:id>")
@login_required
def excluirAtvTreino(id):
    atividade = Atividade.query.filter_by(_id=id).first()

    idRef = atividade.treino_id

    db.session.delete(atividade)

    db.session.commit()

    return redirect(url_for("listarTreino", id=idRef))




@app.route("/excluirTreino/<int:id>")
@login_required
def excluirTreino(id):
    treino = Treino.query.filter_by(_id=id).first()

    treinoAtv = Atividade.query.filter_by(treino_id=id).all()

    db.session.delete(treino)

    for atividade in treinoAtv:
        db.session.delete(atividade)

    db.session.commit()

    return redirect(url_for("listaDeTreinos"))


@app.route("/atualizarTreino/<int:id>", methods=['GET','POST'])
@login_required
def atualizarTreino(id):
    treino  = Treino.query.filter_by(_id=id).first()

    if(request.method == "POST"):
        nome = request.form.get("nome")
        data = request.form.get("data")

        if nome and data:
            treino.nome = nome
            expiration_year = int(data[:4])
            expiration_month = int(data[5:7])
            expiration_date = int(data[8:10])
            expiration_date = datetime(expiration_year, expiration_month, expiration_date)
            treino.data = expiration_date

            db.session.commit()

            return redirect(url_for("listaDeTreinos"))
    return render_template("treino/atualizarTreino.html",treino=treino)

#####################################################
# Rota para upload de vídeos

@app.route('/videos')
def videos():
    videos = Video.query.all()
    return render_template('videos/videos.html', videos=videos)

# Rota para upload de vídeos
@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400

    file = request.files['file']

    if file.filename == '':
        return "Nome de arquivo inválido", 400


    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    new_video = Video(title=request.form['title'], filename=filename)
    db.session.add(new_video)
    db.session.commit()

    return redirect(url_for('videos'))

@app.route("/sidebar")
def sidebar():
    return render_template("sidebar.html")

if __name__ == "__main__":
    app.run(debug=True)




