from app.models import db, Order, environment, SCHEMA
from sqlalchemy.sql import text



def seed_orders():
    order1 = Order(
        address = "1503 jacmel ave.", user_id = 1, total = 6000
    )
    order2 = Order(
           address = "1503 jacmel ave.", user_id = 2, total = 7000
        
    )
    order3 = Order(
          address = "1503 jacmel ave.", user_id = 3, total = 8000
        
    )
  
  
    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    db.session.commit()



def undo_orders():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orders"))

    db.session.commit()
