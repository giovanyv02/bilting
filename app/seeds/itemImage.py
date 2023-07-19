from app.models import db, ItemImage, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_itemImages():
    itemImage1 = ItemImage(
       item_id = 1, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966629883318373/item1.png'
    )
    itemImage2 = ItemImage(
       item_id = 2, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966630189510717/item2.png'
        
        
    )
    itemImage3 = ItemImage(
        item_id = 3, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631418433709/item3.png'
        
    )
    itemImage4 = ItemImage(
        item_id = 4, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631703654541/item4.png'
       
    )
    itemImage5 = ItemImage(
          item_id = 5, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966632018215023/item5.png'
      
    )
    itemImage6 = ItemImage(
          item_id = 6, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631129022605/item6.png'
       
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
