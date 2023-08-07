import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import MainPage from "./components/MainPage";
import ItemsPage from "./components/AllItem";
import ItemDetail from "./components/ItemsDetail";
import CartComponent from "./components/Cart";
import FavoritesItemsPage from "./components/Favorite";
import AllReviews from "./components/Review/AllReview";
import Navbar1 from "./components/NavBar1";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
    <Navbar1 />
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path='/cart'>
            <CartComponent />
          </Route>
          <Route path='/favorite'>
            <FavoritesItemsPage />
          </Route>
          <Route path='/reviews/:itemId'>
            <AllReviews />
          </Route>
          <Route exact path="/" >
            <MainPage />
          </Route>
        <Route exact path='/items/:itemId'>
          <ItemDetail />
        </Route>
        <Route path='/:newId'>
        <ItemsPage />
        </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
