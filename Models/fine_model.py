from utils.utils import db

class FineModel(db.Model):
    __tablename__ = 'fine'
    fine_id = db.Column(db.String(10), primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    days_delay = db.Column(db.Date, nullable=False)
    member_id = db.Column(db.String(10), db.ForeignKey('member.member_id', ondelete="CASCADE"), nullable=False)

    member = db.relationship("MemberModel", backref=db.backref("fines", lazy=True))

    def __repr__(self):
        return f"<Fine {self.fine_id} - Amount: {self.amount}>"
    def to_dict(self):
        """Convert the FineModel instance into a dictionary format."""
        return {
            'fine_id': self.fine_id,
            'amount': self.amount,
            'days_delay': self.days_delay,
            'member_id': self.member_id,
            'member': self.member.to_dict() if self.member else None
        }