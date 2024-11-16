from utils.utils import db

class ShelfModel(db.Model):
    __tablename__ = 'shelf'
    shelf_id = db.Column(db.String(10), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    shelf_floor = db.Column(db.Integer, nullable=False)
    shelf_rows = db.Column(db.Integer, nullable=False)
    shelf_cols = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Shelf {self.shelf_id} - Floor: {self.shelf_floor}>"
    def to_dict(self):
        """Convert the ShelfModel instance into a dictionary format."""
        return {
            'shelf_id': self.shelf_id,
            'quantity': self.quantity,
            'shelf_floor': self.shelf_floor,
            'shelf_rows': self.shelf_rows,
            'shelf_cols': self.shelf_cols,
        }