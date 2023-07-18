const LOAD_REVIEW = "reviews/LOAD_REVIEW";
const ADD_REVIEW = "reviews/ADD_REVIEW";
const UPDATE_REVIEW = "reviews/UPDATE_REVIEW";
const REMOVE_REVIEW = "reviews/REMOVE_REVIEW";

const loadReview = (reviews) => ({
    type: LOAD_REVIEW,
    reviews
});

const addNewReview = (review) => ({
    type: ADD_REVIEW,
    review
});

const updateReview = (review) => ({
    type: UPDATE_REVIEW,
    review
});

const removeReview = (reviewId) => ({
    type: REMOVE_REVIEW,
    reviewId
});

export const allReviews = () => async dispatch => {
    const res = await fetch("/api/reviews");
    const reviews = await res.json();

    dispatch(loadReview(reviews));
};

export const addReview = (review) => async dispatch => {
    const res = await fetch('/api/reviews/new', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(review)
    });
    if (res.ok) {
        const data = await res.json();
        dispatch(addNewReview(data));
        return data;

    }
};

export const deleteReview = (id) => async dispatch => {
    const res = await fetch(`/api/reviews/remove/${id}`, {
        method: "POST"
    });
    if (res.ok) {
        // dispatch(removeSpot(id));
        dispatch(removeReview(id));
    }
}

export const reviewUpdate = (id, ques) => async dispatch => {
    const res = await fetch(`/api/reviews/update/${id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(ques)
    });

    if (res.ok) {

        const updateQues = await res.json()

        dispatch(updateReview(updateQues))
        return res
    }
}

const reviewReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD_REVIEW:
            const newState = {};
            action.reviews.forEach(ele => newState[ele.id] = ele);
            return { ...state, ...newState }
        case ADD_REVIEW:
            const np = {};
            np[action.review.id] = action.review;
            return { ...state, ...np }
        case UPDATE_REVIEW:
            return { ...state, [action.review.id]: action.review }
        case REMOVE_REVIEW:
            const nState = { ...state };

            delete nState[action.reviewId];
            return nState
        default:
            return state
    }
};

export default reviewReducer
