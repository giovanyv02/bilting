from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from api.AWS_helpers import ALLOWED_EXTENSIONS
from app.api.AWS_helpers import ALLOWED_EXTENSIONS

class ReviewForm(FlaskForm):
    itemId = IntegerField("ItemId", validation=[DataRequired])
    userId = IntegerField("UserId")
    review = StringField("Review", validation=[DataRequired])
    stars = IntegerField("Stars", validation=[DataRequired])
    reviewImage = StringField("ReviewImage")
    # reviewimage = FileField("Image File", validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])

class OrderForm(FlaskForm):
    adress = StringField("Adress", validation=[DataRequired])
    total = IntegerField("Total", validation=[DataRequired])    
    
class CartItemForm(FlaskForm):
    quantity = IntegerField("Quantity")
    cart_id = IntegerField('CartId')
    item_id = IntegerField('ItemId') 

