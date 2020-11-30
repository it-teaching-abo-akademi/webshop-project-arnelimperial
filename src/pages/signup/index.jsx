import React from "react";
import axios from "axios";
import Header from "../../partials/header/index";
import { Redirect } from "react-router-dom";
//import CSRFToken from "../../partials/csrf/csrf";
import EmailRegex from "../../partials/validators/email";
import { fromBase64 } from "js-base64";
import PasswordMask from "react-password-mask";

class SignUp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      email: "",
      password1: "",
      password2: "",
      created: false,
      errors: {
        username: "",
        email: "",
        password1: "",
        password2: "",
      },
    };
  }

  handleChange = (event) => {
    event.preventDefault();
    const { name, value } = event.target;
    let errors = this.state.errors;
    const password1 = this.state.password1;

    switch (name) {
      case "username":
        errors.username =
          value.length < 4 ? "Username must at least 4 chars." : "";
        break;
      case "email":
        errors.email = EmailRegex.test(value) ? "" : "Email not valid!";
        break;
      case "password1":
        errors.password1 =
          value.length < 5 ? "Password must at least 5 chars." : "";
        break;
      case "password2":
        errors.password2 = value !== password1 ? "Password do not match." : "";
        break;
      default:
        break;
    }

    this.setState({ errors, [name]: value });
  };

  handleSubmit = (event) => {
    event.preventDefault();

    const data = {
      username: this.state.username,
      email: this.state.email,
      password1: this.state.password1,
      password2: this.state.password2,
    };

    const loginName = data.username;

    const axiosConfig = {
      headers: {
        "Content-Type": "application/json",
      },
      auth: {
        username: data.username,
        email: data.email,
        password1: data.password1,
        password2: data.password2,
      },
    };

    const endpoint_signup = process.env.REACT_APP_ENDPOINT_SIGNUP;

    axios
      .post(endpoint_signup, data, axiosConfig)
      .then((response) => {
        const status = response.status;
        localStorage.setItem("user", data.username);
        localStorage.setItem("user_email", data.email);

        localStorage.setItem("token", response.data.key);
        if (status === 201 && localStorage.user === data.username) {
          this.setState({ created: true });
          let successmsg = document.querySelector("#sMsg");
          successmsg.innerHTML = `Hi! ${loginName}, welcome to Nutrsrx Shop.`;
          setTimeout(function () {
            window.location = "/";
          }, 200);
        }
      })
      .catch((error) => {
        let errormsg = document.querySelector("#formMsg");
        errormsg.innerHTML = `Sorry ${loginName}, there was an error. Maybe your are registered here before.`;
      });

    this.setState({
      username: "",
      email: "",
      password1: "",
      password2: "",
    });
  };

  render() {
    const { errors, created } = this.state;

    return (
      <>
        <Header />

        <div className="container pt-3" style={{marginBottom:"5rem"}}>
          <section
            className="mt-5 pl-3 py-5"
            style={{ border: "7px solid rgb(65, 52, 52)" }}
          >
            <h3>Sign Up</h3>
            <form
              method="POST"
              onSubmit={this.handleSubmit}
              encType="multipart/form-data"
              className="py-2"
            >
              {errors ? (
                <div className="container mt-2 mb-5 mx-2">
                  <p id="formMsg" className="text-danger"></p>
                </div>
              ) : (
                ""
              )}
              {created ? (
                <div className="container mt-2 mb-5 mx-2">
                  <p id="sMsg" className="text-success"></p>
                </div>
              ) : (
                ""
              )}

              <div className="form-group font-weight-bold">
                <label className="control-label col-sm-2" htmlFor="username">
                  Username
                </label>
                <div className="col-sm-10">
                  <input
                    type="text"
                    value={this.state.username}
                    name="username"
                    placeholder="Min. 4 chars."
                    className="form-control"
                    onChange={this.handleChange}
                    noValidate
                  />
                  {errors.username.length > 0 && (
                    <p className="pt-2 text-danger">{errors.username}</p>
                  )}
                </div>
              </div>

              <div className="form-group font-weight-bold">
                <label className="control-label col-sm-2" htmlFor="email">
                  Email
                </label>
                <div className="col-sm-10">
                  <input
                    type="email"
                    value={this.state.email}
                    name="email"
                    placeholder="Email"
                    className="form-control"
                    onChange={this.handleChange}
                    noValidate
                  />
                  {errors.email.length > 0 && (
                    <p className="pt-2 text-danger">{errors.email}</p>
                  )}
                </div>
              </div>
              <div className="form-group font-weight-bold">
                <label className="control-label col-sm-2" htmlFor="password1">
                  Password
                </label>
                <div className="col-sm-10">
                  <PasswordMask
                    type="password"
                    value={this.state.password1}
                    name="password1"
                    placeholder="Min. 5 chars."
                    onChange={this.handleChange}
                    noValidate
                    useVendorStyles={false}
                    inputClassName="form-control"
                  />
                  {errors.password1.length > 0 && (
                    <p className="pt-2 text-danger">{errors.password1}</p>
                  )}
                </div>
              </div>

              <div className="form-group font-weight-bold">
                <label className="control-label col-sm-2" htmlFor="password2">
                  Repeat Password
                </label>
                <div className="col-sm-10">
                  <PasswordMask
                    type="password"
                    value={this.state.password2}
                    name="password2"
                    placeholder="Confirm your password."
                    onChange={this.handleChange}
                    noValidate
                    useVendorStyles={false}
                    inputClassName="form-control"
                  />
                  {errors.password2.length > 0 && (
                    <p className="pt-2 text-danger">{errors.password2}</p>
                  )}
                </div>
              </div>

              <div className="form-group pt-2">
                <div className="col-sm-offset-2 col-sm-10">
                  <button
                    type="submit"
                    name="submit"
                    className="btn btn-outline-info btn-lg btn-block"
                  >
                    Sign Up
                  </button>
                </div>
              </div>
            </form>
          </section>
        </div>
      </>
    );
  }
}

export default SignUp;


