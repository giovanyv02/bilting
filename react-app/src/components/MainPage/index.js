import React, { useState, useEffect } from "react";
import Carousel from "react-multi-carousel";
import 'react-multi-carousel/lib/styles.css';
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


function MainPage(props) {
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(allItems())
    }, [dispatch]);

    useEffect(() => {
        dispatch(allReviews())
    }, [dispatch])

    const responsive = {
        superLargeDesktop: {
            // the naming can be any, depends on you.
            breakpoint: { max: 4000, min: 3000 },
            items: 5
        },
        desktop: {
            breakpoint: { max: 3000, min: 1024 },
            items: 3
        },
        tablet: {
            breakpoint: { max: 1024, min: 464 },
            items: 2
        },
        mobile: {
            breakpoint: { max: 464, min: 0 },
            items: 1
        }
    }



    return (
        <div className="mainPageDiv">
            <NavLink exact to='/new-arrival' className="newArrival"><p >Shop new Arrival</p></NavLink>
            
            <div >
                <p className="shopBySport">Shop by sport</p>
                <div className="sportDiv">
                    <Carousel swipeable={false}
                        draggable={false}
                        showDots={true}
                        responsive={responsive}
                        ssr={true} // means to render carousel on server-side.
                        infinite={true}
                        autoPlay={props.deviceType !== "mobile" ? true : false}
                        autoPlaySpeed={4000}
                        keyBoardControl={true}
                        customTransition="all .5"
                        transitionDuration={500}
                        containerClass="carousel-container"
                        removeArrowOnDeviceType={["tablet", "mobile"]}
                        deviceType={props.deviceType}
                        dotListClass="custom-dot-list-style"
                        itemClass="carousel-item-padding-40-px">

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
                                <img src={nikeRunning} id='nikeR' alt="nikeR" className="sportImage" />
                                <p>Nike Running</p>
                                <p>Everything you'll need for every mile.</p>
                                <p>Shop</p>

                            </NavLink>
                        </div>
                        <div className="singleSport">
                            <NavLink to='tennis'>
                                <img src={nikeTennis} id='nikeT' alt="nikeT" className="sportImage" />
                                <p>Nike Tennis</p>
                                <p>Serve up in style</p>
                                <p>Shop</p>

                            </NavLink>
                        </div>
                        <div className="singleSport">
                            <NavLink to='football'>
                                <img src={nikeFootball} id='nikeF' alt="nikeF" className="sportImage" />
                                <p>Nike Football</p>
                                <p>Show up and show out the latest gridiron gear.</p>
                                <p>Shop</p>

                            </NavLink>
                        </div>
                        <div className="singleSport">
                            <NavLink to='soccer'>
                                <img src={nikeSoccer} id='nikeS' alt="nikeS" className="sportImage" />
                                <p>Nike Soccer</p>
                                <p>Let your inner Messi comes out.</p>
                                <p>Shop</p>

                            </NavLink>
                        </div>
                    </Carousel>
                </div>
            </div>
        </div>
    )
}

export default MainPage;