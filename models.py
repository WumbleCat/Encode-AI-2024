from . import db
from flask_login import UserMixi

class Wallet():
    def __init__(self,private_key,public_key):
        self.private_key = private_key
        self.public_key = public_key
    def get_balance(self):
        pass # Maine implement this pls

class User(db.model,UserMixi):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100),unique = True)
    password = db.Column(db.String(162))
    wallet = db.Column(Wallet)

class Transaction(db.model):
    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.Integer,db.ForeignKey("user.id"))
    receiver = db.Column(db.Integer,db.ForeignKey("user.id"))
    amount = db.Column(db.Integer)