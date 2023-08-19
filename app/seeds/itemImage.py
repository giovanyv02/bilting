from app.models import db, ItemImage, environment, SCHEMA
from sqlalchemy.sql import text



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
    itemImage7 = ItemImage(
        item_id = 7, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694877327593572/football6.png'
    )
    itemImage8 = ItemImage(
        item_id = 8, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694877608628316/football5.png'
    )
    itemImage9 = ItemImage(
        item_id = 9, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878120316948/football4.png'
    )
    itemImage10 = ItemImage(
        item_id = 10, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878539743383/football3.png'
    )
    itemImage11 = ItemImage(
        item_id = 11, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878791422033/football2.png'
    )
    itemImage12 = ItemImage(
        item_id = 12, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879005315122/football1.png'
    )
    itemImage13 = ItemImage(
        item_id = 13, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879240192000/basket8.png'
    )
    itemImage14 = ItemImage(
        item_id = 14, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879487660042/basket7.png'
    )
    itemImage15 = ItemImage(
        item_id = 15, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879743508501/basket6.png'
    )
    itemImage16 = ItemImage(
        item_id = 16, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879986798613/basket5.png'
    )
    itemImage17 = ItemImage(
        item_id = 17, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002028441772/basket4.png'
    )
    itemImage18 = ItemImage(
        item_id = 18, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002376589412/basket3.png'
    )
    itemImage19 = ItemImage(
        item_id = 19, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002645012621/basket2.png'
    )
    itemImage20 = ItemImage(
        item_id = 20, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003064434718/basket1.png'
    )
    itemImage21 = ItemImage(
        item_id = 21, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003286753320/golf4.png'
    )
    itemImage22 = ItemImage(
        item_id = 22, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003521622026/golf3.png'
    )
    itemImage23 = ItemImage(
        item_id = 23, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003743912057/golf2.png'
    )
    itemImage24 = ItemImage(
        item_id = 24, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004113031219/golf1.png'
    )
    itemImage25 = ItemImage(
        item_id = 25, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004444368946/soccer6.png'
    )
    itemImage26 = ItemImage(
        item_id = 26, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004696018995/soccer5.png'
    )
    
    db.session.add(itemImage1)
    db.session.add(itemImage2)
    db.session.add(itemImage3)
    db.session.add(itemImage4)
    db.session.add(itemImage5)
    db.session.add(itemImage6)
    db.session.add(itemImage7)
    db.session.add(itemImage8)
    db.session.add(itemImage9)
    db.session.add(itemImage10)
    db.session.add(itemImage11)
    db.session.add(itemImage12)
    db.session.add(itemImage13)
    db.session.add(itemImage14)
    db.session.add(itemImage15)
    db.session.add(itemImage16)
    db.session.add(itemImage17)
    db.session.add(itemImage18)
    db.session.add(itemImage19)
    db.session.add(itemImage20)
    db.session.add(itemImage21)
    db.session.add(itemImage22)
    db.session.add(itemImage23)
    db.session.add(itemImage24)
    db.session.add(itemImage25)
    db.session.add(itemImage26)
    db.session.commit()



def undo_itemImages():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.itemImages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM itemImages"))

    db.session.commit()
