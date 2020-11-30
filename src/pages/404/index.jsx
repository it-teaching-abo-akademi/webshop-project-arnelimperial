import React from "react";
import { Link } from "react-router-dom";
import Header from "../../partials/header/index";
import './style.css';

const NotFound = () => (
  <>
    <Header />

    <div className="mx-auto mt-5 px-4" style={{width:"500px",height:"auto"}}>
      <h1>Not Found.</h1>

      <p>The thing you're trying to get to doesn't exist.</p>
      <p>
        Maybe you'd be better off at the <Link to="/">Home page</Link> or <Link to="/shop">Shop page</Link>.
      </p>
    </div>
  </>
);

export default NotFound;
