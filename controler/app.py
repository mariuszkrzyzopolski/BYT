from flask import url_for, render_template, request, redirect, session, g
from main import app
from service.plantService import *
from service.userService import *


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
    if session.get("logged_in") is not None:
        rosliny = User.query.filter_by(username=session['username']).first().plants
        return render_template('kolekcja_roslin.html', rosliny=rosliny)
    else:
        return redirect(url_for("login"))


@app.route("/addToAccount/<plant_id>")
def add_plant_to_account(plant_id):
    add_to_account(plant_id, session.get("username"))
    return redirect(url_for("collection"))


@app.route("/remove/<plant_id>", methods=['GET', 'POST'])
def remove(plant_id):
    if session.get("logged_in") is not None:
        name = session.get('username')
        user = User.query.filter_by(username=name).first()
        plant = Plant.query.filter_by(id=plant_id, ownership=user.id).first()
        if plant is not None:
            if request.method == 'GET':
                return render_template('confirmRemove.html', roslina=plant)
            if request.method == 'POST':
                plant.ownership = None
                db.session.commit()
                return redirect(url_for("collection"))


@app.route("/addList")
def add_list():
    plants = Plant.query.filter_by(ownership=None).all()
    return render_template('dodaj_z_listy.html', rosliny=plants)


@app.route("/plant_edit/<plant_id>", methods=['GET', 'POST'])
def plant_edit(plant_id):
    if session.get("logged_in") is not None:
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            photo = request.form['photo']
            plant = Plant.query.filter_by(id=plant_id).first()
            if plant is not None:
                if name is not None:
                    plant.name = name
                if description is not None:
                    plant.description = description
                if photo is not None:
                    plant.photo = photo
                db.session.commit()
            return redirect(url_for("collection"))
        elif request.method == 'GET':
            plant = Plant.query.filter_by(id=plant_id).first()
            return render_template("editPlant.html", roslina=plant)
        else:
            return "err"
    else:
        return redirect(url_for("login"))


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
