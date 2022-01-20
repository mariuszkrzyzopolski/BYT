from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    plants = db.relationship('Plant', backref='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
