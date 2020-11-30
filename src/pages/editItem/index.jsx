import React from "react";
import axios from "axios";
import { Redirect, withRouter } from "react-router-dom";
//import queryString from "query-string"
import Header from "../../partials/header/index";
//import './style.css';

class EditItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: "",
      title: "",
      price: "",
      merchant_email: "",
      description: "",
      product_image: "",
      errors: {
        title: "",
        description: "",
        price: "",
      },
      updated: false,
    };
  }

  getData = () => {
    let slug = this.props.match.params.slug;
    let endpoint = process.env.REACT_APP_ENDPOINT_USER_ITEMS;
    let key = localStorage.getItem("token");
    axios
      .get(endpoint.concat(slug + "/"), {
        headers: { Authorization: `Token ${key}` },
      })
      .then((response) => {
        this.setState({
          id: response.data.id,
          title: response.data.title,
          price: response.data.price,
          description: response.data.description,
          merchant_email: response.data.merchant_email,
          product_image: response.data.product_image,
        });
      });
  };

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
    //let id = localStorage.getItem("pk");
    const data = {
      title: this.state.title,
      description: this.state.description,
      price: this.state.price,
      //merchant: id,
    };

    const axiosConfig = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    let slug = this.props.match.params.slug;
    let endpoint = process.env.REACT_APP_ENDPOINT_ITEM_DISPLAY;
    let token = localStorage.getItem("token");
    axios
      .patch(endpoint.concat(slug + "/"), data, {
        headers: { Authorization: `Token ${token}` },
      })
      .then((response) => {
        const status = response.status;

        if (status === 200) {
          this.setState({ updated: true });
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
  componentDidMount() {
    this.getData();
  }
  render() {
    const id = this.state.id;
    const title = this.state.title;
    const price = this.state.price;
    const product_image = this.state.product_image;
    const description = this.state.description;
    const merchant_email = this.state.merchant_email;
    const { errors } = this.state;
    const updated = this.state.updated;
    let slug = this.props.match.params.slug;
    let user_email = localStorage.getItem("user_email");
    if (updated) {
      window.location = `/item/edit/${slug}`;
    }

    return (
      <>
        <Header />
        <section key={id}>
          <div className="container wrapper">
            <div className="row  align-items-center mt-5">
              <div className="col-sm-7">
                <h3 className="text-primary">{title}</h3>
                <p>Product ID: {id}</p>
                <p>Price: € {price}</p>
                <p>Description: {description}</p>
                <p>Seller: {merchant_email}</p>
              </div>
              <div className="col-sm-5">
                <img src={product_image} alt="image" />
              </div>
            </div>
          </div>
        </section>
        {merchant_email === user_email ? (
          <section className="container my-5">
            <h5>Edit your Product</h5>
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
                  <button type="submit" className="btn btn-outline-warning btn-lg btn-block">
                    Update
                  </button>
                </div>
              </div>

              <div id="formMsg" className="text-danger">
                <label htmlFor=""></label>
              </div>
            </form>
          </section>
        ) : null}
      </>
    );
  }
}

export default withRouter(EditItem);
