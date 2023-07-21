import { deleteReview } from "../../../store/review";
import { useDispatch, useSelector} from "react-redux";
import { useModal } from "../../../context/Modal";
import "./deleteReview.css"

export default function DeleteReview({id}){
    const { closeModal } = useModal();
    
    const dispatch = useDispatch();
    
    
    const subDelete = ()=>{
        dispatch(deleteReview(id));
         closeModal()
       
    };

    const subNo = ()=>{
        closeModal()
    }

   
    return(
        <>
        <div className="delDiv">

        <h3 className="delH3">Delete</h3>
        <p className="delP"> Remove this review</p>
        <button onClick={subDelete} className="delYes">Continue</button>
        <button onClick={subNo} type="submit" className="delNo">Cancel</button>
        </div>
        
        </>
    )
}