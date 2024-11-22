from utils.utils import db

class Shelfs(db.Model):
    __tablename__ = 'shelf'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    no_of_rows = db.Column(db.Integer, nullable=False)
    no_of_cols = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Shelf {self.id} - Floor: {self.floor}>"
    def to_dict(self):
        """Convert the ShelfModel instance into a dictionary format."""
        return {
            'shelf_id': self.id,
            'quantity': self.quantity,
            'shelf_floor': self.floor,
            'shelf_rows': self.no_of_rows,
            'shelf_cols': self.no_of_cols,
        }