from utils.utils import db

class EmployeeModel(db.Model):
    __tablename__ = 'employee'
    employee_id = db.Column(db.String(10), primary_key=True)
    employee_name = db.Column(db.String(50), nullable=False)
    employee_email = db.Column(db.String(50), nullable=False)
    employee_phone = db.Column(db.BigInteger, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_joining = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Employee {self.employee_name}>"
    
    def to_dict(self):
        """Convert the EmployeeModel instance into a dictionary format."""
        return {
            'employee_id': self.employee_id,
            'employee_name': self.employee_name,
            'employee_email': self.employee_email,
            'employee_phone': self.employee_phone,
            'gender': self.gender,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'date_of_joining': self.date_of_joining.isoformat() if self.date_of_joining else None,
        }