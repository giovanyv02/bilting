import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import nikeLogo from '../../images/nikeLogo.jpg'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

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
			<i class="fas fa-cart-arrow-down"></i>
			</NavLink>
			{sessionUser && (
				
					<ProfileButton user={sessionUser} />
				
			)}

			</div>
			
		</div>
	);
}

export default Navigation;