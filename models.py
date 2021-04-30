from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
from app import db




class User(UserMixin,db.Model):

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index=True, unique=False)
    lastName = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    Completion = db.Column(db.Integer)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return self.id

    def get_user_name(self):
        return self.username
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))