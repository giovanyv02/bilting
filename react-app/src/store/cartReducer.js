const LOAD_CART = "carts/LOAD_CART";
const ADD_CARTITEM = "carts/ADD_CARTITEM";
const UPDATE_CARTITEM = "carts/UPDATE_CARTITEM";
const REMOVE_CARTITEM = "carts/REMOVE_CARTITEM";

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

const removeCartItem = (cartItem) => ({
    type: REMOVE_CARTITEM,
    cartItem
});

export const theCart = () => async dispatch => {
    const res = await fetch("/api/cart");
    const cart = await res.json();
    

    dispatch(loadCart(cart));
};

export const addCartItem = (cartItem) => async dispatch => {
    console.log("mennn cart item", cartItem)
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

const cartReducer =  (state = {}, action) =>{
    switch (action.type) {
        case LOAD_CART:
            const newState = {};
            action.cart.cartItems.forEach(ele=>newState[ele.id]=ele)
            return {...newState}
            case ADD_CARTITEM:
                const np = {};
                np[action.cartItem.id]= action.cartItem;
                return {...state, ...np}
            default:
            return state
    }
}

export default cartReducer;