import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div>
			<div>

				<NavLink exact to="/">Home</NavLink>
			</div>
			<div>
				Man
				Women
				Kid
			</div>
			<NavLink exact to="/cart">Bag</NavLink>

			<div>
			{isLoaded && (
				
					<ProfileButton user={sessionUser} />
				
			)}

			</div>
			
		</div>
	);
}

export default Navigation;