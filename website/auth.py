from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash as hash_gen, check_password_hash as check_pass
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Wallet, Product, Company
from solathon import Keypair

auth = Blueprint("Authentication", __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        print('a')
        if user:
            if check_pass(user.password, password):
                print('b')
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return render_template("navbar.html",user = current_user)
            else:
                print('c')
                flash('Incorrect password, try again.', category='error')
        else:
            print('d')
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('Authentication.login'))

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
            new_user = User(email=email, password=hash_gen(password1))
            db.session.add(new_user)
            new_account = Keypair()
            wallet = Wallet(user_id = new_user.id,public_key = str(new_account.public_key), private_key = str(new_account.private_key))
            db.session.add(wallet)
            db.session.commit()
            login_user(new_user, remember=True)
            return render_template("navbar.html",user = current_user)
    return render_template("signup.html",user = current_user)

@auth.route('/save-transaction', methods=['POST'])
def save_transaction():
    try:
        transaction_data = request.json
        # Process and save the transaction data to your database
        print(transaction_data)  # You can print it for testing purposes
        return jsonify({'message': 'Transaction saved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@auth.route('/pay/<int:id>')
def pay(id):
    product = Product.query.filter_by(id=id).first()
    price = product.cost
    company = Company.query.filter_by(id = product.company_id).first()
    return render_template("pay.html",price = price, public_key = company.public_key)
@auth.route('/business')
@login_required
def business():
    company = Company.query.filter_by(merchant_id = current_user.id).first()
    if not company:
        return render_template("business-page.html",products = None, public_key=None, user=current_user)
    products = Product.query.filter_by(company_id = company.id).all()
    if not products:
        return render_template("business-page.html",products = None, public_key=company.public_key, user=current_user)
    return render_template("business-page.html",products = products, public_key=company.public_key, user=current_user)