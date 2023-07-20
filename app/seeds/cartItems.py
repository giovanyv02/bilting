from app.models import db, CartItem, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_cartItems():
    cartItem1 = CartItem(
        quantity = 2, cart_id = 1, item_id= 1, size = 'M 3.5 / W 5'
    )
    cartItem2 = CartItem(
        item_id = 2, cart_id = 1, quantity = 1, size = 'M 3.5 / W 5'
        
    )
    cartItem3 = CartItem(
       item_id = 3, cart_id = 2, quantity = 1, size = 'M 3.5 / W 5'
        
    )
    cartItem4 = CartItem(
        item_id = 4, cart_id = 3, quantity = 1, size = 'M 3.5 / W 5'
       
    )
    cartItem5 = CartItem(
       item_id = 5, cart_id = 2, quantity = 2, size = 'M 3.5 / W 5'
      
    )
    
    db.session.add(cartItem1)
    db.session.add(cartItem2)
    db.session.add(cartItem3)
    db.session.add(cartItem4)
    db.session.add(cartItem5)
    db.session.commit()



def undo_cartItems():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.cartItems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cartItems"))

    db.session.commit()
