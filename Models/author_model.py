from utils.utils import db


class AuthorModel(db.Model):
    __tablename__ = 'author'
    
    author_id = db.Column(db.String(10), primary_key=True)
    author_name = db.Column(db.String(50), nullable=False)
    author_dob = db.Column(db.Date, nullable=False)
    author_origin = db.Column(db.Text)
    about = db.Column(db.Text)

    def __repr__(self):
        return f"<Author {self.author_name}>"
    def to_dict(self):
        """Convert the AuthorModel instance into a dictionary format."""
        return {
            'author_id': self.author_id,
            'author_name': self.author_name,
            'author_dob': self.author_dob,
            'author_origin': self.author_origin,
            'about':self.about,
        }
    
    