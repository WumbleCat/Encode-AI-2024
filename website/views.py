from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("navbar.html", user=current_user)

@views.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html", user=current_user)
