from utils.utils import db
from datetime import datetime
from Models.employee_model import EmployeeModel
from Models.book_model import BookModel
from Models.member_model import MemberModel

from datetime import datetime

IST= datetime('Asia/Kolkata')
class TransactionModel(db.Model):
    __tablename__ = 'transaction'
    transaction_id = db.Column(db.String(10), primary_key=True)
    transaction_type = db.Column(db.String(10), nullable=False)  # "issue" or "return"
    transaction_date = db.Column(db.DateTime, default=datetime.now(IST), nullable=False)
    employee_id = db.Column(db.String(10), db.ForeignKey('employee.employee_id', onupdate="CASCADE"), nullable=False)
    member_id = db.Column(db.String(10), db.ForeignKey('member.member_id', onupdate="CASCADE"), nullable=False)
    book_id = db.Column(db.String(10), db.ForeignKey('book.book_id', onupdate="CASCADE"), nullable=False)

    # Relationships to retrieve related data if needed
    employee = db.relationship('EmployeeModel', backref='transactions', lazy=True)
    member = db.relationship('MemberModel', backref='transactions', lazy=True)
    book = db.relationship('BookModel', backref='transactions', lazy=True)

    def __repr__(self):
        return f"<Transaction {self.transaction_id} - {self.transaction_type}>"
    
    def to_dict(self):
        """Convert the TransactionModel instance into a dictionary format."""
        return {
            'transaction_id': self.transaction_id,
            'transaction_type': self.transaction_type,
            'transaction_date': self.transaction_date.isoformat() if self.transaction_date else None,
            'employee_id': self.employee_id,
            'member_id': self.member_id,
            'book_id': self.book_id,
            'employee': self.employee.to_dict() if self.employee else None,
            'member': self.member.to_dict() if self.member else None,
            'book': self.book.to_dict() if self.book else None
        }