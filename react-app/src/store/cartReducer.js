const LOAD_CART = "carts/LOAD_CART";
const ADD_CARTITEM = "carts/ADD_CARTITEM";
const UPDATE_CARTITEM = "carts/UPDATE_CARTITEM";
const REMOVE_CARTITEM = "carts/REMOVE_CARTITEM";
const REMOVE_CART = "carts/REMOVE_CART";

const removeCart = () => ({
    type: REMOVE_CART
})

const loadCart = (cart) => ({
    type: LOAD_CART,
    cart
});

const addNewCartItem = (cartItem) => ({
    type: ADD_CARTITEM,
    cartItem
});

const updateCartItem = (cartItem) => ({
    type: UPDATE_CARTITEM,
    cartItem
});

const removeCartItem = (cartItemId) => ({
    type: REMOVE_CARTITEM,
    cartItemId
});

export const theCart = () => async dispatch => {
    const res = await fetch("/api/cart");
    const cart = await res.json();


    dispatch(loadCart(cart));
};

export const addCartItem = (cartItem) => async dispatch => {
    const res = await fetch("/api/cartItems/new", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(cartItem)
    });
    if (res.ok) {
        const data = await res.json();
        dispatch(addNewCartItem(data));
        return data;

    }
};

export const removeTheCart = () => async dispatch => {
    dispatch(removeCart())
}

export const deleteCartItem = (id) => async dispatch => {
    const res = await fetch(`/api/cartItems/remove/${id}`, {
        method: "POST"
    });
    if (res.ok) {
        dispatch(removeCartItem(id));
    }
}

export const cartItemToUpdate = (id, item) => async dispatch => {
    const res = await fetch(`/api/cartItems/update/${id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(item)
    });

    if (res.ok) {

        const cartItem = await res.json()

        dispatch(updateCartItem(cartItem))
        return res
    }
}

const cartReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD_CART:
            const newState = {};
            action.cart.cartItems.forEach(ele => newState[ele.id] = ele)
            return { ...newState }
        case ADD_CARTITEM:
            const np = {};
            np[action.cartItem.id] = action.cartItem;
            return { ...state, ...np }
        case UPDATE_CARTITEM:
            return { ...state, [action.cartItem.id]: action.cartItem }
        case REMOVE_CARTITEM:
            const nState = { ...state };

            delete nState[action.cartItemId];
            return nState
        case REMOVE_CART:
            const blankState = {}
            return blankState
        default:
            return state
    }
}

export default cartReducer;