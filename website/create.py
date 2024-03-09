from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash as hash_gen, check_password_hash as check_pass
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Wallet, Company, Product
from solathon import Keypair

create = Blueprint("Create", __name__)

@create.route('/create', methods=['POST', 'GET'])
@login_required
def create_company():
    if request.method == "POST":
        public_key = request.form['public_key']
        name = request.form['name']
        user_id = current_user.id
        new_company = Company(name=name,public_key=public_key,merchant_id = user_id)
        db.session.add(new_company)
        db.session.commit()

    return render_template("create.html",user = current_user)

@create.route('/add', methods=['POST', 'GET'])
@login_required
def create_product():
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        # Fetch the current user's company
        company = Company.query.filter_by(merchant_id=current_user.id).first()
        if company:
            new_product = Product(name=name, cost=price, company_id=company.id)
            db.session.add(new_product)
            db.session.commit()
            flash('Product created successfully!', category='success')
        else:
            flash('You need to create a company first.', category='error')

    return render_template('add.html',user = current_user)