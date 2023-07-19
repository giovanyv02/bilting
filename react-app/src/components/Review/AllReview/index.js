import React, {useState, useEffect} from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { NavLink } from 'react-router-dom/cjs/react-router-dom.min';
import OpenModalButton from "../../OpenModalButton";
import CreateReview from "../CreateReview";
import UpdateReview from "../updateReview";
import DeleteReview from "../DeleteReview";
import { allReviews } from "../../../store/review";


const AllReviews = ()=>{
    const itemid = parseInt(useParams().itemId)
    const dispatch = useDispatch();
    const item = useSelector(state => state.items[itemid])
    const user = useSelector(state=> state.session.user)
    let userid;
    if(user) userid = user.id 
    const allreview = useSelector(state=> Object.values(state.reviews))
    const reviews = allreview.filter(ele=> ele.itemId === itemid)
    const userReview = reviews.filter(ele=>ele.userId == userid)

    useEffect(()=>{
        dispatch(allReviews())
    },[dispatch])

    return (
        <div>
            {!userReview[0] &&  <OpenModalButton 
           buttonText="Create a review"
            modalComponent={<CreateReview id={itemid} />}
           />}
          
            {reviews.map(ele=>
                <div>
                    <p>{ele.stars}</p>
                    <p>{ele.review}</p>
                    <p>{ele.createdAt}</p>
                    {ele.userId === userid && <OpenModalButton 
                    buttonText='update Review'
                    modalComponent={<UpdateReview id={ele.id}/>}
                    />}
                     {ele.userId === userid && <OpenModalButton 
                    buttonText='delete Review'
                    modalComponent={<DeleteReview id={ele.id} />}
                    />}
                    
                </div>
                )}
        </div>
    )
}
export default AllReviews