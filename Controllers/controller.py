from flask import request
from Services.service import userService, SearchService, BookService
from flask import Blueprint, jsonify, request
from Views.view import View, employeeService, authorService, vendorService
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
        type = request.form.get('user_type')
        result = userService.log_in(mail=mail, password=password,type=type)
        return result
    
class SearchController:
    @staticmethod
    def search_book(book):
        found = SearchService.get_books_by_name_partial(book)
        if not found: 
            return View.render_error('Sorry, Book not found'), 404
        return View.render_book(found), 200
    
class BookController:
    @staticmethod
    def add_book():
        data = request.json
        new_book = BookService.add_book(data)
        return jsonify(new_book.to_dict()), 201     

class userController:
    @staticmethod
    def update_user():
        data = request.form
        file = request.files['profile_pic']
        if not file.filename:
            pfp = current_user.profile_pic
        elif not userService.is_allowed(file.filename):
            return {'error': 'file type not compatible, upload gif, jpg or jpeg'}
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
    
class employeeController:
    @staticmethod
    def add_employee():
        data = request.form
        new_employee = userService.get_employee_by_mail(data.get('mail'))
        if not new_employee:
            new_employee = employeeService.create_employee(data)
            return new_employee
        else:
            return {'error': 'Admin already exists'}
        
class authorController:
    @staticmethod
    def add_author():
        data = request.form
        new_author = authorService.get_author_by_name(data.get('name'))
        if not new_author:
            new_author = authorService.add_author(data)
            return new_author
        else:
            return {'error': 'Author already exists'}
        
    @staticmethod
    def update_author():
        data = request.form
        author = authorService.get_author_by_name(data.get('name'))
        if not author:
            return {'error': 'No author of this name'}
        else:
            author = authorService.modify_author(data)
            return author
        
    @staticmethod
    def delete_author():
        data = request.form
        author = authorService.get_author_by_name(data.get('name'))
        if not author:
            return {'error': 'No author of this name'}
        else:
            authorService.remove_author(author)
            return author

class vendorController:
    @staticmethod
    def add_vendor():
        data = request.form
        new_vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not new_vendor:
            new_vendor = vendorService.add_vendor(data)
            return new_vendor
        else:
            return {'error': 'Vendor already exists'}
        
    @staticmethod
    def update_vendor():
        data = request.form
        vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not vendor:
            return {'error': 'No vendor of this name'}
        else:
            vendor = vendorService.modify_vendor(data)
            return vendor
        
    @staticmethod
    def delete_vendor():
        data = request.form
        vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not vendor:
            return {'error': 'No vendor of this name'}
        else:
            vendorService.remove_vendor(vendor)
            return vendor

    @staticmethod
    def add_vendor():
        data = request.form
        new_vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not new_vendor:
            new_vendor = vendorService.add_vendor(data)
            return new_vendor
        else:
            return {'error': 'Vendor already exists'}
        
    @staticmethod
    def update_vendor():
        data = request.form
        vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not vendor:
            return {'error': 'No vendor of this name'}
        else:
            vendor = vendorService.modify_vendor(data)
            return vendor
        
    @staticmethod
    def delete_vendor():
        data = request.form
        vendor = vendorService.get_vendor_by_name(data.get('name'))
        if not vendor:
            return {'error': 'No vendor of this name'}
        else:
            vendorService.remove_vendor(vendor)
            return vendor