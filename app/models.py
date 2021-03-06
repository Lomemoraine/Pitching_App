from . import db ,login_manager
from datetime import datetime
from flask_login import UserMixin, current_user #UserMixin helps in configuration of models by implementing the four configuration methods
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')
   
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     
    @property #creates a write only class property password
    def password(self):
        raise AttributeError('You cannot read the password attribute')
#takes in a password ,hashes it and compares it to the hashed password to check if they are the same
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)#passing the hash passowrd as a value to pass_secure
       

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

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
    pitch = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    category = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    up_vote = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    down_vote = db.relationship('Downvote', backref='pitch', lazy='dynamic')
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Pitch Title: {self.title}"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
    comment = db.Column(db.Text())
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch_id):
        comments = Comment.query.filter_by(pitch_id= pitch_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'
    
class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        

    # def like(cls, id):
    #     upvote_pitch = Upvote(user=current_user, pitch_id=id)
    #     upvote_pitch.save()

    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote
    
    # @classmethod
    # def all_upvotes(cls):
    #     upvotes = Upvote.query.order_by('id').all()
    #     return upvotes
    
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
    
class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    # def dislike(cls, id):
    #     downvote_pitch = Downvote(user=current_user, pitch_id=id)
    #     downvote_pitch.save()
        
    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote
    
    # @classmethod
    # # def all_downvotes(cls):
    # #     downvotes = Downvote.query.order_by('id').all()
    # #     return downvotes
    
    
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
    
