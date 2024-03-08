from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash as hash_gen, check_password_hash as check_pass
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("Authentication", __name__)

@auth.route('/login',methods = ['POST'])
def login():
    pass

@auth.route('/signout')
@login_required
def signout():
    pass

@auth.route('/signup')
def signup():
    pass
