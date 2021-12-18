from main import db
from model.user import User


def add_user(u_name,u_email,u_pass):
    new_user = User(
        username=u_name,
        email=u_email,
        password=u_pass)
    db.session.add(new_user)
    db.session.commit()
    return new_user

#def delete_user():

#def edit_user():