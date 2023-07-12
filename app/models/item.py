from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


class Item(db.Model):
    __tablename__ = 'items'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #columns
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(1000), nullable=False)
    featured = db.Column(db.String(1000), nullable=False)
    sports = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, default=datetime.date.today, nullable=False)
    updated_at = db.Column(db.Date, default=datetime.date.today, nullable=False)

    #relationships
    reviews = db.relationship('Review', back_populates='item')
    order_item = db.relationship('Item', back_populates='item')
    cart_item = db.relationship('CartItem', back_populates='item')
    item_images = db.relationship('ItemImage', back_populates='item')
    