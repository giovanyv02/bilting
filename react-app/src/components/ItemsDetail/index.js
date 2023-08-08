import { useSelector, useDispatch } from 'react-redux';
import { useParams, useHistory } from "react-router-dom";
import { useState, useEffect } from "react";
import { theCart, addCartItem } from '../../store/cartReducer';
import { allItems } from '../../store/itemReducer';
import { addFavoriteItem, deleteFavoriteItem } from '../../store/favoriteReducer';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import './itemDetail.css'
import { cartItemToUpdate } from '../../store/cartReducer';


function ItemDetail() {
    const history = useHistory()
    const user = useSelector(state => state.session.user)

    const dispatch = useDispatch();
    useEffect(() => {
        if (user) {

            dispatch(theCart())
            
        }

    }, [dispatch], [user]);

    useEffect(()=>{
        dispatch(allItems())
    },[dispatch])



    const itemId = parseInt(useParams().itemId)
    const item = useSelector(state => state.items[itemId])
    const allCartItems = useSelector(state => Object.values(state.cart))
    const allCartItemIds = allCartItems.map(ele => ele.itemId)
    const allUserFavItems = useSelector(state => Object.values(state.favorite))
    const allUserFavItemIds = allUserFavItems.map(ele=> ele.itemId)

    
    
    let userId
    if (user) userId = user.id
    
    
    const shoeSizes = ['M 3.5 / W 5', 'M 5.5 / W 7', 'M 10.5 / W 12', 'M 15 / W 14.5']
    const choice = [0, 1, 2, 3, 4, 5, 6, 7]
    const [run, setRun] = useState(false)
    const [size, setSize] = useState("")
    const [quantity, setQuantity] = useState(0)
    const [validationErrors, setValidationErrors] = useState({});
    
    
    const err = {}
    if (!size) err['size'] = 'Please select a size'
    if (!quantity || quantity < 1) err['quantity'] = 'Please select a quantity'
    let newCartItem = {}
    if (!Object.values(err).length) {
        newCartItem = {
            "quantity": parseInt(quantity),
            "item_id": itemId,
            "cart_id": userId,
            'size': size
        }
    }
    
    
    
    useEffect(() => {
        if (run && Object.values(newCartItem).length > 2) {
            if (allCartItemIds.includes(itemId)) {
               

                const cartItmToUpdate = allCartItems.filter(ele => ele.itemId === itemId && ele.size === size)
                
                if (cartItmToUpdate[0]) {
                    
                const total = cartItmToUpdate[0].quantity + parseInt(quantity)
                
                dispatch(cartItemToUpdate(cartItmToUpdate[0].id,{'quantity': total, "size": size}))
                    setRun(false);
                    setSize("")
                } else {
                    dispatch(addCartItem(newCartItem))
                    setRun(false)
                    setSize("")
                }
                
            } else {
                dispatch(addCartItem(newCartItem))
                setRun(false)
                setSize("")
                
            }
        }
    }, [dispatch, run])
    
    const updateSize = (e) => setSize(e.target.dataset.value)
    const updateQuantity = (e) => setQuantity(e.target.value)
    
    
    
    const onSubmit = (e) => {
        setValidationErrors(err);
        if (!userId) history.push('/login')
        e.preventDefault();
        
        if (!Object.values(err).length) {
            setRun(true)
        }

    }

    const addFavItem = (e)=>{
        if (!userId) history.push('/login')
        e.preventDefault();
    const fav = {"item_id": itemId}
    dispatch(addFavoriteItem(fav))    
    }

    const removeFavItem = (e)=>{
        e.preventDefault();
        dispatch(deleteFavoriteItem(itemId))
    }

    if(!item){
        return null
    }
    return (
        <div className='a'>
            <div className='detailImgDiv'>
                <img src={item.images[0].url} className='imgDiiv' />
            </div>
            <div className='detailDiv'>
                <p className='pDetail'>{item.sports} {item.category}</p>
                <p className='pDetail'>${item.price}</p>
                <p>Select size</p>
                {validationErrors["size"] && <p className='errors'>{validationErrors['size']}</p>}
                <div className='allButtonsDiv'>
                    {shoeSizes.map(shoeSize =>
                        <button onClick={updateSize} data-value={shoeSize} className={shoeSize === size ? "selectedSize" :'sizeOption'}>{shoeSize}</button>
                    )}
                </div>
                <div className='quantityDrop'>
                    <p>Quantity</p>
                    <select id="dropdown" onChange={updateQuantity}>
                        {choice.map(num =>
                            <option value={num}>{num}</option>
                        )}
                    </select>

                </div>
                {validationErrors["quantity"]&& <p className='errors'>{validationErrors['quantity']}</p>}

                <button onClick={onSubmit} className='addToBag'>Add to bag</button>
                {user && allUserFavItemIds.includes(itemId) && <button onClick={removeFavItem} className='addToFav'>Favorite <i class="fa-solid fa-heart"></i></button>}
                {user && !allUserFavItemIds.includes(itemId) && <button onClick={addFavItem} className='addToFav'>Favorite <i class="fa-regular fa-heart"></i></button>}
                {!user && <button onClick={addFavItem} className='addToFav'>Favorite <i class="fa-regular fa-heart"></i></button>}

                <NavLink to={`/reviews/${item.id}`}>Reviews({item.reviews.length})</NavLink>
            </div>
        </div>
    )
}
export default ItemDetail;