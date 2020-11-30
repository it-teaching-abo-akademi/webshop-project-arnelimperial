import React from "react";
import axios from "axios";
import { withRouter } from "react-router-dom";
//import queryString from "query-string"
import Header from "../../partials/header/index";
import "./style.css";

class SingleItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: "",
      title: "",
      price: "",
      merchant_email: "",
      description: "",
      product_image: "",
      created_date: "",
      updated_date: "",
      on_stock: "",
    };
  }

  getData = () => {
    let slug = this.props.match.params.slug;
    let endpoint = process.env.REACT_APP_ENDPOINT_ITEM_DISPLAY;
    let key = process.env.REACT_APP_INITIAL_KEY;
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
          created_date: response.data.created_date,
          updated_date: response.data.updated_date,
          on_stock: response.data.on_stock,
        });
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
    const created = this.state.created_date;
    const updated = this.state.updated_date;
    const on_stock = this.state.on_stock;

    return (
      <>
        <Header />
        <section key={id}>
          <div className="container wrapper">
            <div className="row  align-items-center mt-5">
              <div className="col-sm-7">
                {title && <h3 className="text-primary">{title}</h3>}
                {id && <p>Product ID: {id}</p>}
                {price && <p>Price: € {price}</p>}
                {description && <p>Description: {description}</p>}
                {merchant_email && <p>Seller: {merchant_email}</p>}
                {created && <p>Created: {created}</p>}
                {updated && <p>Updated: {updated}</p>}
                {on_stock === true && (<p>Availability: In stock</p>)}
                {on_stock === false && (<p>Availability: Out of stock</p>)}
                
              </div>
              <div className="col-sm-5">
                {product_image && (
                  <img src={product_image} alt="product image" />
                )}
              </div>
            </div>
          </div>
        </section>
      </>
    );
  }
}

export default withRouter(SingleItem);
