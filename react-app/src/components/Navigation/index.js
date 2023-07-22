import React, {useState} from 'react';
import { useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import nikeLogo from '../../images/nikeLogo.jpg'
import { theCart } from '../../store/cartReducer';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	  const user = useSelector(state => state.session.user)
	  const cart = useSelector(state=> Object.values(state.cart))
	  const [run, setRun] = useState(true)

    const dispatch = useDispatch();
   
        if (user && !cart[0] && run) {
            dispatch(theCart())
			setRun(false)

        }
		let quantity
		if(cart[0]){
			quantity = cart.reduce((a,b)=> a + b.quantity, 0)
		}


    

	return (
		<div className='nav2'>
			<div className='nikelogo'>

				<NavLink exact to="/">
					<img src={nikeLogo} alt='nikeLogo' className='nikeLogo'/>
				</NavLink>
			</div>
			<div className='nav2Text'>
				<NavLink to='/man'>Men</NavLink>
				<NavLink to='/women'>Women</NavLink>
				<NavLink to='/kid'>Kid</NavLink>
			</div>

			<div className='cartDiv'>
			<NavLink exact to="/cart">
			<i class="fas fa-cart-arrow-down">{quantity && quantity}</i>
			</NavLink>
			{sessionUser && (
				
					<ProfileButton user={sessionUser} />
				
			)}

			</div>
			
		</div>
	);
}

export default Navigation;