const LOAD_Favorite = "favorites/LOAD_Favorite";
const ADD_FavoriteItem = "favorites/ADD_FavoriteItem";
const UPDATE_FavoriteItem = "favorites/UPDATE_FavoriteItem";
const REMOVE_FavoriteItem = "favorites/REMOVE_FavoriteItem";

const loadFavorite = (favorite) => ({
    type: LOAD_Favorite,
    favorite
});

const addNewFavoriteItem = (favoriteItem) => ({
    type: ADD_FavoriteItem,
    favoriteItem
});

const updateFavoriteItem = (favoriteItem) => ({
    type: UPDATE_FavoriteItem,
    favoriteItem
});

const removeFavoriteItem = (favoriteItemId) => ({
    type: REMOVE_FavoriteItem,
    favoriteItemId
});

export const theFav = () => async dispatch => {
    const res = await fetch("/api/favorite");
    const favorite = await res.json();


    dispatch(loadFavorite(favorite));
};

export const addFavoriteItem = (favoriteItem) => async dispatch => {
    const res = await fetch("/api/favoriteItems/new", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(favoriteItem)
    });
    if (res.ok) {
        const data = await res.json();
        dispatch(addNewFavoriteItem(data));
        return data;

    }
};

export const deleteFavoriteItem = (id) => async dispatch => {
    const res = await fetch(`/api/favoriteItems/remove/${id}`, {
        method: "POST"
    });
    if (res.ok) {
        dispatch(removeFavoriteItem(id));
    }
}



const favoriteReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD_Favorite:
            const newState = {};
            action.favorite.favoriteItems.forEach(ele => newState[ele.id] = ele)
            return { ...newState }
        case ADD_FavoriteItem:
            const np = {};
            np[action.favoriteItem.id] = action.favoriteItem;
            return { ...state, ...np }
        case REMOVE_FavoriteItem:
            let nState = Object.values(state);
            let nState1 = nState.filter(ele=>ele.itemId == action.favoriteItemId)
            const mstate = {...state}
            delete mstate[nState1[0].id]
            return mstate
        default:
            return state
    }
}

export default favoriteReducer;