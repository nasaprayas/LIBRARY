from flask import Blueprint, render_template, request

bp = Blueprint('bp', __name__)

@bp.route('/home_page', methods=['GET','POST'])
def home_page():
    return render_template('home_page.html')

@bp.route('/login', methods=['GET','POST'])
def login():
    return render_template('log_in.html')    

@bp.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('sign_up.html')
    # elif request.method == 'POST':
