from flask import url_for, render_template, request, redirect, session

from main import app
from controllers.PlantController import *
from controllers.UserController import *


@app.route("/collection")
def collection():
    if session.get("username") is not None:
        rosliny = User.query.filter_by(username=session['username']).first().plants
        return render_template('kolekcja_roslin.html', rosliny=rosliny)
    else:
        return redirect(url_for("login"))


@app.route("/addList")
def add_from_list():
    if session.get("username") is not None:
        plants = Pubplant.query.filter_by().all()
        return render_template('dodaj_z_listy.html', rosliny=plants)
    else:
        return redirect(url_for("login"))


@app.route("/addNewPlant", methods=['GET', 'POST'])
def create_plant():
    if session.get("username") is not None:
        if request.method == 'GET':
            return render_template('formPlant.html')
        else:
            create_privplant(
                request.form['name'],
                request.form['description'],
                request.form['photo'],
                User.query.filter_by(username=session.get("username")).first().id,
                request.form['sun'])
            return redirect(url_for("collection"))
    else:
        return redirect(url_for("login"))


@app.route("/addToAccount/<pubplant_id>")
def add_to_account(pubplant_id):
    if session.get("username") is not None:
        add_pubplant_to_account(pubplant_id, session.get("username"))
        return redirect(url_for("collection"))
    else:
        return redirect(url_for("login"))


@app.route("/plant_edit/<plant_id>", methods=['GET', 'POST'])
def plant_edit(plant_id):
    if session.get("username") is not None:
        if request.method == 'POST':
            edit_privplant(plant_id, request)
            return redirect(url_for("collection"))
        else:
            plant = Plant.query.filter_by(id=plant_id).first()
            return render_template("editPlant.html", roslina=plant)
    else:
        return redirect(url_for("login"))


@app.route("/remove/<plant_id>", methods=['GET', 'POST'])
def remove(plant_id):
    if session.get("username") is not None:
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
