import React from "react";
import axios from "axios";

class AddItemForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "",
      description: "",
      price: "",
      created: false,
      errors: {
        title: "",
        description: "",
        price: "",
      },
    };
  }

  handleChange = (event) => {
    event.preventDefault();
    const { name, value } = event.target;
    let errors = this.state.errors;

    switch (name) {
      case "title":
        errors.title =
          value.length < 4 ? "Char length from 4 - 60 allowed." : "";
        break;
      case "description":
        errors.description =
          value.length < 8 ? "Char length from 8 - 53 allowed." : "";
        break;
      case "price":
        errors.price =
          value.length < 1 ? "Only numbers and comma accepted." : "";
        break;
      default:
        break;
    }

    this.setState({ errors, [name]: value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    let id = localStorage.getItem("pk");
    const data = {
      title: this.state.title,
      description: this.state.description,
      price: this.state.price,
      merchant: id,
    };

    const axiosConfig = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const endpoint = process.env.REACT_APP_ENDPOINT_ITEM_DISPLAY;
    const token = localStorage.getItem("token");
    axios
      .post(endpoint, data, { headers: { Authorization: `Token ${token}` } })
      .then((response) => {
        const status = response.status;

        if (status === 201) {
          this.setState({ created: true });
          window.location = "/myitems";
        }
      })
      .catch((error) => {
        let errormsg = document.querySelector("#formMsg");
        errormsg.innerHTML = "There was an error. Please try again.";
      });

    this.setState({
      title: "",
      description: "",
      price: "",
    });
  };

  render() {
    const { errors } = this.state;
    return (
      <>
        <section className="mt-5">
          <h3>Add Product</h3>
          <form
            method="POST"
            onSubmit={this.handleSubmit}
            encType="multipart/form-data"
            className="form-horizontal"
          >
            <div className="form-group font-weight-bold">
              <label className="control-label col-sm-2" htmlFor="title">
                Title
              </label>
              <div className="col-sm-10">
                <input
                  type="text"
                  value={this.state.title}
                  name="title"
                  placeholder="Max. char length 60"
                  onChange={this.handleChange}
                  className="form-control"
                  noValidate
                />
                {errors.title.length > 0 && (
                  <p className="pt-2 text-danger">{errors.title}</p>
                )}
              </div>
            </div>

            <div className="form-group mb-3 font-weight-bold">
              <label htmlFor="price" className="control-label col-sm-2">
                Price
              </label>
              <div className="col-sm-10">
                <input
                  type="text"
                  value={this.state.price}
                  name="price"
                  placeholder="Only numbers and comma accepted"
                  onChange={this.handleChange}
                  className="form-control"
                  noValidate
                />

                {errors.price.length > 0 && (
                  <p className="pt-2 text-danger">{errors.price}</p>
                )}
              </div>
            </div>
            <div className="form-group mb-3 font-weight-bold">
              <label htmlFor="description" className="control-label col-sm-2">
                Description
              </label>
              <div className="col-sm-10">
                <textarea
                  className="form-control"
                  rows="3"
                  type="number"
                  value={this.state.description}
                  name="description"
                  placeholder="Max. char length 53"
                  onChange={this.handleChange}
                  className="form-control"
                  noValidate
                ></textarea>
                {errors.description.length > 0 && (
                  <p className="pt-2 text-danger">{errors.description}</p>
                )}
              </div>
            </div>

            <div className="form-group">
              <div className="col-sm-offset-2 col-sm-10">
                <button type="submit" className="btn btn-outline-success btn-lg btn-block">
                  Submit
                </button>
              </div>
            </div>

            <div id="formMsg" className="text-danger">
              <label htmlFor=""></label>
            </div>
          </form>
        </section>
      </>
    );
  }
}

export default AddItemForm;
