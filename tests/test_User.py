from app import app as application
from models import User


def test_user():
    usr = User("Testowy", "pass", "w@wp.pl")
    print(usr.id)
    assert usr.email == "w@wp.pl"
