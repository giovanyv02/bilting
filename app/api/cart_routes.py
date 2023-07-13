from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Cart, db


cart_routes = Blueprint('carts', __name__)

@cart_routes.route("")
@login_required
def cart():
    cart = Cart.query.filter(Cart.user_id == current_user.id).all()
    return cart.to_dict()

@cart_routes.route('/new', methods = ['POST'])
@login_required
def newCart():
   newcart = Cart(
   user_id = current_user.id
   )
   db.session.add(newCart)
   db.session.commit()
   return newcart.to_dict()