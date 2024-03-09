from . import db
from flask_login import UserMixin


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    public_key = db.Column(db.String(216), unique=True)
    merchant_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    cost = db.Column(db.Integer)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(162))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey("user.id"))
    receiver = db.Column(db.Integer, db.ForeignKey("user.id"))
    amount = db.Column(db.Integer)


class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    public_key = db.Column(db.String(216), unique=True)
    private_key = db.Column(db.String(256), unique=True)