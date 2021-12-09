from app import app as application


def test_user():
    response = application.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b"<p>Hello, World!</p>"
