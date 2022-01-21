from main import db


class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1 = db.Column(db.Integer, db.ForeignKey('user.id'))
    user2 = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
