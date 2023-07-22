import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import firstImage from "../../images/firstImage.webp"
import NikeBasket from "../../images/nikeBasket.webp"
import nikeFootball from "../../images/nikeFootball.webp"
import nikeRunning from "../../images/nikeRunning.webp"
import nikeTennis from "../../images/nikeTennis.webp"
import nikeSoccer from "../../images/nikeSoccer.webp"
import nikem from "../../images/nikeMember.webp"
import { NavLink, Redirect } from 'react-router-dom';
import { allItems } from "../../store/itemReducer";
import "./mainpage.css"
import { allReviews } from "../../store/review";


function MainPage(){
    const dispatch = useDispatch();
    useEffect(()=>{
        dispatch(allItems())
    }, [dispatch]);

    useEffect(()=>{
        dispatch(allReviews())
    }, [dispatch])

    

   
    return (
        <div className="mainPageDiv">
            <NavLink exact to='/new-arrival' className="newArrival"><p >Shop new Arrival</p></NavLink>
            <div className="firstImageDiv">

            <img src={firstImage} id='firstImage' alt="firstImage" className="firstImage"/>
            </div>
            {/* <p>Become a nike Membership</p>
            <div className="nikeMemberDiv">
                <imag src={nikem} id='member' alt='nikemember' className="nikeMember"/>
            </div> */}
            <div className="shopBySport">
                <p>Shop by sport</p>
                <div className="sportDiv">
                    <div className="singleSport">
                        <NavLink to='/basket'>
                       <img src={NikeBasket} id='nikeB' alt="nikeB" className="sportImage" /> 
                       <p>Nike Basketball</p>
                       <p>Stlyle made for your game</p>
                       <p>Shop</p>

                        </NavLink>
                    </div>
                    <div className="singleSport">
                        <NavLink to='/running'>
                    <img src={nikeRunning} id='nikeR' alt="nikeR" className="sportImage"/> 
                       <p>Nike Running</p>
                       <p>Everything you'll need for every mile.</p>
                       <p>Shop</p>

                        </NavLink>
                    </div>
                    <div className="singleSport">
                        <NavLink to='tennis'>
                    <img src={nikeTennis} id='nikeT' alt="nikeT" className="sportImage"/> 
                       <p>Nike Tennis</p>
                       <p>Serve up in style</p>
                       <p>Shop</p>

                        </NavLink>
                    </div>
                    <div className="singleSport">
                        <NavLink to='football'>
                    <img src={nikeFootball} id='nikeF' alt="nikeF" className="sportImage"/> 
                       <p>Nike Football</p>
                       <p>Show up and show out the latest gridiron gear.</p>
                       <p>Shop</p>

                        </NavLink>
                    </div>
                    <div className="singleSport">
                        <NavLink to='soccer'>
                    <img src={nikeSoccer} id='nikeS' alt="nikeS" className="sportImage"/> 
                       <p>Nike Soccer</p>
                       <p>Let your inner Messi comes out.</p>
                       <p>Shop</p>

                        </NavLink>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default MainPage;