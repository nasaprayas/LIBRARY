from utils.utils import db
from datetime import datetime
import flask_login

class Members(flask_login.UserMixin, db.Model):
    __tablename__ = 'member'
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
    type = db.Column(db.String(10), default='member')

    def __repr__(self):
        return f"<Member {self.name} - ID: {self.id}>"
    
    def to_dict(self):
        """Convert the MemberModel instance into a dictionary format."""
        return {
            'id': self.id,
            'name': self.name,
            'mail': self.mail,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'gender': self.gender,
            'date_of_joining': self.date_of_joining.isoformat() if self.date_of_joining else None,
            'country': self.country,
            'state': self.state,
            'city': self.city,
            'street': self.street,
        }
    
    def get_id(self):
        return self.mail