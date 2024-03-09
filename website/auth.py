from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash as hash_gen, check_password_hash as check_pass
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Wallet

auth = Blueprint("Authentication", __name__)

@auth.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_pass(user.password,password):
                flash('Logged in successfully!', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html")

@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        else:
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            ismerchant = request.form.get('ismerchant')
            if ismerchant == '0':
                new_user = User(email=email, password=hash_gen(
                password1), ismerchant = False)
            else:
                new_user = User(email=email, password=hash_gen(
                    password1), ismerchant = True)
            db.session.add(new_user)

            wallet = Wallet(user_id = new_user.id,)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")
