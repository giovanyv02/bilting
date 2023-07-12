from app.models import db, OrderItem, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_orderItems():
    orderItem1 = OrderItem(
        item_id = 1, order_id = 1, quantity = 2
    )
    orderItem2 = OrderItem(
         item_id = 2, order_id = 1, quantity = 1
        
    )
    orderItem3 = OrderItem(
        item_id = 3, order_id = 2, quantity = 1
        
    )
    orderItem4 = OrderItem(
         item_id = 4, order_id = 3, quantity = 1
       
    )
    orderItem5 = OrderItem(
          item_id = 5, order_id = 2, quantity = 2
      
    )
  
    db.session.add(orderItem1)
    db.session.add(orderItem2)
    db.session.add(orderItem3)
    db.session.add(orderItem4)
    db.session.add(orderItem5)
    db.session.commit()



def undo_orderItems():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.orderItems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orderItems"))

    db.session.commit()
