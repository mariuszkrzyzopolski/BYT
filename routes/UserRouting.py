from flask import url_for, render_template, request, redirect, session

from main import app
from controllers.UserController import *
from controllers.FrendshipController import *


@app.route("/")
def start():
    if session.get("username") is None:
        return render_template('firstPage.html')
    else:
        return render_template('firstPage.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get("username") is None:
        if request.method == 'POST':
            data = User.query.filter_by(
                username=request.form['username'],
                password=request.form['password']
            ).first()
            if data is not None:
                session.clear()
                session['username'] = request.form['username']
                return redirect(url_for("start"))
            else:
                alert = 'Niepoprawny login lub hasło, spróbuj ponownie'
                return render_template('logowanie.html', alert=alert)
        else:
            return render_template('logowanie.html')
    else:
        return redirect(url_for('logout'))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('start'))


@app.route("/account_edit", methods=['GET', 'POST'])
def edit_account():
    if session.get("username") is not None:
        if request.method == 'POST':
            edited = edit_user(session.get("username"), request.form['email'], request.form['password'])
            if edited is not None and request.form['username'] == session.get("username"):
                return redirect(url_for("start"))
            else:
                return render_template('edycja.html', alert="By wprowadzić zmiany wpisz swój login")
        else:
            return render_template('edycja.html')
    else:
        return redirect(url_for("login"))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get("username") is None:
        if request.method == 'POST':
            try:
                new = add_user(request.form['username'], request.form['email'], request.form['password'])
                session['username'] = new.username
            except:
                return render_template('rejestracja.html', alert="Być może użytkownik już istnieje")
            return redirect(url_for("start"))
        else:
            return render_template('rejestracja.html')
    else:
        return redirect(url_for("start"))


@app.route("/delete")
def delete_account():
    del_user(session['username'])
    session.clear()
    return redirect(url_for("start"))


@app.route("/u", methods=['GET', 'POST'])
def get_all_firend():
    if session.get("username") is not None:
        user = User.query.filter_by(username=session.get("username")).first()
        if request.method == 'GET':
            friends = show_friend(user.id)
            return render_template('siec_uzytkownikow.html', users=friends)
        else:
            friend = User.query.filter_by(username=request.form['username']).first()
            add_friend(user.id, friend.id)
            return redirect(url_for("get_all_firend"))
    else:
        return redirect(url_for("login"))


@app.route("/u/<user_id>")
def get_firend(user_id):
    if session.get("username") is not None:
        user = User.query.filter_by(id=user_id).first()
        if user is not None:
            return render_template('kolekcja_roslin_usera.html', collection=user.plants, username=user.username)
        else:
            return "Not Found"
    else:
        return redirect(url_for("login"))


@app.route("/u/<user_id>/delete")
def delete_firend(user_id):
    if session.get("username") is not None:
        user = User.query.filter_by(username=session.get("username")).first()
        delete_friend(user.id, user_id)
        return redirect(url_for("get_all_firend"))
    else:
        return redirect(url_for("login"))
