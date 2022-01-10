from main import db
from models.Plant import Plant
from models.User import User
from models.Pubplant import Pubplant


def add_pubplant_to_account(plant_id, u_name):
    owner = User.query.filter_by(username=u_name).first()
    pubplant = Pubplant.query.filter_by(id=plant_id).first()
    plant = Plant(name=pubplant.name, description=pubplant.description, photo=pubplant.photo, ownership=owner.id)
    db.session.add(plant)
    db.session.commit()


def create_privplant(name, description, photo, ownership):
    new_plant = Plant(name, description, photo, ownership)
    db.session.add(new_plant)
    db.session.commit()


def edit_privplant(plant_id, request):
    name = request.form['name']
    description = request.form['description']
    photo = request.form['photo']
    plant = Plant.query.filter_by(id=plant_id).first()
    if plant is not None:
        if name != "":
            plant.name = name
        if description != "":
            plant.description = description
        if photo != "":
            plant.photo = photo
        db.session.commit()


def remove_privplant(plant_id, owner):
    user = User.query.filter_by(username=owner).first()
    plant = Plant.query.filter_by(id=plant_id, ownership=user.id).first()
    db.session.delete(plant)
    db.session.commit()
