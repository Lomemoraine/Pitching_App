from . import db
from datetime import datetime
from flask_login import UserMixin, current_user
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    

    def __repr__(self):
        return f'User {self.username}'
    
# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")


    # def __repr__(self):
    #     return f'User {self.name}'
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    post = db.Column(db.String, nullable=False)
    comment = db.relationship('Comment', backref='post', lazy='dynamic')
    category = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    up_vote = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    down_vote = db.relationship('Downvote', backref='pitch', lazy='dynamic')