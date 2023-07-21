import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../../context/Modal";
import { reviewUpdate } from "../../../store/review";
import nikeWhite from "../../../images/whiteLogo.png"


export default function UpdateReview({ id }) {
  const { closeModal } = useModal();
  const review = useSelector(state => state.reviews[id])
  console.log("men reviewwww", review)
  const [text, setText] = useState(review.review);
  const [activeRating, setActiveRating] = useState(review.stars);
  const [sub, setSub] = useState(false);
  const dispatch = useDispatch();

  let klik = false
  useEffect(() => {
    if (sub) {
      const nR = { "review": text, "stars": activeRating, "item_id": id }

      dispatch(reviewUpdate(id, nR));
      closeModal()

    }
  })
  const submitRev = () => {
    setSub(true);
  }
  return (
    <>
      <div className="createReviewDiv">

        
          <h3>Review</h3>
          <img src={nikeWhite} className="revLogo"/>


        
        
          <textarea placeholder={review.review} onChange={(e) => setText(e.target.value)} className="reviewTextArea"></textarea>

      
        <div className="stars" >
          <div
            className={activeRating >= 1 ? "filled" : "empty"}
            onMouseEnter={() => {
              if (!klik) setActiveRating(1);
            }}
            onMouseLeave={() => {
              if (!klik) setActiveRating(0);
            }}
            onClick={() => {
              klik = !klik
            }}
          >
            <i className="fas fa-star revStar" ></i>
          </div>
          <div
            className={activeRating >= 2 ? "filled" : "empty"}
            onMouseEnter={() => {
              if (!klik) setActiveRating(2);
            }}
            onMouseLeave={() => {
              if (!klik) setActiveRating(0);
            }}
            onClick={() => {
              klik = !klik
            }}
          >
            <i className="fas fa-star revStar"></i>
          </div>
          <div
            className={activeRating >= 3 ? "filled" : "empty"}
            onMouseEnter={() => {
              if (!klik) setActiveRating(3);
            }}
            onMouseLeave={() => {
              if (!klik) setActiveRating(0);
            }}
            onClick={() => {
              klik = !klik
            }}
          >
            <i className="fas fa-star revStar"></i>
          </div>
          <div
            className={activeRating >= 4 ? "filled" : "empty"}
            onMouseEnter={() => {
              if (!klik) setActiveRating(4);
            }}
            onMouseLeave={() => {
              if (!klik) setActiveRating(0);
            }}
            onClick={() => {
              klik = !klik
            }}
          >
            <i className="fas fa-star revStar"></i>
          </div>
          <div
            className={activeRating >= 5 ? "filled" : "empty"}
            onMouseEnter={() => {
              if (!klik) setActiveRating(5);
            }}
            onMouseLeave={() => {
              if (!klik) setActiveRating(0);
            }}
            onClick={() => {
              klik = !klik
            }}
          >
            <i className="fas fa-star revStar"></i>
          </div>
          
        </div>
        <div>
          <button disabled={text.length < 10 || !activeRating} onClick={submitRev} className="submitReviewButton">Update your review</button>
        </div>
      </div>



    </>
  )
}