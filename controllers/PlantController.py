from main import db
from models.Plant import Plant
from models.User import User


def add_plant_to_account(plant_id, u_name):
    user = User.query.filter_by(username=u_name).first()
    plant = Plant.query.filter_by(id=plant_id).first()
    plant.ownership = user.id
    db.session.commit()