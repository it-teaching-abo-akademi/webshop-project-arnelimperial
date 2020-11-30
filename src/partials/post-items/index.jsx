import React from "react";
import { Link, Redirect } from "react-router-dom";
import axios from "axios";
import "./style.css";
//import { data } from "jquery";

class DisplayItems extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      item: "",
      items: [],
      isAuthed: false,
      //wrongItem: "",
      err: false,
      created: false,
      
    };

    this.handleClick = this.handleClick.bind(this);
  }


  handleClick = (e) => {
    //console.log('Old: ', e.target.value);
    this.setState({ item: e.target.value }, () => {
      //console.log('New: ', this.state.id)
      const data = {
        item: this.state.item,
      };
      let endpoint = process.env.REACT_APP_ENDPOINT_CART;
      let key = localStorage.getItem("token");
      axios
        .post(endpoint, data, {
          headers: { Authorization: `Token ${key}` },
        })

        .then((response) => {
          this.setState({
            items: [...response.data.results],
          });
          if (response.status == 201) {
            this.setState({
              created: true,
            });
          }
          if (this.state.created) {
            <Redirect to="/myitems" />;
          }
        })
        .catch((error) => {
          console.log(error);
          if (error.response) {
            // error.response.data
            this.setState({ err: true });
          } else {
            this.setState({ created: true });
          }
        });
    });
  };

  toLogin = () => {
    return (
      <button className="btn btn-sm btn-info pt-1">
        <Link to="/login" className="text-white">
          Add to cart
        </Link>
      </button>
    );
  };

  outOfStock = () => {
    return (
      <button
        className="btn btn-sm btn-danger mt-2"
        type="button"
        disabled
      >
        Out of Stock
      </button>
    );
  };

  addToCart = () => {
    return (
      <>
        <button
          className="btn btn-sm btn-primary mt-2"
          type="button"
          value={this.props.obj.id}
          onClick={this.handleClick}
        >
          Add to cart
        </button>
      </>
    );
  };

  sellersItemBtn = () => {
    return (
      <button
        className="btn btn-sm btn-light mt-2 text-info"
        type="button"
        disabled
      >
        Seller's item
      </button>
    );
  };

  render() {
    const auth = localStorage.getItem("user");
    const user_email = localStorage.getItem("user_email");
    const err = this.state.err;
    const created = this.state.created;
   

    let wmsg;
    let rmsg;
    if (err) {
      wmsg = (
        <span className="text-danger">
          Invalid! Can't add your own merchandise.
        </span>
      );
    }
    if (created) {
      window.location = "/shop";
      rmsg = (
        <span className="text-success">
          Valid! Item added to your cart. Add more.
        </span>
      );
    }
    return (
      <>
        <div className="row mt-5">
          {rmsg}
          {wmsg}
         
          <div className="col-sm-6" style={{ paddingRight: "0" }}>
            <small className="font-weight-bold" style={{ padding: "0" }}>
              <Link to={`/item/${this.props.obj.slug}`}>
                Name: {this.props.obj.title}
              </Link>
            </small>
            <br />
            <small style={{ display: "inline" }}>
              <span className="font-weight-bold">Description: </span>
              {this.props.obj.description}
            </small>
            <br />
            <small className="font-weight-bold">
              {this.props.obj.merchant_email === user_email ? (
                <span className="text-danger">
                  Seller: {this.props.obj.merchant_email}
                </span>
              ) : (
                <>
                  Seller:
                  <span className="text-primary">
                    {" "}
                    {this.props.obj.merchant_email}
                  </span>
                </>
              )}
            </small>
            <br />
            <small className="font-weight-bold">
              Price:{" "}
              <span className="text-info">&euro; {this.props.obj.price}</span>
              </small>
                
            <div>
           
              {(auth &&
              this.props.obj.merchant_email !== user_email && this.props.obj.on_stock === true) 
                ? this.addToCart()
                : null}

              {(auth && this.props.obj.merchant_email === user_email)
                ? this.sellersItemBtn()
                : null}

              {(!auth && this.props.obj.on_stock === true) && this.toLogin()}

              {(this.props.obj.on_stock === false && auth) && this.outOfStock()}

              {(this.props.obj.on_stock === false && !auth) && this.outOfStock()}
            </div>
          </div>

          <div className="col-sm-6">
            <img
              className="pt-2"
              src={this.props.obj.product_image}
              alt="Image"
            />
          </div>
        </div>
      </>
    );
  }
}

export default DisplayItems;
