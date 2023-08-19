from app.models import db, FavoriteItem, environment, SCHEMA
from sqlalchemy.sql import text



def seed_favoriteItems():
    favoriteItem1 = FavoriteItem(
         favorite_id = 1, item_id= 1
    )
    favoriteItem2 = FavoriteItem(
        item_id = 2, favorite_id = 1
        
    )
    favoriteItem3 = FavoriteItem(
       item_id = 3, favorite_id = 2
        
    )
    favoriteItem4 = FavoriteItem(
        item_id = 4, favorite_id = 3
       
    )
    favoriteItem5 = FavoriteItem(
       item_id = 5, favorite_id = 2
      
    )
    
    db.session.add(favoriteItem1)
    db.session.add(favoriteItem2)
    db.session.add(favoriteItem3)
    db.session.add(favoriteItem4)
    db.session.add(favoriteItem5)
    db.session.commit()



def undo_favoriteItems():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.favoriteItems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favoriteItems"))

    db.session.commit()
