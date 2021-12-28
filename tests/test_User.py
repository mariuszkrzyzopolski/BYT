from models import User
from controllers.UserController import *
from flask import session


def test_adduser(mocker):
    mocker.patch('controllers.UserController.db')
    usr = User("Testowy", "w@wp.pl", "pass")
    usr2 = add_user(usr.username, usr.email, usr.password)
    assert usr.username == usr2.username
    assert usr.password == usr2.password
    assert usr.email == usr2.email


def test_edituser(mocker):
    mocker.patch('controllers.UserController.db')
    usr = User("Testowy", "w@wp.pl", "pass")
    assert session['username'] == usr.username
    usr = edit_user(usr.username, "newemail", "newpass")
    assert usr.email == "newemail"
    assert usr.password == "newpass"


def test_deluser(mocker):
    mocker.patch('controllers.UserController.db')
    usr = User("Testowy", "w@wp.pl", "pass")
    assert session['username'] == usr.username
    usr = del_user(usr.username)
    assert usr.username is None
    assert usr.password is None
    assert usr.email is None

