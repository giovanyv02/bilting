from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


class FavoriteItem(db.Model):
    __tablename__ = 'favoriteitems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #columns
    id = db.Column(db.Integer, primary_key=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('favorites.id')), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')), nullable=False)

    created_at = db.Column(db.Date, default=datetime.date.today, nullable=False)
    updated_at = db.Column(db.Date, default=datetime.date.today, nullable=False)

    #relationships
    item = db.relationship('Item', back_populates='fav_item')
    favorite = db.relationship('Favorite', back_populates='fav_items')

    def to_dict(self):
        return {
            "id": self.id,
            
            
           
              'itemId': self.item_id,
                "item":{"sex": self.item.sex, "category":self.item.category, "featured":self.item.featured, "sports":self.item.sports, "price":self.item.price, "image":self.item.item_images[0].url}
            }