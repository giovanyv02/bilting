from app.models import db, ItemImage, environment, SCHEMA
from sqlalchemy.sql import text



def seed_itemImages():
    # hello
    itemImage1 = ItemImage(
       item_id = 1, url = 'https://i.postimg.cc/Pf6wK8WH/item1.png'
    )
    itemImage2 = ItemImage(
       item_id = 2, url = 'https://i.postimg.cc/SRtYKwSR/item2.png'

    )
    itemImage3 = ItemImage(
        item_id = 3, url = 'https://i.postimg.cc/D0zbn2KR/item3.png'

    )
    itemImage4 = ItemImage(
        item_id = 4, url = 'https://i.postimg.cc/85N6XRXp/item4.png'

    )
    itemImage5 = ItemImage(
          item_id = 5, url = 'https://i.postimg.cc/KYnT5qNp/item5.png'

    )
    itemImage6 = ItemImage(
          item_id = 6, url = 'https://i.postimg.cc/hjs7kXN9/item6.png'

    )
    itemImage7 = ItemImage(
        item_id = 7, url = 'https://i.postimg.cc/15kZZJGK/football6.png'
    )
    itemImage8 = ItemImage(
        item_id = 8, url = 'https://i.postimg.cc/jqkbMsCm/football5.png'
    )
    itemImage9 = ItemImage(
        item_id = 9, url = 'https://i.postimg.cc/DyJKDtXZ/football4.png'
    )
    itemImage10 = ItemImage(
        item_id = 10, url = 'https://i.postimg.cc/B6S0VbT9/football3.png'
    )
    itemImage11 = ItemImage(
        item_id = 11, url = 'https://i.postimg.cc/bJmhcPgG/football2.png'
    )
    itemImage12 = ItemImage(
        item_id = 12, url = 'https://i.postimg.cc/gjrPG7tg/football1.png'
    )
    itemImage13 = ItemImage(
        item_id = 13, url = 'https://i.postimg.cc/QCFv2TVP/basket8.png'
    )
    itemImage14 = ItemImage(
        item_id = 14, url = 'https://i.postimg.cc/C1PWrNMk/basket7.png'
    )
    itemImage15 = ItemImage(
        item_id = 15, url = 'https://i.postimg.cc/25mR1yXb/basket6.png'
    )
    itemImage16 = ItemImage(
        item_id = 16, url = 'https://i.postimg.cc/85P2b3GT/basket5.png'
    )
    itemImage17 = ItemImage(
        item_id = 17, url = 'https://i.postimg.cc/2yJNyxPr/basket4.png'
    )
    itemImage18 = ItemImage(
        item_id = 18, url = 'https://i.postimg.cc/5t3cLJZP/basket3.png'
    )
    itemImage19 = ItemImage(
        item_id = 19, url = 'https://i.postimg.cc/4xpR4VwR/basket2.png'
    )
    itemImage20 = ItemImage(
        item_id = 20, url = 'https://i.postimg.cc/vmdM53Dm/basket1.png'
    )
    itemImage21 = ItemImage(
        item_id = 21, url = 'https://i.postimg.cc/PqzHyY8Q/golf4.png'
    )
    itemImage22 = ItemImage(
        item_id = 22, url = 'https://i.postimg.cc/VLpbPQZH/golf3.png'
    )
    itemImage23 = ItemImage(
        item_id = 23, url = 'https://i.postimg.cc/ZKCyQKHd/golf2.png'
    )
    itemImage24 = ItemImage(
        item_id = 24, url = 'https://i.postimg.cc/GhHcR4Zb/golf1.png'
    )
    itemImage25 = ItemImage(
        item_id = 25, url = 'https://i.postimg.cc/wMB97MMc/soccer6.png'
    )
    itemImage26 = ItemImage(
        item_id = 26, url = 'https://i.postimg.cc/6q4dJWKz/soccer5.png'
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
