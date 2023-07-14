from app.models import db, ItemImage, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_itemImages():
    itemImage1 = ItemImage(
       item_id = 1, url = 'https://static.nike.com/a/images/c_limit,w_592,f_a…apor-11-womens-hard-court-tennis-shoes-jFxzWK.png'
    )
    itemImage2 = ItemImage(
       item_id = 2, url = 'https://static.nike.com/a/images/c_limit,w_592,f_a…apor-11-womens-hard-court-tennis-shoes-jFxzWK.png'
        
        
    )
    itemImage3 = ItemImage(
        item_id = 3, url = '	https://static.nike.com/a/images/t_default/856ed19…-mens-dri-fit-short-sleeve-fitness-top-bc8lMz.png'
        
    )
    itemImage4 = ItemImage(
        item_id = 4, url = 'https://static.nike.com/a/images/t_default/47ebd6a…/rafa-mens-dri-fit-adv-7-tennis-shorts-4skBJP.png'
       
    )
    itemImage5 = ItemImage(
          item_id = 5, url = 'https://static.nike.com/a/images/c_limit,w_592,f_a…cushioned-training-ankle-socks-6-pairs-xql9Hn.png'
      
    )
    itemImage6 = ItemImage(
          item_id = 6, url = 'https://static.nike.com/a/images/c_limit,w_592,f_a…it-victory-big-kids-girls-tennis-skirt-CbbV6g.png'
       
    )
    db.session.add(itemImage1)
    db.session.add(itemImage2)
    db.session.add(itemImage3)
    db.session.add(itemImage4)
    db.session.add(itemImage5)
    db.session.add(itemImage6)
    db.session.commit()



def undo_itemImages():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.itemImages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM itemImages"))

    db.session.commit()
