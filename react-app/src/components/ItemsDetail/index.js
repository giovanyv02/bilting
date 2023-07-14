import { useSelector, useDispatch } from 'react-redux';
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

function ItemDetail(){
const itemId = parseInt(useParams().itemId)
const item = useSelector(state=> state.items[itemId])
const shoeSizes = ['M 3.5 / W 5', 'M 5.5 / W 7', 'M 10.5 / W 12', 'M 15 / W 14.5' ]
const [size, setSize] = useState("")



const updateSize = (e)=> setSize(e.target.dataset.value)

 return (
    <div>
        <div className='imgDiv'>
            <img src={item.images[0].url}/>
        </div>
        <div className='detailDiv'>
            <p>{item.sports} {item.category}</p>
            <p>{item.price}</p>
            <p>Select size</p>
            {shoeSizes.map(shoeSize=>
                <button onClick={updateSize} data-value={shoeSize}>{shoeSize}</button>
                )}
            <button>Add to bag</button>
        </div>
    </div>
 )
}
export default ItemDetail;