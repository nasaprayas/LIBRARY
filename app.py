import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from Routes.routes import bp
from utils.utils import db,migrate,login_manager
from Services.service import userService


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/LIBRARY'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'BookArchitects'
login_manager.login_view = 'bp.login'
login_manager.login_message = 'Please log in to access this page.'

app.register_blueprint(bp)
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(mail):
    user = userService.get_member_by_mail(mail) or userService.get_employee_by_mail(mail)
    return user
    

if __name__ == '__main__':
    app.run(debug='True', port=5000)

from Models import author_model,book_model,employee_model,fine_model,member_model,publisher_model,shelf_model,transaction_model,vendor_model