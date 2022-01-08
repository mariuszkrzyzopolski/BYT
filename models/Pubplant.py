from main import db


class Pubplant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500))
    photo = db.Column(db.String(200))

    def __init__(self, name, description, photo):
        self.name = name
        self.description = description
        self.photo = photo