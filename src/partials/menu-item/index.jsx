import React from "react";
import { withRouter } from "react-router-dom";

import "./style.scss";

//Renders navigation menu
const MenuItem = ({ title, imageUrl, size, linkUrl, history, match }) => (
  <div
    style={{ backgroundImage: `url(${imageUrl})` }}
    className={`menu--background img-responsive card-4 text-center mt-1 ${size}`}
     //Go to shop page
    onClick={() => history.push('/shop')}
    //Go to respective menu categories
    // onClick={() => history.push(`${match.url}${linkUrl}`)}
  >
    {" "}
    <div className="container">
      <div className="content mt-5 pb-2 mb-3 border bg-light">
        <h5 className="text-center text-black title py-1">{title.toUpperCase()}</h5>
        <small className="text-center text-white bg-dark border border--nav-index px-1 py-1 card-4 subtitle">
          SHOP NOW
        </small>
      </div>
    </div>
  </div>
);

export default withRouter(MenuItem);
