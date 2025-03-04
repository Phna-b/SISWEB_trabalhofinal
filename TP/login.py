from classes import *
from flask_login import login_required, current_user, login_user, logout_user

@app.route('/login')
def login():
    return render_template('login/login.html')

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
    return redirect(url_for('exibir_grafico'))


@app.route('/signup')
def signup():
    return render_template('login/signup.html')

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
    return render_template('login/recovery.html')

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