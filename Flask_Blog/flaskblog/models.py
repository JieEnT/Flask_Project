from datetime import datetime
from flaskblog import db, login_manager
#login_manager requires User to have certain attributes such as isAuthenticated, isActive, isAnonymous, getId
#Class adds these attributes
from flask_login import UserMixin

#To get the user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # How the user is supposed to look like when it is being printed out
    # e.g.

    # class Person:
    #     def __init__(self, first_name, last_name, age):
    #         self.first_name = first_name
    #         self.last_name = last_name
    #         self.age = age
    # def __repr__(self):
    #     return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    # person = Person("John", "Doe", 25)
    # print(repr(person))
    # Output: Person("John", "Doe", 25)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
