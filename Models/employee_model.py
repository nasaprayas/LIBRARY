from utils.utils import db
from flask_login import UserMixin
from datetime import datetime

class Employees(UserMixin,db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    profile_pic = db.Column(db.Text)
    name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10))
    date_of_joining = db.Column(db.Date, default=datetime.utcnow)
    country = db.Column(db.String(50))
    state = db.Column(db.String(50))
    city = db.Column(db.String(50))
    street = db.Column(db.String(50))
    type = db.Column(db.String(10), default='admin')

    def __repr__(self):
        return f"<Employee {self.employee_name}>"
    
    def to_dict(self):
        """Convert the EmployeeModel instance into a dictionary format."""
        return {
            'employee_id': self.id,
            'employee_name': self.name,
            'employee_email': self.mail,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'date_of_joining': self.date_of_joining.isoformat() if self.date_of_joining else None,
        }
    
    def get_id(self):
        return self.mail