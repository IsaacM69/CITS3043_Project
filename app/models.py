from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
##from app import login
from hashlib import md5
from app import db




class User(UserMixin,db.Model):

    id = db.Column(db.Integer, primary_key=True)

    firstName = db.Column(db.String(64), index=True, unique=False)
    lastName = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    Scores = db.relationship('post', backref = 'user', lazy = 'dynamic')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.firstName)

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.firstName

class Sores(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)

    score_ID = db.Column(db.Integer, db.ForeignKey('user.id')) 
    Mod_1 = db.Column(db.Integer, index=True, unique=False)
    Mod_2 = db.Column(db.Integer, index=True, unique=False)
    Mod_3 = db.Column(db.Integer, index=True, unique=False)
    finalScore = db.Column(db.Integer, index=True, unique=False)
    totalScore = db.Column(db.Integer, index=True, unique=False)