from main import db


class Pubplant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500))
    photo = db.Column(db.String(200))
    sun = db.Column(db.String(50))

    def __init__(self, name, description, photo, sun):
        self.name = name
        self.description = description
        self.photo = photo
        self.sun = sun