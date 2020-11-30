import React from "react";
import { Link } from 'react-router-dom'
import './style.css';
const Nav = () => (
  <div className="mb-2 bg--nav card-4 border-top border-bottom">
    <nav className="nav nav-justified">
    <Link className="nav-item nav-link secondary--text" to="/shop">
      Shop
    </Link>
    <Link className="nav-item nav-link secondary--text" to="/">
      Link
    </Link>
    <Link className="nav-item nav-link secondary--text" to="/">
      Link
    </Link>
    <Link className="nav-item nav-link secondary--text" to="/hats">
      Disabled
    </Link>
  </nav>


  </div>
  
);

export default Nav;
