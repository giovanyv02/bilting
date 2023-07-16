import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { theCart, addCartItem } from '../../store/cartReducer';
import { cartItemToUpdate } from '../../store/cartReducer';

const CartComponent = () =>{
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(theCart())
        
    }, [dispatch]);

    const choice = [0,1,2,3,4,5,6,7]
    const [quantity, setQuantity] = useState(0)

    // const updateQuantity = (e)=> setQuantity(e.target.value)
    function updateQuantity(e){
        const cartItem = {
            'quantity': parseInt(e.target.value)
        }
        dispatch(cartItemToUpdate(e.target.dataset.value, cartItem))
    }
    const allCartItems = useSelector(state=>Object.values(state.cart))
    return (
        <div>
            <div>
            <p>Bags</p>
            {allCartItems.map(ele=>
                <div>
                    <div>
                        <img src={ele.item.image}/>
                    </div>
                    <div>
                        <p>{ele.item.sports} {ele.item.category}</p>
                        <p>Quantity</p>
                        <select id="dropdown" value={ele.quantity} data-value={ele.id} onChange={updateQuantity}>
                    {choice.map(num=>
                        <option  value={num}>{num}</option>
                        )}
                </select>
                    </div>
                </div>
                )}
            </div>
            <div>

            </div>
        </div>
    )
}

export default CartComponent;