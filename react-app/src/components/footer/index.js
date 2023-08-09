import React from "react"
import { NavLink } from "react-router-dom"
import "./footer.css"
function FooterComponent() {
    return (
        <>
            <div className="footer-container">
                <div>
                    <p className="footerP">Technologies used</p>
                    <div className="tech">
                        <i class="fa-brands fa-react"></i>
                        <i class="fa-brands fa-js"></i>
                        <i class="fa-brands fa-python"></i>
                        <i class="fa-brands fa-css3-alt"></i>
                    </div>
                </div>
                <div>
                    <p className="footerP">Contact me</p>
                    <div className="contact">
                        <NavLink to={{ pathname: "https://giovanyv02.github.io/" }} target="_blank" className='findStore'>My Portfolio</NavLink>
                        <NavLink to={{ pathname: "https://github.com/giovanyv02" }} target="_blank" className='findStore'><i class="fa-brands fa-github"></i></NavLink>
                        <NavLink to={{ pathname: "https://www.linkedin.com/in/giovany-victor-33226a266/" }} target="_blank" className='findStore'><i class="fa-brands fa-linkedin"></i></NavLink>
                        <NavLink to={{ pathname: "https://wellfound.com/u/giovany-victor" }} target="_blank" className='findStore'><i class="fa-brands fa-angellist"></i></NavLink>
                        <i class="fa-regular fa-envelope" >victorgiovany02@gmail.com</i>


                    </div>
                </div>




            </div>
        </>
    )
}

export default FooterComponent