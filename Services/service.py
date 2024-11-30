import os
from flask import request, Flask
from utils.utils import db
from Models.member_model import Members
from Models.book_model import Books
from Models.author_model import Authors
from Models.publisher_model import Publishers
from Models.employee_model import Employees
from Models.author_model import Authors
from Models.vendor_model import Vendors

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user
from config import config


class userService:
    def get_member_by_mail(mail):
        return Members.query.filter_by(mail=mail).first()

    def get_employee_by_mail(mail):
        return Employees.query.filter_by(mail=mail).first()

    @staticmethod
    def sign_up(name, password, dob, mail):
        new_member = Members(name=name, password_hash=generate_password_hash(
            password), date_of_birth=dob, mail=mail)
        db.session.add(new_member)
        db.session.commit()
        return new_member

    @staticmethod
    def log_in(mail, password, type):
        user = None
        if type == 'member':
            user = userService.get_member_by_mail(mail)
            if not user:
                return {'error': 'member not found'}
        elif type == 'admin':
            user = userService.get_employee_by_mail(mail)
            if not user:
                return {'error': 'admin not found'}
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            if current_user.is_authenticated:
                return user.to_dict()
            return {'error': 'not authenticated'}
        return {'error': 'incorrect password'}

    @staticmethod
    def update_user(pfp, name, dob, gender, country, state, city, street):
        current_user.profile_pic = pfp
        current_user.name = name
        current_user.date_of_birth = dob
        current_user.gender = gender
        current_user.country = country
        current_user.state = state
        current_user.city = city
        current_user.street = street
        db.session.commit()
        return current_user

    @staticmethod
    def upload_profile_pic(file):
        filename = secure_filename(file.filename)
        file.save(os.path.join(config.PROFILE_UPLOAD_FOLDER, filename))

    @staticmethod
    def is_allowed(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.ALLOWED_FORMATS
    
    @staticmethod
    def get_all_members():
        return Members.query.all()

class employeeService:
    @staticmethod
    def create_employee(data):
        new_employee = Employees(
            name=data.get('name'),
            mail=data.get('mail'),
            date_of_birth=data.get('dob'),
            password_hash=generate_password_hash(data.get('password')),
        )
        db.session.add(new_employee)
        db.session.commit()
        return new_employee

class authorService:
    @staticmethod
    def add_author(data):
        new_author = Authors(
            name=data.get('name'),
            dob=data.get('dob'),
            origin=data.get('origin'),
            about=data.get('about')
        )
        db.session.add(new_author)
        db.session.commit()
        return new_author
    
    @staticmethod
    def get_author_by_name(name):
        return Authors.query.filter_by(name=name).first()
    
    @staticmethod
    def modify_author(author, data):
        author.dob=data.get('dob'),
        author.origin=data.get('origin'),
        author.about=data.get('about')
        db.session.commit()
        return author
    
    @staticmethod
    def remove_author(author):
        db.session.delete(author)
        db.session.commit()
        return author

class vendorService:
    @staticmethod
    def add_vendor(data):
        new_vendor = Vendors(
            name=data.get('name'),
            address=data.get('address'),
            about=data.get('about')
        )
        db.session.add(new_vendor)
        db.session.commit()
        return new_vendor
    
    @staticmethod
    def get_vendor_by_name(name):
        return Vendors.query.filter_by(name=name).first()
    
    @staticmethod
    def modify_vendor(vendor, data):
        vendor.name=data.get('name'),
        vendor.address=data.get('address'),
        vendor.about=data.get('about')
        db.session.commit()
        return vendor
    
    @staticmethod
    def remove_vendor(vendor):
        db.session.delete(vendor)
        db.session.commit()
        return vendor
    
class publisherService:
    @staticmethod
    def add_publisher(data):
        new_publisher = Publishers(
            name=data.get('name'),
            address=data.get('address'),
            about=data.get('about')
        )
        db.session.add(new_publisher)
        db.session.commit()
        return new_publisher
    
    @staticmethod
    def get_publisher_by_name(name):
        return Publishers.query.filter_by(name=name).first()
    
    @staticmethod
    def modify_publisher(publisher, data):
        publisher.name=data.get('name'),
        publisher.address=data.get('address'),
        publisher.about=data.get('about')
        db.session.commit()
        return publisher
    
    @staticmethod
    def remove_publisher(publisher):
        db.session.delete(publisher)
        db.session.commit()
        return publisher

class SearchService:
    def get_books_by_name_partial(book_title):
        books = Books.query.filter(Books.title.ilike(f"%{book_title}%")).all()
        return [book.to_dict() for book in books] if books else []
    
class BookService:
    def add_book(data, cover_page):
        new_book = Books(
            title=data.get('title'),
            preface=data.get('preface'),
            author_id=authorService.get_author_by_name(data.get('author_name')).id,
            publisher_id=publisherService.get_publisher_by_name(data.get('publisher_name')).id,
            vendor_id=vendorService.get_vendor_by_name(data.get('vendor_name')).id,
            shelf_id=data.get('shelf_id'),
            language=data.get('language'),
            subject=data.get('subject'),
            category=data.get('category'),
            genre=data.get('genre'),
            price=data.get('price'),
            availability=data.get('availability'),
            date_of_publishing=data.get('date_of_publishing'),
            shelf_date=data.get('shelf_date'),
            bought_on=data.get('bought_on'),
            cover_page=cover_page
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book
    
    @staticmethod
    def get_book_by_title(title):
        return Books.query.filter_by(title=title).first()
    
    @staticmethod
    def upload_book_cover(file):
        filename = secure_filename(file.filename)
        file.save(os.path.join(config.COVER_UPLOAD_FOLDER, filename))

    @staticmethod
    def is_allowed(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.ALLOWED_FORMATS
    
    @staticmethod
    def update_book(book, data):
        book.title=data.get('title')
        book.preface=data.get('preface')
        book.publisher_id=publisherService.get_publisher_by_name(data.get('publisher_name')).id
        book.vendor_id=vendorService.get_vendor_by_name(data.get('vendor_name')).id,
        book.shelf_id=data.get('shelf_id')
        book.price=data.get('price')
        book.availability=data.get('availability')
        book.date_of_publishing=data.get('date_of_publishing')
        book.shelf_date=data.get('shelf_date')
        book.bought_on=data.get('bought_on')
        db.session.commit()
        return book
    
    @staticmethod
    def remove_book(book):
        db.session.delete(book)
        db.session.commit()
        return book
    
    @staticmethod
    def get_book_by_id(book_id):
        book = Books.query.filter_by(id=book_id).first()
        return book.to_dict()
    
