from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    photo = db.Column(db.String(10))
    ownership = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, description, photo, ownership):
        self.description = description
        self.photo = photo
        self.ownership = ownership
