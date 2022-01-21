from main import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500))
    photo = db.Column(db.String(200))
    ownership = db.Column(db.Integer, db.ForeignKey('user.id'))
    sun = db.Column(db.String(50))

    def __init__(self, name, description, photo, ownership, sun):
        self.name = name
        self.description = description
        self.photo = photo
        self.ownership = ownership
        self.sun = sun