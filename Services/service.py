from flask import request, Flask
from utils.utils import db
from Models.member_model import Members
from Models.book_model import Books
from Models.author_model import Authors
from Models.publisher_model import Publishers
from Models.employee_model import Employees
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user


class userService:
    def get_member_by_mail(mail):
        return Members.query.filter_by(mail=mail).first()
    
    def get_employee_by_mail(mail):
        return Employees.query.filter_by(mail=mail).first()

    @staticmethod
    def sign_up(name, password, dob, mail):
        new_member = Members(name=name, password_hash=generate_password_hash(password), date_of_birth=dob, mail=mail)
        db.session.add(new_member)
        db.session.commit()
        return new_member
    
    @staticmethod
    def log_in(mail, password, type):
        if type == 'member':
            user = userService.get_member_by_mail(mail)
            if not user:
                return {'error': 'member not found'}
        else:
            user = userService.get_employee_by_mail(mail)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            if current_user.is_authenticated:
                return user.to_dict()
            return {'error': 'not authenticated'}    
        return {'error': 'incorrect password'}
    
    
class SearchService:
    def get_books_by_name_partial(book_title):
        books = Books.query.filter(Books.name.ilike(f"%{book_title}%")).all()
        return [book.to_dict() for book in books] if books else []
    
class BookService:
    def add_book(data):
        new_book = Books(
            book_id=data.get('book_id'),
            author_id=data.get('author_id'),
            book_title=data.get('book_title'),
            publisher_id=data.get('publisher_id'),
            vendor_id=data.get('vendor_id'),
            shelf_id=data.get('shelf_id'),
            category=data.get('category'),
            price=data.get('price'),
            language_name=data.get('language_name'),
            subject_name=data.get('subject_name'),
            genre=data.get('genre'),
            date_of_publishing=data.get('date_of_publishing'),
            date_of_addition=data.get('date_of_addition'),
            availability=data.get('availability'),
            shelf_date=data.get('shelf_date'),
            bought_on=data.get('bought_on'),
            cover_page =request.form.get('cover_page')
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book

    

    
