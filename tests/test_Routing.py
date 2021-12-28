import flask
import requests
from flask import url_for, render_template, request, redirect, session
from models import User

from app import db, app as application

'''

def test_routing_home():
    session['logged_in'] = False
    response = application.test_client().get('/')
    assert response.status_code == 200


def test_routing_login():
    post = {'loguj': 'Zaloguj', 'username': '1', 'password': '1'}
    response = application.test_client()
    assert response.post('/login', data=post).status_code == 200
    with response.session_transaction() as sess:
        assert sess['logged_in'] == True


def test_routing_logout():
    response = application.test_client().get('/')
    assert response.status_code == 200
    assert response.request.method == 'GET'


def test_routing_register():
    response = application.test_client().get('/register')
    assert response.status_code == 200


def test_routing_collection():
    response = application.test_client().get('/collection')
    assert response.status_code == 200
    
'''