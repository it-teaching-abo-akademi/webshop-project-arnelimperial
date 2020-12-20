import React from "react";
import { Link } from "react-router-dom";
//import Nav from "./nav";
import axios from "axios";
//import FontAwesome from "react-fontawesome";
//import faStyles from "font-awesome/css/font-awesome.css";
import logo from "../../files/crown.svg";
import "./style.css";

class HeaderHome extends React.Component {
  constructor(props) {
    super(props);
    //this.UserData = this.UserData.bind(this);
    this.state = {
      user: "",
      userId: "",
      isLogged: false,
    };
  }

  componentDidMount() {
    const key = localStorage.getItem("token");

    if (key) {
      const endpoint_getUser = process.env.REACT_APP_ENDPOINT_USER;

      axios
        .get(endpoint_getUser, { headers: { Authorization: `Token ${key}` } })
        .then((response) => {
          localStorage.setItem("user", response.data.username);
          localStorage.setItem("pk", response.data.pk)
          if (response.status === 200) {
            this.setState({
              user: response.data.username,
              userId: response.data.pk,
              isLogged: true,
            });
          }
        })
        .catch((errors) => {
          console.log(errors);
        });
    }
  }

  render() {
    return (
      <>
        <div className="pt-3 py-1 header--background">
          <div className="container">
            <header className="row justify-content-between py-1">
              <div className="col-4 py-1">
                <Link
                  to="/"
                  className="text-white logo"
                  style={{ textDecoration: "none" }}
                >
                  <img src={logo} alt="Crown" />
                </Link>
              </div>
              <div className="col-4 mt-3">
                {this.state.isLogged && (
                  <Link to="/shop" className="primary--text font-weight-bold">
                    <span key={this.state.userId}>
                      Hi! {this.state.user}
                    </span>
                  </Link>
                )}
               
              </div>
            </header>
          </div>
        </div>
      </>
    );
  }
}

export default HeaderHome;
