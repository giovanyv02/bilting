import { useSelector, useDispatch } from 'react-redux';
import { allItems } from "../../store/itemReducer";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import './allItem.css'
import { NavLink } from 'react-router-dom';

function ItemsPage(){
    const dispatch = useDispatch();
    useEffect(()=>{
        dispatch(allItems())
    }, [dispatch]);

    const allitems = useSelector(state=> Object.values(state.items))
    const sort = useParams().newId
    let items = allitems.filter(item=> item.sex === sort)
    if (!items[0]){
        items = allitems.filter(item => item.sports === sort)
        if(!items[0]){
            items = allitems.filter(item=> item.featured === 'new arrival')
        }
    }
    if (!allitems) return null
   
    
    return (
        <>
            <p className='pLength'>{sort}({items.length})</p>
        <div className='allItemsDiv'>
            {items.map(ele=>
            <NavLink to={`/items/${ele.id}`}>

                <div className='itemsDiv'>
                    <div className='imgDiv'>
                       
                        <img src={ele.images[0].url} className='allImg'/>
                    </div>
                    <div>
                        <p>{ele.sports}</p>
                        <p>{ele.sex} {ele.category}</p>
                        <p>${ele.price}</p>
                    </div>
                </div>
            </NavLink>
                )}
        </div>
        </>
    )
}
export default ItemsPage;