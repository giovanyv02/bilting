import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import OpenModalButton from "../../OpenModalButton";
import CreateReview from "../CreateReview";
import UpdateReview from "../updateReview";
import DeleteReview from "../DeleteReview";
import { allReviews } from "../../../store/review";
import "./allReview.css"


const AllReviews = () => {
    const itemid = parseInt(useParams().itemId)
    const dispatch = useDispatch();
    const item = useSelector(state => state.items[itemid])
    const user = useSelector(state => state.session.user)
    let userid;
    if (user) userid = user.id
    const allreview = useSelector(state => Object.values(state.reviews))
    const reviews = allreview.filter(ele => ele.itemId === itemid)
    const userReview = reviews.filter(ele => ele.userId == userid)

    useEffect(() => {
        dispatch(allReviews())
    }, [dispatch])

    return (
        <div>
            <div className="createReviewButton">
            {!userReview[0] && <OpenModalButton
                buttonText="Create a review"
                modalComponent={<CreateReview id={itemid} />}
            />}

            </div>

            {reviews.map(ele =>
                <div className="allRevDiv">
                    <p className="userName">{ele.user.lastName} {ele.user.firstName}</p>
                    <p className="reviewDate">{ele.createdAt.split(" ").slice(1,4).join(" ")}</p>
                    <div className="stars">
                        <div
                            className={ele.stars >= 1 ? "filled" : "empty"}      >
                            <i className="fas fa-star revStar" ></i>
                        </div>
                        <div
                            className={ele.stars >= 2 ? "filled" : "empty"}      >
                            <i className="fas fa-star revStar"></i>
                        </div>
                        <div
                            className={ele.stars >= 3 ? "filled" : "empty"}      >
                            <i className="fas fa-star revStar" ></i>
                        </div>
                        <div
                            className={ele.stars >= 4 ? "filled" : "empty"}      >
                            <i className="fas fa-star revStar"></i>
                        </div>
                        <div
                            className={ele.stars >= 5 ? "filled" : "empty"}      >
                            <i className="fas fa-star revStar" ></i>
                        </div>

                    </div>
                    <p className="rev">{ele.review}</p>
                    {ele.userId === userid && <OpenModalButton
                        buttonText={<i class="fas fa-edit"></i>}
                        className="editRevButton"
                        modalComponent={<UpdateReview id={ele.id} className="a"/>}
                    />}
                    
                    {ele.userId === userid && <OpenModalButton
                        buttonText={<i class="fas fa-trash"></i>}
                        modalComponent={<DeleteReview id={ele.id} />}
                    />}
                    <hr></hr>
                    <hr></hr>

                </div>
            )}
        </div>
    )
}
export default AllReviews