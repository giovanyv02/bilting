from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


class CartItem(db.Model):
    __tablename__ = 'cartitems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #columns
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(1000), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('carts.id')), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')), nullable=False)

    created_at = db.Column(db.Date, default=datetime.date.today, nullable=False)
    updated_at = db.Column(db.Date, default=datetime.date.today, nullable=False)

    #relationships
    item = db.relationship('Item', back_populates='cart_item')
    cart = db.relationship('Cart', back_populates='cart_items')

    def to_dict(self):
        return {
            "id": self.id,
            'id': self.id, 
            'quantity': self.quantity,
              'itemId': self.item_id,
                "item":{"sex": self.item.sex, "category":self.item.category, "featured":self.item.featured, "sports":self.item.sports, "price":self.item.price, "image":self.item.item_images[0].url}
            }