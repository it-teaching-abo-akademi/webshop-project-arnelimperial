import React from "react";
import axios from "axios";
//import CSRFToken from "../../partials/csrf/csrf";
import Header from '../../partials/header/index';

export default class Logout extends React.Component {
 

  handleClick = (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    const access_token = token;
    const endpoint = process.env.REACT_APP_ENDPOINT_AUTH_LOGOUT;
    axios
      .post(endpoint, {
        headers: { Authorization: `Token ${access_token}` },
      })
      .then((res) => {
        localStorage.removeItem("token");
        localStorage.removeItem("user");
        localStorage.removeItem("init");
        localStorage.removeItem("pk");
        localStorage.removeItem("user_email");
        localStorage.removeItem("user_email");
        localStorage.removeItem("purchased");


        
        this.setState({ isLogout: true });
        const status = res.status;
        if (status === 200) {
          window.location = "/";
        }
      })
      .catch((err) => console.log(err));
  };

  render() {
    return (
      <>
      <Header />
      <div className="container mt-5">
        <div className="mx-5" style={{border:"10px solid rgb(65, 52, 52)"}}>
          <div className="mx-auto mt-5 px-5 pb-5" style={{width:"500px",height:"auto"}}>
            <h3 className="h3">Logout</h3>
            <p>Are you sure you want to sign out?</p>
            <form method="POST">
              {/* <CSRFToken /> */}
              <button onClick={this.handleClick} type="submit" className="btn btn-lg btn-danger">
                Submit
              </button>
            </form>
          </div>
        </div>
      </div>
      </>
    );
  }
}
