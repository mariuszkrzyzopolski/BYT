from models import User


def test_user(mocker):
    usr = User("Testowy", "pass", "w@wp.pl")

    assert usr.email == "w@wp.pl"

def test_foo(
        flask_app_mock,
        mock_get_sqlalchemy
):
    assert 1==1
