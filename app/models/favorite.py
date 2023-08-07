from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


class Favorite(db.Model):
    __tablename__ = 'favorites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #columns
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    created_at = db.Column(db.Date, default=datetime.date.today, nullable=False)
    updated_at = db.Column(db.Date, default=datetime.date.today, nullable=False)

    #relationships
    user = db.relationship('User', back_populates='favorite')
    fav_items = db.relationship('FavoriteItem', back_populates='favorite')

    def to_dict(self):
        return {
            "id": self.id,
            
            'userId': self.user_id,
            'favoriteItems': [{'id': cart.id,  'itemId': cart.item_id, "item":{"sex": cart.item.sex, "category":cart.item.category, "featured":cart.item.featured, "sports":cart.item.sports, "price":cart.item.price, "image":cart.item.item_images[0].url}} for cart in self.fav_items]
        }