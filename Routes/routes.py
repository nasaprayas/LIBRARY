from flask import Blueprint, render_template, request, url_for, redirect
from Controllers.controller import authenticaionController
from flask_login import login_required, current_user

bp = Blueprint('bp', __name__)

@bp.route('/home_page', methods=['GET','POST'])
def home_page():
    if current_user.is_authenticated:
        return render_template('home_page.html')
    return redirect(url_for('bp.login'))

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