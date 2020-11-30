import React from "react";
import { Link } from "react-router-dom";
import Nav from "./nav";
import FontAwesome from "react-fontawesome";
import faStyles from "font-awesome/css/font-awesome.css";
import logo from "../../files/crown.svg";
//import { useLocation } from "react-router-dom";
import CartItems from "../cart-items/index";
import $ from "jquery";
import "./style.css";
import Axios from "axios";

class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLogged: false,
      user: "",
      fadeOut: false,
      search_text: "",
      search: [],
      slug: "",
    };
  }
  getUser = () => {
    const u = localStorage.getItem("user");
    if (u && localStorage.length > 0) {
      this.setState({ isLogged: true, user: u });
    }
  };
  componentDidMount() {
    this.getUser();
  }

  fadeOut = () => {
    this.setState({ fadingOut: true });
    $(".basket").click(function () {
      $("body").not(".dropdown-menu").addClass("blur");
    });

    // $('.dropdown-toggle').on('click', function(event) {
    //   $('.dropdown-menu').slideToggle();
    //   event.stopPropagation();
    // });

    // $('.dropdown-menu').on('click', function(event) {
    //   event.stopPropagation();
    // });

    // $(window).on('click', function() {
    //   $('.dropdown-menu').slideUp();
    // });
  };

  handleChange = (e) => {
    this.setState({ search_text: e.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    let endpoint = process.env.REACT_APP_ENDPOINT_ITEM_SEARCH;
    let key = process.env.REACT_APP_INITIAL_KEY;
    
    Axios.get(endpoint.concat(this.state.search_text), {
      headers: { Authorization: `Token ${key}` },
    }).then((response) => {
      this.setState({ search: [...response.data.results] });
      let search = this.state.search;
      let slug = search.map((i) => i.slug);
      window.location = `/item/${slug}`;
    });
  };

  render() {
    //const location = this.props.location.pathname;
    //const { isLogged, user } = this.state;

    return (
      <>
        <div className="pt-3 py-1 header--background">
          <div className="container">
            <header className="header--container">
              <div>
                <Link
                  to="/"
                  className="text-white logo"
                  style={{ textDecoration: "none" }}
                >
                  <img src={logo} alt="web logo" />
                </Link>
              </div>

              <div className="header--search">
                <form
                  method="GET"
                  encType="multipart/form-data"
                  onSubmit={this.handleSubmit}
                >
                  <div className="input-group input-group-md">
                    <input
                      type="text"
                      className="form-control"
                      style={{ borderRadius: "0.8em" }}
                      value={this.state.search_text}
                      onChange={this.handleChange}
                    />
                    <FontAwesome
                      className="search--btn position-absolute pl-1"
                      name="search"
                    />
                  </div>
                </form>
              </div>
              <div>
                {this.state.isLogged ? (
                  <>
                    <Link
                      className="pl-2 secondary--text"
                      style={{ textDecoration: "none", fontSize: "2vw" }}
                      to="/"
                    >
                      {this.state.user}
                    </Link>
                    <ul className="nav header--nav__ul">
                      <li className="nav-item">
                        <Link
                          className="nav-link secondary--text header--nav"
                          activeclassname="invisible"
                          to="/account"
                        >
                          Change Password
                        </Link>
                      </li>
                      <li className="nav-item">
                        <Link
                          className="nav-link secondary--text header--nav"
                          activeclassname="invisible"
                          to="/myitems"
                        >
                          My Items
                        </Link>
                      </li>
                      <li className="nav-item">
                        <Link
                          className="nav-link secondary--text header--nav"
                          activeclassname="active"
                          to="/logout"
                        >
                          Logout
                        </Link>
                      </li>
                      <li className="nav-item dropdown">
                        <FontAwesome
                          name="shopping-basket"
                          className="basket nav-link secondary--text header--nav dropdown-toggle"
                          data-toggle="dropdown"
                          aria-expanded="false"
                          aria-haspopup="true"
                          onClick={this.fadeOut}
                          id="btnid"
                        />

                        <CartItems />
                      </li>
                    </ul>
                  </>
                ) : (
                  <ul className="nav header--nav__ul py-2">
                    <li className="nav-item">
                      <Link
                        className="nav-link secondary--text header--nav"
                        activeclassname="active"
                        to="/signup"
                      >
                        SignUp
                      </Link>
                    </li>
                    <li className="nav-item pl-3">
                      <Link
                        className="nav-link secondary--text header--nav"
                        activeclassname="active"
                        to="/login"
                      >
                        SignIn
                      </Link>
                    </li>
                  </ul>
                )}
              </div>
            </header>
          </div>
        </div>

        <Nav />
      </>
    );
  }
}

export default Header;
