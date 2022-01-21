from main import db
from models.Friendship import Friendship
from models.User import User


def add_friend(my_id, friend_id):
    if Friendship.query.filter_by(user1=my_id, user2=friend_id).first() is None:
        new_friendship = Friendship(
            user1=my_id,
            user2=friend_id
        )
        db.session.add(new_friendship)
        db.session.commit()
        return new_friendship
    

def show_friend(my_id):
    friends = []
    friendships = Friendship.query.filter_by(user1=my_id).all()
    for x in friendships:
        next_friend = User.query.filter_by(id=x.user2).first()
        friends.append(next_friend)
    return friends


def delete_friend(my_id, friend_id):
    friendship = Friendship.query.filter_by(user1=my_id, user2=friend_id).first()
    db.session.delete(friendship)
    db.session.commit()
