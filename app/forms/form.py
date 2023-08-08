from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.api.AWS_helpers import ALLOWED_EXTENSIONS

class ReviewForm(FlaskForm):
    itemId = IntegerField("ItemId")
    userId = IntegerField("UserId")
    review = StringField("Review")
    stars = IntegerField("Stars")
    reviewImage = StringField("ReviewImage")
    # reviewimage = FileField("Image File", validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])

class OrderForm(FlaskForm):
    adress = StringField("Adress", validation=[DataRequired])
    total = IntegerField("Total", validation=[DataRequired])    
    
class CartItemForm(FlaskForm):
    quantity = IntegerField("Quantity")
    size = StringField('Size')
    cart_id = IntegerField('CartId')
    item_id = IntegerField('ItemId') 

class FavoriteItemForm(FlaskForm):
    # fav_id = IntegerField('FavId')
    item_id = IntegerField('ItemId')    

