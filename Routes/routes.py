from flask import Blueprint, render_template, request, url_for, redirect, jsonify
from Controllers.controller import authenticaionController, SearchController, BookController, userController, employeeController, authorController, vendorController, publisherController
from flask_login import login_required, current_user, logout_user

bp = Blueprint('bp', __name__)

@bp.route('/home_page', methods=['GET','POST'])
def home_page():
    return render_template('home_page.html', current_user=current_user)

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
    return admin

@bp.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book = BookController.add_book()
        if 'error' in book:
            return render_template('add_book.html', error=book['error'])
        return render_template('add_book.html', error='')
    return render_template('add_book.html', error='')

@bp.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        author = authorController.add_author()
        if 'error' in author:
            return render_template('add_author.html', error=author['error'])
        return render_template('add_author.html', error='')
    return render_template('add_author.html', error='')

@bp.route('/add_vendor', methods=['GET', 'POST'])
def add_vendor():
    if request.method == 'POST':
        vendor = vendorController.add_vendor()
        if 'error' in vendor:
            return render_template('add_vendor.html', error=vendor['error'])
        return render_template('add_vendor.html', error='')
    return render_template('add_vendor.html', error='')

@bp.route('/add_publisher', methods=['GET', 'POST'])
def add_publisher():
    if request.method == 'POST':
        publisher = publisherController.add_publisher()
        if 'error' in publisher:
            return render_template('add_publisher.html', error=publisher['error'])
        return render_template('add_publisher.html', error='')
    return render_template('add_publisher.html', error='')

@bp.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    return render_template('add_transaction.html')

@bp.route('/update_book', methods=['GET', 'POST'])
def update_book():
    if request.method == 'POST':
        book = BookController.update_book()
        if 'error' in book:
            return render_template('update_book.html', error=book['error'])
        return render_template('update_book.html', error='')
    return render_template('update_book.html', error='')

@bp.route('/update_author', methods=['GET', 'POST'])
def update_author():
    if request.method == 'POST':
        author = authorController.update_author()
        if 'error' in author:
            return render_template('update_author.html', error=author['error'])
        return render_template('update_author.html', error='')
    return render_template('update_author.html', error='')

@bp.route('/update_vendor', methods=['GET', 'POST'])
def update_vendor():
    if request.method == 'POST':
        vendor = vendorController.update_vendor()
        if 'error' in vendor:
            return render_template('update_vendor.html', error=vendor['error'])
        return render_template('update_vendor.html', error='')
    return render_template('update_vendor.html', error='')

@bp.route('/update_publisher', methods=['GET', 'POST'])
def update_publisher():
    if request.method == 'POST':
        publisher = publisherController.update_publisher()
        if 'error' in publisher:
            return render_template('update_publisher.html', error=publisher['error'])
        return render_template('update_publisher.html', error='')
    return render_template('update_publisher.html', error='')

@bp.route('/update_transaction', methods=['GET', 'POST'])
def update_transaction():
    return render_template('update_transaction.html')

@bp.route('/delete_book', methods=['GET', 'POST'])
def delete_book():
    if request.method == 'POST':
        book = BookController.delete_book()
        if 'error' in book:
            return render_template('delete_book.html', error=book['error'])
        return render_template('delete_book.html', error='')
    return render_template('delete_book.html', error='')

@bp.route('/delete_author', methods=['GET', 'POST'])
def delete_author():
    if request.method == 'POST':
        author = authorController.delete_author()
        if 'error' in author:
            return render_template('delete_author.html', error=author['error'])
        return render_template('delete_author.html', error='')
    return render_template('delete_author.html', error='')

@bp.route('/delete_vendor', methods=['GET', 'POST'])
def delete_vendor():
    if request.method == 'POST':
        vendor = vendorController.delete_vendor()
        if 'error' in vendor:
            return render_template('delete_vendor.html', error=vendor['error'])
        return render_template('delete_vendor.html', error='')
    return render_template('delete_vendor.html', error='')

@bp.route('/delete_publisher', methods=['GET', 'POST'])
def delete_publisher():
    if request.method == 'POST':
        publisher = publisherController.delete_publisher()
        if 'error' in publisher:
            return render_template('delete_publisher.html', error=publisher['error'])
        return render_template('delete_publisher.html', error='')
    return render_template('delete_publisher.html', error='')

@bp.route('/book_search', methods=['GET'])
def search_book():
    search = request.args.get('search').lower()
    results = SearchController.search_book(search)
    return jsonify(results)

@bp.route('/book/<int:book_id>', methods=['GET'])
def book_view(book_id):
    book = BookController.book_view(book_id)
    return render_template('book_view.html', book=book)

@bp.route('/view_history', methods=['GET'])
def view_history():
    return render_template('view_history.html')

@bp.route('/view_all_members', methods=['GET'])
def view_all_members():
    list = userController.get_users()
    return render_template('all_members.html', members=list)

@bp.route('/view_location', methods=['GET'])
def view_location():
    return render_template('view_location.html')