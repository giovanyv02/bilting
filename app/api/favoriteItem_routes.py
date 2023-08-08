from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import FavoriteItem, Favorite, db
from app.forms import FavoriteItemForm

favoriteItem_routes = Blueprint('favoriteItems', __name__)

@favoriteItem_routes.route("")
def allUserFavoriteItems():
    favoriteItems = FavoriteItem.query.filter(FavoriteItem.favorite_id == current_user.id)
    return "lalala"

@favoriteItem_routes.route("/remove/<int:id>", methods = ['POST'])
def removeFavoriteItems(id):
    favoriteItem = FavoriteItem.query.filter(FavoriteItem.item_id == id).first()
    db.session.delete(favoriteItem)
    db.session.commit()
    return {'message': 'Successfully Deleted' }


@favoriteItem_routes.route('/new', methods = ['POST'])
def addFavItem():
    form = FavoriteItemForm()
    UserFavorite = Favorite.query.filter(Favorite.user_id == current_user.id).first()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    
    if form.validate_on_submit():
        newfavitem = FavoriteItem(
            favorite_id = UserFavorite.id,
            item_id = data['item_id']
        )
        db.session.add(newfavitem)
        db.session.commit()
        return newfavitem.to_dict()





