import React from "react";
import Directory from "../../partials/directory/index";
import { Link } from "react-router-dom";
import axios from "axios";
import "./style.css";

import HeaderHome from "../../partials/header/index.home";

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      active_users: "",
      product_count: "",
      init: false,
      name: "",
    };
  }
  componentDidMount() {
    // Count active users
    const endpoint1 = process.env.REACT_APP_ENDPOINT_USERS_COUNT;
    //const endpoint1 = process.env.REACT_APP_ENDPOINT_AUTH_USERS
    const key = process.env.REACT_APP_INITIAL_KEY;

    axios
      .get(endpoint1, { headers: { Authorization: `Token ${key}` } })
      .then((response) => {
        if (response.status === 200) {
          this.setState({ active_users: response.data.active_users });
          
        }
      })
      .catch((error) => {
        console.log(error);
      });

    // Count products
    //const endpoint2 = process.env.REACT_APP_ENDPOINT_PRODUCTS_COUNT;
    const endpoint2 = process.env.REACT_APP_ENDPOINT_ITEM_DISPLAY
    axios
      .get(endpoint2, { headers: { Authorization: `Token ${key}` } })
      .then((response) => {
        if (response.status === 200) {
          this.setState({ product_count: response.data.count });
         
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }

  handleSubmit(event) {
    event.preventDefault();
    // Delete users and generate new one
    const endpoint_init = process.env.REACT_APP_ENDPOINT_INITIAL;
    const key = process.env.REACT_APP_INITIAL_KEY;
    const i = "initialize";
    const data = {
      name: i,
    };
    axios
      .post(endpoint_init, data, {
        headers: {
          Authorization: `Token ${key}`,
        },
      })
      .then((response) => {
        if (response.status === 201) {
          localStorage.setItem("init", "Restart!");
          window.location = "/";
        }
      });
  }

  render() {
    const init = localStorage.getItem("init");
    let display;
    if (!init) {
      display = (
        <>
           <p className="mt-3">Goto Shop</p>
          <form method="POST" onSubmit={this.handleSubmit}>
            <button
              className="btn btn-primary"
              type="text"
              name="name"
              value={this.state.name}
            >
              Delete all items and generate 6 new users and 30 new items.
            </button>
          </form>
          <h5 className="mt-3">
            N.B.: By going to the store you accept our terms and conditions
          </h5>
          <Link to="/shop">Go to Shop</Link>
        </>
      );
    } else {
      display = (
        <>
          <h5>Goto Shop</h5>
          <p>N.B.: By going to the store you accept our terms and conditions</p>
          <h5 className="text-info font-weight-bold">
            Database items Generated!
          </h5>
        </>
      );
    }
    return (
      <>
        <HeaderHome />
        <div className="container">
          <Directory />
        </div>
        <div className="container mt-5 px-5" style={{ marginBottom: "10rem" }}>
          <div className="card">
            <div className="card-body">
              <h4 className="card-title">Info</h4>
              <h5>Dynamic Info</h5>
              <p className="card-text">
                Our page has{" "}
                <span className="text-info font-weight-bold">
                  {this.state.product_count}
                </span>{" "}
                items with{" "}
                <span className="text-info font-weight-bold">
                  {this.state.active_users}
                </span>{" "}
                active users currently.
              </p>

              {display}
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default Home;

{
  /* <p className="mt-3">Goto Shop</p>
<p>N.B.: By going to the store you accept our terms and conditions</p>
<Link to="/shop">Go to shop</Link> */
}
