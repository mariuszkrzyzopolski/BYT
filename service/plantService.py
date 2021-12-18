from main import db
from model.plant import Plant
from model.user import User


def add_to_account(plant_id, u_name):
    user = User.query.filter_by(username=u_name).first()
    plant = Plant.query.filter_by(id=plant_id).first()
    plant.ownership = user.id
    db.session.commit()