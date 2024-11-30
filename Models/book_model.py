from utils.utils import db
from Models.author_model import Authors
from Models.publisher_model import Publishers
from Models.vendor_model import Vendors
from Models.shelf_model import Shelfs
from datetime import datetime

class Books(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    preface = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id', onupdate="CASCADE"), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id', onupdate="CASCADE"), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id', onupdate="CASCADE"), nullable=False)
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.id', onupdate="CASCADE"), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Integer, nullable=False)
    date_of_publishing = db.Column(db.Date)
    date_of_addition = db.Column(db.Date, default=datetime.utcnow)
    shelf_date = db.Column(db.Date)
    bought_on = db.Column(db.Date)
    cover_page = db.Column(db.Text)
    
    def __repr__(self):
        return f"<Book {self.book_title}>"
    def to_dict(self):
        """Convert the BookModel instance into a dictionary format."""
        return {
            'book_id': self.id,
            'title': self.title,
            'preface': self.preface,
            'author_id': self.author_id,
            'author': Authors.query.filter_by(id=self.author_id).first().name,
            'about_author': Authors.query.filter_by(id=self.author_id).first().about,
            'publisher_id': self.publisher_id,
            'publisher': Publishers.query.filter_by(id=self.publisher_id).first().name,
            'vendor_id': self.vendor_id,
            'vendor': Vendors.query.filter_by(id=self.vendor_id).first().name,
            'shelf_id': self.shelf_id,
            'floor': Shelfs.query.filter_by(id=self.shelf_id).first().floor,
            'language': self.language,
            'subject': self.subject,
            'category': self.category,
            'genre': self.genre,
            'price': self.price,
            'availability': self.availability,
            'date_of_publishing': self.date_of_publishing.isoformat() if self.date_of_publishing else None,
            'date_of_addition': self.date_of_addition.isoformat() if self.date_of_addition else None,
            'shelf_date': self.shelf_date.isoformat() if self.shelf_date else None,
            'bought_on': self.bought_on.isoformat() if self.bought_on else None,
            'cover_page': self.cover_page
        }