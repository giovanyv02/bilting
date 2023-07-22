import React, { useState } from "react";
import { login } from "../../store/session";
import { NavLink } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import './LoginForm.css';

function LoginFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const demoUser = (e)=>{
    e.preventDefault();
    dispatch(login("demo@aa.io", "password"))
  }

  return (
    <>
    <div className="signDiv">

      <h1>Log In</h1>
      <form onSubmit={handleSubmit} className="signForm">
        <ul>
          {errors.map((error, idx) => (
            <li key={idx} className="err">{error} </li>
          ))}
        </ul>
        <div>

        <label>
          
          <input
          placeholder="Email"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="createAccountInput"
          />
        </label>
        </div>
        <div>

        <label>
         
          <input
          placeholder="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="createAccountInput"
          />
        </label>
        </div>
        <div className="buttons">

        <button type="submit" className="signUpButton">Log In</button>
      <button className="demoUser" onClick={demoUser}>Demo User</button>
        </div>
      </form>
    </div>
    </>
  );
}

export default LoginFormPage;
