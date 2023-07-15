from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import CartItem, db
from app.forms import CartItemForm

cartItem_routes = Blueprint('cartItems', __name__)

@cartItem_routes.route("")
def allUserCartItems():
    cartItems = CartItem.query.filter(CartItem.cart_id == current_user.id)
    return "lalala"

@cartItem_routes.route("/remove/<int:id>", methods = ['POST'])
def removeCartItems(id):
    cartItem = CartItem.query.filter(CartItem.id == id).first()
    db.session.delete(cartItem)
    db.session.commit()
    return {'message': 'Successfully Deleted' }

@cartItem_routes.route('/new', methods = ['POST'])
def addCartItem():
    form = CartItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    print("daaaaaaataaaa", data)
    if form.validate_on_submit():
        newcartItem = CartItem(
            quantity = data['quantity'],
            cart_id = data['cart_id'],
            item_id = data['item_id']
        )
        db.session.add(newcartItem)
        db.session.commit()
        return newcartItem.to_dict()

@cartItem_routes.route('/update/<int:id>', methods = ['POST'])
def updateCartItem(id):
    cartItem = CartItem.query.filter(CartItem.id == id).first()
    data = request.get_json()
    cartItem.quantity = data.get('quantity')
    db.session.commit()






