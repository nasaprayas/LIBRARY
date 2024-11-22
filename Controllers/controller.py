from flask import request
from Services.service import userService, SearchService, BookService
from flask import Blueprint, jsonify, request
from Views.view import View

class authenticaionController:
    @staticmethod
    def signup():
        full_name=request.form.get('full_name')
        password=request.form.get('password')
        dob=request.form.get('dob')
        email=request.form.get('email')
        user = userService.sign_up(name=full_name,password=password,dob=dob,mail=email)
        return user
    
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