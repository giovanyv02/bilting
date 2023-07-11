from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    itemId = IntegerField("ItemId", validation=[DataRequired])
    userId = IntegerField("UserId")
    review = StringField("Review", validation=[DataRequired])
    stars = IntegerField("Stars", validation=[DataRequired])
    reviewImage = StringField("ReviewImage")

class OrderForm(FlaskForm):
    adress = StringField("Adress", validation=[DataRequired])
    total = IntegerField("Total", validation=[DataRequired])    
    

