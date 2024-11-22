from utils.utils import db
from Models.member_model import Members

class Fines(db.Model):
    __tablename__ = 'fine'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    days_delay = db.Column(db.Date, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id', ondelete="CASCADE"), nullable=False)

    member = db.relationship("MemberModel", backref=db.backref("fines", lazy=True))

    def __repr__(self):
        return f"<Fine {self.id} - Amount: {self.amount}>"
    def to_dict(self):
        """Convert the FineModel instance into a dictionary format."""
        return {
            'fine_id': self.id,
            'amount': self.amount,
            'days_delay': self.days_delay,
            'member_id': self.member_id,
            'member': self.member.to_dict() if self.member else None
        }