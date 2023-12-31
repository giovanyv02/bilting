from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #columns
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    reviewImage = db.Column(db.String(1000))
    stars = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, default=datetime.date.today, nullable=False)
    updated_at = db.Column(db.Date, default=datetime.date.today, nullable=False)

    
    user = db.relationship('User', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')

    def to_dict(self):
        return {'id':self.id, 
                'itemId':self.item_id, 
                'userId':self.user_id,
                  'review':self.review, 
                  'reviewImage':self.reviewImage, 
                  'stars':self.stars, 
                  'createdAt':self.created_at, 
                  'updatedAt':self.updated_at,
                  'user': {'firstName': self.user.firstName, 'lastName': self.user.lastName}
                    }