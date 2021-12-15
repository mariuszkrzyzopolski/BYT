from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    plants = db.relationship('Plant', backref='user')

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500))
    photo = db.Column(db.String(10))
    ownership = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, description, photo):
        self.name = name
        self.description = description
        self.photo = photo