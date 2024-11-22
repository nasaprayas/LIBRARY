from utils.utils import db

class Publishers(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.Text, nullable=False)
    about = db.Column(db.Text)

    def __repr__(self):
        return f"<Publisher {self.name} - ID: {self.id}>"
    def to_dict(self):
        """Convert the PublisherModel instance into a dictionary format."""
        return {
            'publisher_id': self.id,
            'publisher_name': self.name,
            'publisher_address': self.address,
            'about':self.about,
        }