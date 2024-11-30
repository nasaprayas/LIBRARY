from flask import request
from Services.service import userService, SearchService, BookService, employeeService, authorService, vendorService, publisherService
from flask import Blueprint, jsonify, request
from Views.view import View
from werkzeug.utils import secure_filename
from flask_login import current_user

class authenticaionController:
    @staticmethod
    def signup():
        full_name=request.form.get('full_name')
        password=request.form.get('password')
        dob=request.form.get('dob')
        email=request.form.get('email')
        new_member = userService.get_member_by_mail(email)
        if not new_member:
            new_user = userService.sign_up(name=full_name,password=password,dob=dob,mail=email)
            return new_user
        else:
            return {'error': 'Admin already exists'}
    
    @staticmethod
    def login():
        mail = request.form.get('email')
        password = request.form.get('password')
        type = request.form.get('type')
        result = userService.log_in(mail=mail, password=password,type=type)
        return result
    
class SearchController:
    @staticmethod
    def search_book(book):
        return SearchService.get_books_by_name_partial(book)
    
class BookController:
    @staticmethod
    def add_book():
        data = request.form
        file = request.files['cover_page']
        if not file.filename:
            cover = None
        elif not BookService.is_allowed(file.filename):
            return {'error': 'file type not compatible, upload gif, jpg, jpeg or png'}
        else:
            cover = secure_filename(file.filename)
            BookService.upload_book_cover(file=file)
        new_book = BookService.get_book_by_title(data.get('title'))
        if not new_book:
            new_book = BookService.add_book(data, cover)
            return new_book.to_dict()
        else:
            return {'error': 'Book already exists'}
        
    @staticmethod
    def update_book():
        data = request.form
        book = BookService.get_book_by_title(data.get('title'))
        if not book:
            return {'error': 'No book of this title'}
        else:
            book = BookService.update_book(book, data)
            return book.to_dict()
        
    @staticmethod
    def delete_book():
        data = request.form
        book = BookService.get_book_by_title(data.get('title'))
        if not book:
            return {'error': 'No book of this title'}
        else:
            book = BookService.remove_book(book)
            return book.to_dict()
        
    @staticmethod
    def book_view(book_id):
        return BookService.get_book_by_id(book_id)

class userController:
    @staticmethod
    def update_user():
        data = request.form
        file = request.files['profile_pic']
        if not file.filename:
            pfp = current_user.profile_pic
        elif not userService.is_allowed(file.filename):
            return {'error': 'file type not compatible, upload gif, jpg, jpeg or png'}
        else:
            pfp = secure_filename(file.filename)
            userService.upload_profile_pic(file)
        updated_user = userService.update_user(pfp=pfp,
                                               name=data['name'],
                                               dob=data['dob'],
                                               gender=data['gender'],
                                               country=data['country'],
                                               state=data['state'],
                                               city=data['city'],
                                               street=data['street'])
        return updated_user
    
    @staticmethod
    def get_users():
        users = userService.get_all_members()
        user_list = [user.to_dict() for user in users]
        return user_list
    
class employeeController:
    @staticmethod
    def add_employee():
        data = request.form
        new_employee = userService.get_employee_by_mail(data.get('mail'))
        if not new_employee:
            new_employee = employeeService.create_employee(data)
            return new_employee.to_dict()
        else:
            return {'error': 'Admin already exists'}
        
class authorController:
    @staticmethod
    def add_author():
        data = request.form
        new_author = authorService.get_author_by_name(data.get('name'))
        if not new_author:
            new_author = authorService.add_author(data)
            return new_author.to_dict()
        else:
            return {'error': 'Author already exists'}
        
    @staticmethod
    def update_author():
        data = request.form
        author = authorService.get_author_by_name(data.get('name'))
        if not author:
            return {'error': 'No author of this name'}
        else:
            author = authorService.modify_author(author, data)
            return author.to_dict()
        
    @staticmethod
    def delete_author():
        data = request.form
        author = authorService.get_author_by_name(data.get('name'))
        if not author:
            return {'error': 'No author of this name'}
        else:
            author = authorService.remove_author(author)
            return author.to_dict()

class vendorController:
    @staticmethod
    def add_vendor():
        data = request.form
        new_vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not new_vendor:
            new_vendor = vendorService.add_vendor(data)
            return new_vendor.to_dict()
        else:
            return {'error': 'Vendor already exists'}
        
    @staticmethod
    def update_vendor():
        data = request.form
        vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not vendor:
            return {'error': 'No vendor of this name'}
        else:
            vendor = vendorService.modify_vendor(vendor, data)
            return vendor.to_dict()
        
    @staticmethod
    def delete_vendor():
        data = request.form
        vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not vendor:
            return {'error': 'No vendor of this name'}
        else:
            vendor = vendorService.remove_vendor(vendor)
            return vendor.to_dict()

class publisherController:
    @staticmethod
    def add_publisher():
        data = request.form
        new_publisher = publisherService.get_publisher_by_name(data.get('name'))
        if not new_publisher:
            new_publisher = publisherService.add_publisher(data)
            return new_publisher.to_dict()
        else:
            return {'error': 'Publisher already exists'}
        
    @staticmethod
    def update_publisher():
        data = request.form
        publisher = publisherService.get_publisher_by_name(data.get('name'))
        if not publisher:
            return {'error': 'No publisher of this name'}
        else:
            publisher = publisherService.modify_publisher(publisher, data)
            return publisher.to_dict()
        
    @staticmethod
    def delete_publisher():
        data = request.form
        publisher = publisherService.get_publisher_by_name(data.get('name'))
        if not publisher:
            return {'error': 'No publisher of this name'}
        else:
            publisher = publisherService.remove_publisher(publisher)
            return publisher.to_dict()