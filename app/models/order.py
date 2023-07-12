from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


class Order(db.Model):
    __tablename__ = 'orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #columns
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, default=datetime.date.today, nullable=False)
    updated_at = db.Column(db.Date, default=datetime.date.today, nullable=False)

    #relationships
    order_items = db.relationship('OrderItem', back_populates='order')
    user = db.relationship('User', back_populates='orders')