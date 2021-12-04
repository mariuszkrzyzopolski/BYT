from flask import url_for, render_template, request, redirect, session
from models import User
from main import app, db


@app.route("/")
def start():
    return render_template('projekt.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('logowanie.html')
    else:
        if request.form['loguj'] == "Zaloguj":
            name = request.form['username']
            password = request.form['password']
            data = User.query.filter_by(username=name, password=password).first()
            if data is not None:
                session['logged_in'] = True
                session['username'] = name
                return redirect(url_for("start"))
            else:
                return "404 User Not Found"


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('rejestracja.html')
    else:
        new_user = User(
            username=request.form['username'],
            email=request.form['email'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        session['username'] = request.form['username']
        return redirect(url_for("start"))


@app.route("/account_edit", methods=['GET', 'POST'])
def edit_account():
    name = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=name).first()
    if user is not None:
        if password is not None:
            user.password = password
        db.session.commit()
        return redirect(url_for("start"))
    else:
        return "User don't exists"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
