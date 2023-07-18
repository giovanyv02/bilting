from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


class OrderItem(db.Model):
    __tablename__ = 'orderitems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #columns
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('items.id')), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('orders.id')), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, default=datetime.date.today, nullable=False)
    updated_at = db.Column(db.Date, default=datetime.date.today, nullable=False)

    #relationships
    item = db.relationship('Item', back_populates='order_item')
    order = db.relationship('Order', back_populates='order_items')