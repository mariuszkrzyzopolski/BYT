from models import Plant
from models import Pubplant
from models import User
from controllers.PlantController import *

'''
def test_add_pubplant_to_account(mocker):
    mocker.patch('controllers.PlantController.db')
    usr = User("username", "email", "pass")
    mocker.patch('controllers.UserController.User', usr)
    pubplant = Pubplant("name", "description", "photo")
    pubplant.id = 1
    mocker.patch('controllers.PlantController.Pubplant', pubplant)
    plant = Plant(pubplant.name, pubplant.description, pubplant.photo, usr.id)
    mocker.patch('controllers.PlantController.Plant', plant)
    add_pubplant_to_account(pubplant.id, usr.username)
    assert usr.id == plant.ownership
'''
