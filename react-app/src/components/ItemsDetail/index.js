import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { theCart, addCartItem } from '../../store/cartReducer';


function ItemDetail() {

    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(theCart())
        
    }, [dispatch]);

    
    const itemId = parseInt(useParams().itemId)
    const item = useSelector(state => state.items[itemId])
    const allCartItems = useSelector(state=>Object.values(state.cart))
    const allCartItemIds = allCartItems.map(ele=> ele.itemId)
    console.log("all cart items",allCartItems)
    console.log("all cart itemsId",allCartItemIds)

    const userId = useSelector(state=> state.session.user.id)
    const shoeSizes = ['M 3.5 / W 5', 'M 5.5 / W 7', 'M 10.5 / W 12', 'M 15 / W 14.5']
    const choice = [0,1,2,3,4,5,6,7]
    const [run, setRun] = useState(false) 
    const [size, setSize] = useState("")
    const [quantity, setQuantity] = useState(0)
    const [validationErrors, setValidationErrors] = useState({});
    
    
    const err = {}
    if(!size) err['size'] = 'Please select a size'
    if(!quantity) err['quantity'] = 'Please select a quantity'
    let newCartItem = {}
    if(!Object.values(err).length){
        newCartItem = {
            "quantity": parseInt(quantity),
            "item_id": itemId,
            "cart_id": userId
        }
    }

    
    
    useEffect(()=>{
        if(run && Object.values(newCartItem).length > 2){
            if(allCartItemIds.includes(itemId)){
               const cartItemToUpdate = allCartItems.filter(ele => ele.itemId === itemId && ele.item.size === size)
                if(cartItemToUpdate[0]){
                    console.log("lala")
                    setRun(false)
                }else{
                    dispatch(addCartItem(newCartItem))
                    setRun(false)
                }

            }else{
                dispatch(addCartItem(newCartItem))
                setRun(false)

            }
        }
    },[dispatch, run])

    const updateSize = (e) => setSize(e.target.dataset.value)
    const updateQuantity = (e)=> setQuantity(e.target.value)
   
   

    const onSubmit = (e)=>{
        setValidationErrors(err);
        e.preventDefault();

        if(!Object.values(err).length){
            setRun(true)
        }
    }
    return (
        <div>
            <div className='imgDiv'>
                <img src={item.images[0].url} />
            </div>
            <div className='detailDiv'>
                <p>{item.sports} {item.category}</p>
                <p>{item.price}</p>
                <p>Select size</p>
                {shoeSizes.map(shoeSize =>
                    <button onClick={updateSize} data-value={shoeSize}>{shoeSize}</button>
                )}
                <p>Quantity</p>
                <select id="dropdown"  onChange={updateQuantity}>
                    {choice.map(num=>
                        <option  value={num}>{num}</option>
                        )}
                </select>
                <button disabled={!userId} onClick={onSubmit}>Add to bag</button>


            </div>
        </div>
    )
}
export default ItemDetail;