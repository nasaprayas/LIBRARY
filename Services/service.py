from flask import request, Flask
from utils.utils import db
from Models.member_model import Members
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