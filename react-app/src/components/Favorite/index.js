import { useSelector, useDispatch } from 'react-redux';
import { theFav } from '../../store/favoriteReducer';
import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { NavLink } from 'react-router-dom';

function FavoritesItemsPage(){
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

            dispatch(theFav())
        }

    }, [dispatch]);

    

    const allFavItems = useSelector(state=> Object.values(state.favorite))
    console.log(allFavItems)
   

    
   
    
    return (
        <>
            <p className='pLength'>My Favorites({allFavItems.length})</p>
        <div className='allItemsDiv'>
            {allFavItems.map(ele=>
            <NavLink to={`/items/${ele.id}`}>

                <div className='itemsDiv'>
                    <div className='imgDiv'>
                       
                        <img src={ele.item.image} className='allImg'/>
                    </div>
                    <div>
                        <p>{ele.item.sports}</p>
                        <p>{ele.item.sex} {ele.category}</p>
                        <p>${ele.item.price}</p>
                    </div>
                </div>
            </NavLink>
                )}
        </div>
        </>
    )
}
export default FavoritesItemsPage;