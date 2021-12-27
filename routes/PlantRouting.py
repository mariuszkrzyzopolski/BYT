from flask import url_for, render_template, request, redirect, session

from main import app
from controllers.PlantController import *
from controllers.UserController import *


@app.route("/collection")
def collection():
    if session.get("logged_in") is not None:
        rosliny = User.query.filter_by(username=session['username']).first().plants
        return render_template('kolekcja_roslin.html', rosliny=rosliny)
    else:
        return redirect(url_for("login"))


@app.route("/addList")
def add_list():
    plants = Plant.query.filter_by(ownership=None).all()
    return render_template('dodaj_z_listy.html', rosliny=plants)


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


@app.route("/addToAccount/<plant_id>")
def add_plant_to_account(plant_id):
    add_to_account(plant_id, session.get("username"))
    return redirect(url_for("collection"))


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
