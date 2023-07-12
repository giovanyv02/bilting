from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    review1 = Review(
        item_id = 1, user_id = 1, review = 'I like it', stars= 5
    )
    review2 = Review(
       item_id = 2, user_id = 2, review = 'superb', stars= 4
        
    )
    review3 = Review(
       item_id = 3, user_id = 3, review = 'trash', stars= 1
        
    )
    review4 = Review(
        item_id = 4, user_id = 1, review = 'I don"t like it', stars= 5
       
    )
    review5 = Review(
        item_id = 5, user_id = 2, review = 'wowww', stars= 4
      
    )
  
    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.commit()



def undo_reviews():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
