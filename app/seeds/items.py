from app.models import db, Item, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_items():
    item1 = Item(
        sex='man', category='shoe', featured='new arrival', sports='tennis', price=3000
    )
    item2 = Item(
        sex='women', category='shoe', featured='new arrival', sports='tennis', price=2000
        
    )
    item3 = Item(
        sex='kid', category='shirt', featured='fitness essential', sports='basket', price=90
        
    )
    item4 = Item(
        sex='man', category='shorts', featured='new arrival', sports='tennis', price=3000
       
    )
    item5 = Item(
        sex='women', category='socks', featured='new arrival', sports='soccer', price=30
      
    )
    item6 = Item(
        sex='kid', category='shirt', featured='fitness essntial', sports='basket', price=40
       
    )
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)
    db.session.commit()



def undo_items():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM items"))

    db.session.commit()
