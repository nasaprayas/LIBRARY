from utils.utils import db

class PublisherModel(db.Model):
    __tablename__ = 'publisher'
    publisher_id = db.Column(db.String(10), primary_key=True)
    publisher_name = db.Column(db.String(50), nullable=False)
    publisher_address = db.Column(db.Text, nullable=False)
    about = db.Column(db.Text)

    def __repr__(self):
        return f"<Publisher {self.publisher_name} - ID: {self.publisher_id}>"
    def to_dict(self):
        """Convert the PublisherModel instance into a dictionary format."""
        return {
            'publisher_id': self.publisher_id,
            'publisher_name': self.publisher_name,
            'publisher_address': self.publisher_address,
            'about':self.about,
        }