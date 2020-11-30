import React from "react";
import axios from "axios";
import { Redirect } from "react-router-dom";
import { withRouter } from "react-router";
import Header from "../../partials/header/index";
import PasswordMask from "react-password-mask";

class Account extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      old_password: "",
      new_password1: "",
      new_password2: "",
      isLogout: false,
      errors: {
        old_password: "",
        new_password1: "",
        new_password2: "",
      },
    };
  }

  handleChange = (event) => {
    event.preventDefault();
    const { name, value } = event.target;
    let errors = this.state.errors;
    let new_password1 = this.state.new_password1;
    switch (name) {
      case "old_password":
        errors.old_password = value.length < 5 ? "" : "Invalid password";
        break;
      case "new_password1":
        errors.new_password1 = value.length < 5 ? "Invalid password." : "";
        break;
      case "new_password2":
        errors.new_password2 =
          value === new_password1 ? "Password do not match." : "";
        break;
      default:
        break;
    }

    this.setState({ errors, [name]: value });
  };

  //   resetPassword(data) {
  //     return fetch(url, {
  //       method: "POST",
  //       body: JSON.stringify(data),
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //     })
  //       .then((res) => res.json())
  //       .then((apiResponse) => {
  //         console.log("api response", apiResponse);
  //         return {
  //           type: "REGISTER_USER",
  //           api_response: apiResponse.data,
  //         };
  //       })
  //       .catch(function (error) {
  //         return {
  //           type: "REGISTER_USER",
  //           api_response: { success: false },
  //         };
  //       });
  //   }

  handleSubmit = (event) => {
    event.preventDefault();

    const data = {
      old_password: this.state.old_password,
      new_password1: this.state.new_password1,
      new_password2: this.state.new_password2,
    };

    const endpoint_reset = process.env.REACT_APP_ENDPOINT_PASSWORD_RESET;
    const access_token = localStorage.getItem("token");
    axios
      .post(endpoint_reset, data, {
        headers: { Authorization: `Token ${access_token}` },
      })
      .then((response) => {
        const status = response.status;
        if (status === 200) {
          localStorage.clear();
        }
      })
      .then((response) => {
        window.location.reload(false);
      });
  };

  logOut = () => {
    localStorage.clear();
    this.setState({ isLogout: true });
  };

  render() {
    const { errors, isLogout } = this.state;
    if (isLogout) {
      return <Redirect to="login" />;
    }

    return (
      <>
        <Header />
        <main className="container">
          <div className="mt-5">
            <section
              style={{
                border: "10px solid rgb(65, 52, 52)",
              }}
              className="px-3 mb-5"
            >
              <h3 className="my-4">Account Settings: Reset Password</h3>
              <small className="text-secondary border border-info px-2 py-2">
                This will auto logout your session.
              </small>
              <form
                method="POST"
                onSubmit={this.handleSubmit}
                encType="multipart/form-data"
                className="my-5"
              >
                {/* <CSRFToken /> */}

                <div className="form-group font-weight-bold">
                  <label
                    className="control-label col-sm-2"
                    htmlFor="old_password"
                  >
                   Password
                  </label>
                  <div className="col-sm-10">
                    <PasswordMask
                      type="password"
                      value={this.state.old_password}
                      name="old_password"
                      placeholder="Current Password"
                      onChange={this.handleChange}
                      noValidate
                      useVendorStyles={false}
                      inputClassName="form-control"
                    />
                    {errors.old_password.length < 5 && (
                      <p className="pt-2 text-danger">{errors.old_password}</p>
                    )}
                  </div>
                </div>

                <div className="form-group font-weight-bold">
                  <label
                    className="control-label col-sm-2"
                    htmlFor="new_password1"
                  >
                    New Password
                  </label>
                  <div className="col-sm-10">
                    <PasswordMask
                      type="password"
                      value={this.state.new_password1}
                      name="new_password1"
                      placeholder="Enter new password"
                      onChange={this.handleChange}
                      noValidate
                      useVendorStyles={false}
                      inputClassName="form-control"
                    />
                    {errors.new_password1.length < 5 && (
                      <p className="pt-2 text-danger">{errors.new_password1}</p>
                    )}
                  </div>
                </div>
                <div className="form-group font-weight-bold">
                  <label
                    className="control-label col-sm-6"
                    htmlFor="new_password12"
                  >
                    New Password Again
                  </label>
                  <div className="col-sm-10">
                    <PasswordMask
                      type="password"
                      value={this.state.new_password2}
                      name="new_password2"
                      placeholder="Repeat new password"
                      onChange={this.handleChange}
                      noValidate
                      useVendorStyles={false}
                      inputClassName="form-control"
                    />
                    {errors.new_password2.length < 5 && (
                      <p className="pt-2 text-danger">{errors.new_password2}</p>
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
                    Save
                  </button>
                </div>
              </div>

                <div className="container">
                  <small id="formMsg" className="text-danger"></small>
                  <small id="sMsg" className="text-success"></small>
                </div>
              </form>
            </section>
          </div>
        </main>
      </>
    );
  }
}

export default withRouter(Account);
