from . import db ,login_manager
from datetime import datetime
from flask_login import UserMixin, current_user #UserMixin helps in configuration of models by implementing the four configuration methods
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True,index=True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255), nullable=False)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     
    @property #creates a write only class property password
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def set_password(self, password):
        self.pass_secure= generate_password_hash(password)#passing the hash passowrd as a value to pass_secure
       

    def verify_password(self, password):  #takes in a password ,hashes it and compares it to the hashed password to check if they are the same
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User: {self.username}'

    @login_manager.user_loader #call back function that retrieves a user when a unique identifier is passed
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    
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