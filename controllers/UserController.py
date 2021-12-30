from main import db
from models.User import User


def add_user(u_name, u_email, u_pass):
    new_user = User(
        username=u_name,
        email=u_email,
        password=u_pass)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def del_user(username):
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()


def edit_user(u_name, u_email, u_pass):
    new_user = User.query.filter_by(username=u_name).first()
    if new_user is not None:
        if u_email is not None:
            new_user.email = u_email
        if u_pass is not None:
            new_user.password = u_pass
        db.session.commit()
        return new_user
    else:
        return None
