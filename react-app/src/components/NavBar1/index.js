import "./navbar1.css"
import jordan from "../../images/jordanlogo.png"
import converse from "../../images/converselogo.png"
import { NavLink, Redirect } from 'react-router-dom';
import OpenModalButton from "../OpenModalButton";
import SignupFormModal from "../SignupFormModal";
import LoginFormModal from "../LoginFormModal";
import ProfileButton from "../Navigation/ProfileButton";
import { useSelector } from "react-redux";

export default function Navbar1(){
    const sessionUser = useSelector(state => state.session.user);

    return(
        <div className="mainNav1">
        <div className="nav1">
            <div className="divImg">
                <img src={jordan} alt="jordan" className="jordan nav1img"/>
                <img src={converse} alt="converse" className="converse nav1img"/>
            </div>
            <div className="divText">
                <NavLink to='/nike.com/retail' className='findStore'>Find a store</NavLink>
                <p className="nav1P">|</p>
                {sessionUser && <p className="hiUser">Hi {sessionUser.firstName}</p>}
                {!sessionUser &&   <OpenModalButton buttonText='Join us'className='nav1ModalButton' modalComponent={<SignupFormModal />} ></OpenModalButton>}
                <p className="nav1P">|</p>
                {!sessionUser && <OpenModalButton buttonText='Sign In' className='nav1ModalButton' modalComponent={<LoginFormModal />}></OpenModalButton>}
                
                
            </div>
        </div>
        <hr></hr>
        </div>
            
    )
}