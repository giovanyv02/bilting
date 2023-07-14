const LOAD_ITEM = "itemms/LOAD_ITEM";

const loadItem = (items) => ({
    type: LOAD_ITEM,
    items
});

export const allItems = () => async dispatch => {
    const res = await fetch("/api/items");
    const items = await res.json();

    dispatch(loadItem(items));
};

const itemsReducer = (state = {}, action) =>{
    switch(action.type){
        case LOAD_ITEM:
            const newState = {};
            action.items.forEach(item => newState[item.id] = item);
            return {...state, ...newState}
            default:
                return state
    }
}

export default itemsReducer
