from utils.utils import db
from flask import Flask
class VendorModel(db.Model):
    __tablename__ = 'vendor'
    vendor_id = db.Column(db.String(10), primary_key=True)
    vendor_name = db.Column(db.String(50), nullable=False)
    vendor_address = db.Column(db.Text, nullable=False)
    about = db.Column(db.Text)

    def __repr__(self):
        return f"<Vendor {self.vendor_name}>"
    
    def to_dict(self):
        """Convert the VendorModel instance into a dictionary format."""
        return {
            'vendor_id': self.vendor_id,
            'vendor_name': self.vendor_name,
            'vendor_address': self.vendor_address,
            'about': self.about,
        }
    
    