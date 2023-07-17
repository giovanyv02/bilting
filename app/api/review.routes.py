from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Review, db
from app.forms import ReviewForm

review_routes = Blueprint('cartItems', __name__)

@review_routes.route("")
def allReview():
    reviews = Review.query.all()
    return [review.to_dict() for review in reviews]


@review_routes.route("/remove/<int:id>", methods = ['POST'])
def removeReviews(id):
    review = Review.query.filter(Review.id == id).first()
    db.session.delete(review)
    db.session.commit()
    return {'message': 'Successfully Deleted' }

@review_routes.route('/new', methods = ['POST'])
def addReview():
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    
    if form.validate_on_submit():
        newReview = Review(
            user_id = data.current_user.id,
            cart_id = data['cart_id'],
            item_id = data['item_id'],
            review = data['review'],
            stars = data['stars'],

        )
        db.session.add(newReview)
        db.session.commit()
        return newReview.to_dict()

@review_routes.route('/update/<int:id>', methods = ['POST'])
def updateReview(id):
    review = Review.query.filter(Review.id == id).first()
    data = request.get_json()
    review.review = data.get('review')
    review.stars = data.get('stars')
    db.session.commit()
    return review.to_dict()






