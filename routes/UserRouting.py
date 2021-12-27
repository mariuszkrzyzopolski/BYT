from flask import url_for, render_template, request, redirect, session, g

from main import app
from controllers.UserController import *


@app.before_request
def check_if_user_logged_in():
    name = session.get('username')
    if name is None:
        g.user = None
    else:
        g.user = User.query.filter_by(username=name).first()


@app.route("/")
def start():
    if session.get("logged_in") is None:
        return render_template('firstPage.html')
    else:
        return render_template('firstPage.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get("logged_in") is None:
        if request.method == 'GET':
            return render_template('logowanie.html')
        else:
            if request.form['loguj'] == "Zaloguj":
                name = request.form['username']
                password = request.form['password']
                data = User.query.filter_by(username=name, password=password).first()
                if data is not None:
                    session.clear()
                    session['logged_in'] = True
                    session['username'] = name
                    return redirect(url_for("start"))
                else:
                    alert = 'Niepoprawny login lub hasło, spróbuj ponownie'
                    return render_template('logowanie.html', alert=alert)
    else:
        return redirect(url_for('logout'))


@app.route("/logout")
def logout():
    """Logout Form"""
    # session['logged_in'] = None
    session.clear()
    g.user = None
    return redirect(url_for('start'))


@app.route("/account_edit", methods=['GET', 'POST'])
def edit_account():
    if session['logged_in']:
        if request.method == 'GET':
            return render_template('edycja.html')
        else:
            name = request.form['username']
            password = request.form['password']
            email = request.form['email']
            user = User.query.filter_by(username=name).first()
            if user is not None:
                if password is not None:
                    user.password = password
                if email is not None:
                    user.email = email
                db.session.commit()
                return redirect(url_for("start"))
            else:
                return "User don't exists"
    else:
        return redirect(url_for("login"))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get("logged_in") is None:
        if request.method == 'GET':
            return render_template('rejestracja.html')
        else:
            add_user(request.form['username'], request.form['email'], request.form['password'])
            session['username'] = request.form['username']
            return redirect(url_for("start"))
    else:
        session['logged_in'] = False
        return redirect(url_for("register"))


@app.route("/delete")
def delete_account():
    user = User.query.filter_by(username=session['username']).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("start"))
