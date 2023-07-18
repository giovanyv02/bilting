import React, {useState, useEffect} from "react";
import {useHistory} from "react-router-dom";
import { useDispatch, useSelector} from "react-redux";
import { useModal } from "../../../context/Modal";
import { addReview } from "../../../store/review";
import './review.css'

export default function CreateReview({id}){
    const {closeModal} = useModal();
    const [activeRating, setActiveRating] = useState(0);
    const [text, setText] = useState("");
    const [sub, setSub] = useState(false);
    const history = useHistory();
    const dispatch = useDispatch();

    let klik = false
    useEffect(()=>{
        if(sub){
            const nR = {"review": text, "stars":activeRating, "item_id":id}
            
            dispatch(addReview(nR));
            closeModal()
            
        }
    })
    const submitRev = ()=>{
        setSub(true);
    }
    return(
        <>
        <div >

        <div>
        <h3>Review</h3>

        </div>
        <div>
            <textarea placeholder="Leave your review here" onChange={(e)=>setText(e.target.value)}></textarea>

        </div>
        <div >
      <div
        className={activeRating >= 1 ? "filled" : "empty"}
        onMouseEnter={() => {
         if(!klik)  setActiveRating(1);
        }}
        onMouseLeave={() => {
          if(!klik) setActiveRating(0);
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
         if(!klik) setActiveRating(2);
        }}
        onMouseLeave={() => {
            if(!klik) setActiveRating(0);
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
            if(!klik) setActiveRating(3);
        }}
        onMouseLeave={() => {
            if(!klik) setActiveRating(0);
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
            if(!klik)  setActiveRating(4);
        }}
        onMouseLeave={() => {
            if(!klik) setActiveRating(0);
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
            if(!klik)  setActiveRating(5);
        }}
        onMouseLeave={() => {
            if(!klik)   setActiveRating(0);
        }}
        onClick={() => {
            klik = !klik
        }}
      >
        <i className="fas fa-star revStar"></i>
      </div>
      <h5>stars</h5>
    </div>
        <div>
            <button  disabled={text.length < 10 || !activeRating} onClick={submitRev}>Submit your review</button>
        </div>
        </div>

        
        
        </>
    )
    
}
// class ReviewForm(FlaskForm):
//     itemId = IntegerField("ItemId", validation=[DataRequired])
//     userId = IntegerField("UserId")
//     review = StringField("Review", validation=[DataRequired])
//     stars = IntegerField("Stars", validation=[DataRequired])
//     reviewImage = StringField("ReviewImage")