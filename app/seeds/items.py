from app.models import db, Item, environment, SCHEMA
from sqlalchemy.sql import text



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
    item7 = Item(
        sex='man', category='pants', featured='new arrival', sports='running', price=2
    )
    item8 = Item(
        sex='man', category='shirt', featured='new arrival', sports='football', price=145
    )
    item9 = Item(
        sex='man', category='shirt', featured='new arrival', sports='football', price=1409
    )
    item10 = Item(
        sex='women', category='shoe', featured='new arrival', sports='football', price=99
    )
    item11 = Item(
        sex='man', category='shoe', featured='new arrival', sports='football', price=149
    )
    item12 = Item(
        sex='man', category='short', featured='new arrival', sports='football', price=66
    )
    item13 = Item(
        sex='man', category='shoe', featured='new arrival', sports='basket', price=22
    )
    item14 = Item(
        sex='man', category='shoe', featured='new arrival', sports='basket', price=14
    )
    item15 = Item(
        sex='women', category='pant', featured='new arrival', sports='basket', price=99
    )
    item16 = Item(
        sex='women', category='shirt', featured='new arrival', sports='basket', price=87
    )
    item17 = Item(
        sex='man', category='shoe', featured='new arrival', sports='basket', price=11
    )
    item18 = Item(
       sex='man', category='shoe', featured='new arrival', sports='basket', price=2996
    )
    item19 = Item(
        sex='man', category='shoe', featured='new arrival', sports='basket', price=32
    )
    item20 = Item(
        sex='women', category='shoe', featured='new arrival', sports='basket', price=1409
    )
    item21 = Item(
        sex='man', category='bag', featured='new arrival', sports='golf', price=34
    )
    item22 = Item(
        sex='women', category='shoe', featured='new arrival', sports='golf', price=2987
    )
    item23 = Item(
        sex='man', category='shirt', featured='new arrival', sports='golf', price=196
    )
    item24 = Item(
        sex='man', category='pant', featured='new arrival', sports='football', price=6789
    )
    item25 = Item(
        sex='man', category='shoe', featured='new arrival', sports='soccer', price=839
    )
    item26 = Item(
        sex='women', category='short', featured='new arrival', sports='soccer', price=8543
    )

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)
    db.session.add(item7)
    db.session.add(item8)
    db.session.add(item9)
    db.session.add(item10)
    db.session.add(item11)
    db.session.add(item12)
    db.session.add(item13)
    db.session.add(item14)
    db.session.add(item15)
    db.session.add(item16)
    db.session.add(item17)
    db.session.add(item18)
    db.session.add(item19)
    db.session.add(item20)
    db.session.add(item21)
    db.session.add(item22)
    db.session.add(item23)
    db.session.add(item24)
    db.session.add(item25)
    db.session.add(item26)
    db.session.commit()



def undo_items():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM items"))

    db.session.commit()
