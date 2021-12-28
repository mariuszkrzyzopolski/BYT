import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


@pytest.fixture
def flask_app_mock():
    app_mock = Flask(__name__)
    app_mock.config.from_object("config.Config")
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock


@pytest.fixture()
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock
