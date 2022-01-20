from models import User
from controllers.UserController import *


def test_adduser(mocker):
    mocker.patch('controllers.UserController.db')
    usr = User("Testowy", "w@wp.pl", "pass")
    usr2 = add_user(usr.username, usr.email, usr.password)
    assert usr.username == usr2.username
    assert usr.password == usr2.password
    assert usr.email == usr2.email


def test_edituserA(mocker):
    mocker.patch('controllers.UserController.db')
    usrA = User("Testowy", "w@wp.pl", "pass")
    mocker.patch('controllers.UserController.User', usrA)
    usrA = edit_user(usrA.username, "newemail", "newpass")
    assert usrA.email == "newemail"
    assert usrA.password == "newpass"

'''
def test_edituserB(mocker):
    mocker.patch('controllers.UserController.db')
    usrB = User("Testowy", "w@wp.pl", "pass")
    mocker.patch('controllers.UserController.User', usrB)
    usrB = edit_user(usrB.username, "newemail", None)
    assert usrB.email == "newemail"
    assert usrB.password == "pass"

def test_edituserC(mocker):
    mocker.patch('controllers.UserController.db')
    usr = User("Testowy", "w@wp.pl", "pass")
    mocker.patch('controllers.UserController.User', usr)
    usr = edit_user(usr.username, None, "newPass")
    assert usr.email == "w@wp.pl"
    assert usr.password == "newPass"
'''
