from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth import auth

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "I AM GONNA CHANGE IT"
    app.config['SQLALCHEMY_DATABASE_URI'] = "database.db"
    db.init_app()
    with app.app_context():
        db.create_all()
    create_database(app)
    app.register_blueprint(auth,url_prefix = '/')


def create_database(app):
    if not path.exists("database.db"):
        db.create_all(app=app)