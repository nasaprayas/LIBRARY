from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from Controllers.controller import authenticaionController, SearchController, BookController, userController, employeeController
from flask_login import login_required, current_user, logout_user

bp = Blueprint('bp', __name__)

@bp.route('/home_page', methods=['GET','POST'])
def home_page():
    return render_template('home_page.html')

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = authenticaionController.login()
        if 'error' in user:
            return render_template('log_in.html', error=user['error'])
        return redirect(url_for('bp.home_page'))
    return render_template('log_in.html', error=' ')

@bp.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        new_user=authenticaionController.signup()
        if new_user:
            return redirect(url_for('bp.login'))
        return render_template('sign_up.html', error='Try Again!!!')
    return render_template('sign_up.html', error=' ')

@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('bp.login'))

@bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        userController.update_user()
    return render_template('dashboard.html', pfp=current_user.profile_pic)

@bp.route('/add/admin', methods=['POST'])
def add_empoyee():
    admin = employeeController.add_employee()
    return

@bp.route('/add_book', methods=['GET', 'POST'])
def add_book():
    return render_template('add_book.html')

@bp.route('/add_author', methods=['GET', 'POST'])
def add_author():
    return render_template('add_author.html')

@bp.route('/add_vendor', methods=['GET', 'POST'])
def add_vendor():
    return render_template('add_vendor.html')

@bp.route('/add_publisher', methods=['GET', 'POST'])
def add_publisher():
    return render_template('add_publisher.html')

@bp.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    return render_template('add_transaction.html')