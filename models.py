from . import db
from flask_login import UserMixi

class user(db.model,UserMixi):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100),unique = True)