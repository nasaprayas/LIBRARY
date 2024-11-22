import os
from flask import request, Flask
from utils.utils import db
from Models.member_model import Members
from Models.employee_model import Employees

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, current_user
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


class employeeService:
    @staticmethod
    def create_employee(data):
        new_employee = Employees(
            name=data.get('name'),
            mail=data.get('mail'),
            gender=data.get('gender'),
            date_of_birth=data.get('dob'),
            password=generate_password_hash(data.get('password')),
            country=data.get('country'),
            state=data.get('state'),
            city=data.get('city'),
            street=data.get('street'),
        )
        db.session.add(new_employee)
        db.session.commit()
        return new_employee
