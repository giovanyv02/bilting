import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { theCart, addCartItem } from '../../store/cartReducer';
import { cartItemToUpdate, deleteCartItem } from '../../store/cartReducer';
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import LoginFormModal from '../LoginFormModal';
import "./cart.css"

const CartComponent = () => {
    const history = useHistory();
    let userId
    let user = useSelector(state => state.session.user)
    if (user) {
        userId = user.id
    }
    if (!user) history.push('/login')
    const dispatch = useDispatch();
    useEffect(() => {
        if (userId) {

            dispatch(theCart())
        }

    }, [dispatch]);

    const choice = [1, 2, 3, 4, 5, 6, 7]
    const [quantity, setQuantity] = useState(0)

    // const updateQuantity = (e)=> setQuantity(e.target.value)
    function updateQuantity(e) {
        const cartItem = {
            'quantity': parseInt(e.target.value)
        }
        dispatch(cartItemToUpdate(e.target.dataset.value, cartItem))
    }
    function deleteI(e) {
        const id = e.target.dataset.value
        dispatch(deleteCartItem(id))

    }

    const allCartItems = useSelector(state => Object.values(state.cart))
    let subTotal = allCartItems.reduce((accumulator, currentValue) => accumulator + (currentValue.item.price * currentValue.quantity),
        0,)
    let tax = subTotal * 0.043
    tax = parseFloat(tax.toFixed(2))
    const total = subTotal + tax

    const checkout=()=>{
        if(allCartItems[0]){
            allCartItems.map(ele=>dispatch(deleteCartItem(ele.id)))
            alert("Thank you for shopping with us")
            history.push('/login')

        }
        else{
            alert("You have nothing to checkout")

        }
    }
    return (
        <div className='bagDiv'>
            <div>
                <p>Bags</p>
                {!allCartItems[0] && <p>Your bag  is empty</p>}
                {user = ! null && allCartItems.map(ele =>
                    <div className='mainLeft'>
                        <div className='cartImgDiv'>
                            <img src={ele.item.image} className='cartImg'/>
                        </div>
                        <div className='cartDetailDiv'>
                            <p className='cartP'>{ele.item.sports} {ele.item.category}</p>
                            <p className='cartP'>{ele.size}</p>
                            <p className='cartP'>${ele.item.price}</p>
                            <div className='cartQuantity'>
                            <p>Quantity</p>
                            <select id="dropdown" value={ele.quantity} data-value={ele.id} onChange={updateQuantity} className='dropDown'>
                                {choice.map(num =>
                                    <option value={num}>{num}</option>
                                )}
                            </select>

                            </div>
                            <i class="fas fa-trash-alt" onClick={deleteI} data-value={ele.id}></i>
                        </div>
                    
                    </div>
                )}
            </div>
            <div>                
                <p className='sumarry'>Summary</p>
                <div className='subTotal'>
                <p >SubTotal</p>
                <p>${subTotal}</p>
                    </div>   
                    <div className='tax'>
                <p >Extimated Tax</p>
                <p>${tax}</p>
                        </div>             
                <hr></hr>
                <div className='total'>
                <p >Total</p>
                <p>${total}</p>
                </div>
                <button className='checkout' onClick={checkout}>Checkout</button>
            </div>

        </div>
    )
}

export default CartComponent;