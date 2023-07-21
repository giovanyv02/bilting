import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [errors, setErrors] = useState({});

  let err = {};
  if (!email) err['email'] = 'email is required'
  if (!username) err['username'] = 'username is required'
  if (!email.includes('@')) err['email'] = 'valid email is required'
  if (firstName.length < 4) err['firstName'] = 'firstName is too short'
  if (lastName.length < 4) err['lastName'] = 'lastName is too short'
  if (password.length < 6) err['password'] = 'password is password needs to at least 6 characters'
  if (password !== confirmPassword) err['confirmPassword'] = 'confirmPassword and password need to match'



  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors(err)
    console.log(errors)
    if (!Object.values(err).length) {
      const data = await dispatch(signUp(username, email, password, firstName, lastName));
      if (data) {
        setErrors(data)
      }
    }
  };

  return (
    <>
      <div className="signDiv">

        <h1>Now let's make you a Nike Member.</h1>
        <form onSubmit={handleSubmit} className="signForm">
          {/* <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul> */}
          <div>
            <label>

              <input
                type="text"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="createAccountInput"
              />
            </label>
            {errors.email && <p className="err">{errors.email}</p>}

          </div>
          <div>

            <label>

              <input
                placeholder="Username"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}

                className="createAccountInput"
              />
            </label>
            {errors.username && <p className="err">{errors.username}</p>}
          </div>
          <div className="firstLastDiv">
            <div>

              <label>

                <input
                  placeholder="First Name"
                  type="text"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  required
                  className="createAccountInput"
                />
              </label>
              {errors.firstName && <p className="firstLast" >{errors.firstName}</p>}
            </div>
            <div>

              <label>

                <input
                  placeholder="Last Name"
                  type="text"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  required
                  className="createAccountInput"
                />
              </label>
              {errors.lastName && <p className="firstLast">{errors.lastName}</p>}
            </div>
          </div>
          <div>

          <label>

            <input
              placeholder="Password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="createAccountInput"
            />
          </label>
          {errors.password && <p className="err">{errors.password}</p>}
          </div>
        <div>

          <label>

            <input
              placeholder="Confirm Password"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
              className="createAccountInput"
            />
          </label>
          {errors.confirmPassword && <p className="err">{errors.confirmPassword}</p>}
        </div>

          <button type="submit" className="signUpButton">Create Account</button>
        </form>
      </div>
    </>
  );
}

export default SignupFormPage;
