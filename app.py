from flask import url_for, render_template, request, redirect, session
from models import User, Plant
from main import app, db


@app.route("/")
def start():
    if not session['logged_in']:
        return render_template('projekt.html', url="/login", log_btn="Zaloguj")
    else:
        return render_template('projekt.html', url="/logout", log_btn="Wyloguj")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if not session['logged_in']:
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
    else:
        return redirect(url_for('logout'))


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('start'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if not session['logged_in']:
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
    else:
        session['logged_in'] = False
        return redirect(url_for("register"))


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


@app.route("/collection")
def collection():
    if session['logged_in']:
        rosliny = User.query.filter_by(username=session['username']).first().plants
        return render_template('kolekcja_roslin.html', rosliny=rosliny)
    else:
        return redirect(url_for("login"))


@app.route("/addToAccount")
def add_to_account():
    plant_id = request.args.get('plant')
    user = User.query.filter_by(username=session['username']).first()
    plant = Plant.query.filter_by(id=plant_id).first()
    plant.ownership = user.id
    db.session.commit()
    return redirect(url_for("collection"))


@app.route("/addList")
def add_list():
    rosliny = Plant.query.filter_by(ownership=None).all()
    return render_template('dodaj_z_listy.html', rosliny=rosliny)


@app.route("/addNewPlant", methods=['GET', 'POST'])
def create_plant():
    if request.method == 'GET':
        return render_template('formPlant.html')
    else:
        new_plant = Plant(
            name=request.form['name'],
            description=request.form['description'],
            photo=request.form['photo'])
        db.session.add(new_plant)
        db.session.commit()
        return redirect(url_for("collection"))


@app.route("/delete")
def delete_account():
    user = User.query.filter_by(username=session['username']).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("start"))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
