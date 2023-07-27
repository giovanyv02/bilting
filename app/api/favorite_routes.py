from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Favorite, db


favorite_routes = Blueprint('favorites', __name__)

@favorite_routes.route("")
@login_required
def fav():
    favorite = Favorite.query.filter(Favorite.user_id == current_user.id).first()
    return favorite.to_dict()

@favorite_routes.route('/new', methods = ['POST'])
@login_required
def newFav():
   newfav = Favorite(
   user_id = current_user.id
   )
   db.session.add(newfav)
   db.session.commit()
   return newfav.to_dict()