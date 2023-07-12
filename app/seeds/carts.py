from app.models import db, Cart, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_carts():
    cart1 = Cart(
        user_id = 1, total = 6000
    )
    cart2 = Cart(
         user_id = 2, total = 7000
        
    )
    cart3 = Cart(
         user_id = 3, total = 8000
        
    )
  
  
    db.session.add(cart1)
    db.session.add(cart2)
    db.session.add(cart3)
    db.session.commit()



def undo_carts():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.carts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM carts"))

    db.session.commit()
