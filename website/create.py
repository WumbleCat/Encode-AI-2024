import io

import qrcode
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, send_file
from werkzeug.security import generate_password_hash as hash_gen, check_password_hash as check_pass
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Wallet, Company, Product
from solathon import Keypair
from .auth import auth
create = Blueprint("Create", __name__)

@create.route('/create', methods=['POST', 'GET'])
@login_required
def create_company():
    if Company.query.filter_by(merchant_id=current_user.id).first():
        flash("You already have a company")
        return render_template("navbar.html", user=current_user)
    if request.method == "POST":
        public_key = request.form['public_key']
        name = request.form['name']
        region = request.form['region']
        user_id = current_user.id
        new_company = Company(name=name,public_key=public_key,merchant_id = user_id, region = region)
        db.session.add(new_company)
        db.session.commit()
        return render_template("navbar.html",user = current_user)
    return render_template("create.html",user = current_user)

@create.route('/add', methods=['POST', 'GET'])
@login_required
def create_product():
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        # Fetch the current user's company
        company = Company.query.filter_by(merchant_id=current_user.id).first()
        if company:
            new_product = Product(name=name, cost=price, company_id=company.id,category = category)
            db.session.add(new_product)
            db.session.commit()
            flash('Product created successfully!', category='success')
            return render_template("navbar.html", user = current_user)
        else:
            flash('You need to create a company first.', category='error')
            return redirect(url_for('Create.create_company',user = current_user))

    return render_template('add.html',user = current_user)

@create.route('/business/<id>', methods = ["GET"])
def qr(id):
    if request.method == "GET":
        url = f"https://127.0.0.1:5000/pay/{id}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to a BytesIO object
        qr_bytes_io = io.BytesIO()
        qr_image.save(qr_bytes_io, format='PNG')
        qr_bytes_io.seek(0)

        return send_file(qr_bytes_io, download_name=f"qr_{id}.png", as_attachment=True)