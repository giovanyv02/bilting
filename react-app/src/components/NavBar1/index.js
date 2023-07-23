import "./navbar1.css"
import jordan from "../../images/jordan.png"
import converse from "../../images/converse.png"
import { NavLink, Redirect } from 'react-router-dom';
import OpenModalButton from "../OpenModalButton";
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
                <NavLink to={{pathname:"https://www.nike.com/retail"}} target="_blank" className='findStore'>Find a store</NavLink>
                <p className="nav1P">|</p>
                {sessionUser && <p className="hiUser">Hi {sessionUser.firstName}</p>}
                {!sessionUser &&  <NavLink to='/signup'>Join Us</NavLink>}
                <p className="nav1P">|</p>
                {!sessionUser &&<NavLink to='/login'>Sign In</NavLink>}
                
                
            </div>
        </div>
      
        </div>
            
    )
}