from flask import request
from Services.service import userService
from werkzeug.utils import secure_filename
from flask_login import current_user

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