from os import path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.app_context().push()
    app.config['SECRET_KEY'] = "I AM GONNA CHANGE IT"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .create import create

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(create, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'Authentication.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from .models import Company, Product, User, Transaction, Wallet

    with app.app_context():
        db.create_all()

    return app


def create_database():
    db.create_all()
