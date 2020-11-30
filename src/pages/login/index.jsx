import React from "react";
import axios from "axios";
import Header from "../../partials/header/index";
//import { useHistory } from "react-router";
import { Redirect } from "react-router-dom";
//import csrftoken from "./csrf";
//import Redirect from "../../components/redirect";
//import { encode } from "js-base64";
//import CSRFToken from "../../partials/csrf/csrf";
//import Cookies from "js-cookie";
import PasswordMask from "react-password-mask";

const validEmailRegex = RegExp(
  /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
);

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      password: "",
      isLogged: false,
      errors: {
        email: "",
        password: "",
      },
    };
  }

  handleChange = (event) => {
    event.preventDefault();
    const { name, value } = event.target;
    let errors = this.state.errors;

    switch (name) {
      case "email":
        errors.email = validEmailRegex.test(value)
          ? ""
          : "Credential not valid!";
        break;
      case "password":
        errors.password = value.length < 2 ? "Invalid password." : "";
        break;
      default:
        break;
    }

    this.setState({ errors, [name]: value });
  };

  handleSubmit = (event) => {
    event.preventDefault();

    const data = {
      email: this.state.email,
      password: this.state.password,
    };
    localStorage.setItem("user_email", data.email);

    const loginName = data.email;

    const axiosConfig = {
      headers: {
        "Content-Type": "application/json",
      },
      auth: {
        email: data.email,
        password: data.password,
      },
    };

    const endpoint_login = process.env.REACT_APP_ENDPOINT_AUTH_LOGIN;

    axios
      .post(endpoint_login, data, axiosConfig)
      .then((response) => {
        const token = response.data.key;
        localStorage.setItem("token", token);

        const status = response.status;
        if (status === 200 && localStorage.length > 0) {
          window.location = "/";
          this.setState({ isLogged: true });
        }
      })
      .catch((error) => {
        let errormsg = document.querySelector("#formMsg");
        errormsg.innerHTML = `Sorry ${loginName}, there was an error. Try to login again.`;
      });
  };

  render() {
    const { errors, isLogged } = this.state;
    if (isLogged) {
      return <Redirect to="/" />;
    }

    return (
      <>
        <Header />

        <div className="container pt-3">
          <section
            className="mt-5 pl-3 py-5"
            style={{ border: "7px solid rgb(65, 52, 52)" }}
          >
            <h3>Sign In</h3>
            <form
              method="POST"
              onSubmit={this.handleSubmit}
              encType="multipart/form-data"
              className="form-horizontal py-3"
            >
              <div className="form-group font-weight-bold">
                <label className="control-label col-sm-2" htmlFor="email">
                  Email
                </label>
                <div className="col-sm-10">
                  <input
                    type="text"
                    value={this.state.email}
                    name="email"
                    placeholder="Email"
                    onChange={this.handleChange}
                    className="form-control"
                    noValidate
                  />
                  {errors.email.length > 0 && (
                    <p className="pt-2 text-danger">{errors.email}</p>
                  )}
                </div>
              </div>

              <div className="form-group mb-3 font-weight-bold">
                <label htmlFor="pwd" className="control-label col-sm-2">
                  Password
                </label>
                <div className="col-sm-10">
                  <PasswordMask
                    type="password"
                    value={this.state.password}
                    name="password"
                    placeholder="Password"
                    onChange={this.handleChange}
                    noValidate
                    useVendorStyles={false}
                    inputClassName="form-control"
                  />
                  {errors.password.length > 0 && (
                    <p className="pt-2 text-danger">{errors.password}</p>
                  )}
                </div>
              </div>

              <div className="form-group">
                <div className="col-sm-offset-2 col-sm-10">
                  <button type="submit" className="btn btn-outline-info btn-lg btn-block">
                    Sign In
                  </button>
                </div>
              </div>

              <div id="formMsg" className="text-danger">
                <label htmlFor=""></label>
              </div>
            </form>
          </section>
        </div>
      </>
    );
  }
}

export default Login;
