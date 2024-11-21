from flask import request
from Services.service import userService

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

class userController():
    @staticmethod
    def update_details():
        return