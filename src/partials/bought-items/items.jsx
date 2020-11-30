import React from "react";
import { Link } from "react-router-dom";
import "./style.css";

class Items extends React.Component {
  render() {
    return (
      <>
        <div className="row mt-5">
          <div className="col" style={{ paddingRight: "0" }}>
            <small className="font-weight-bold" style={{ padding: "0" }}>
              Name: {this.props.obj.purchased_item_name}
            </small>
            <br />
            <small style={{ display: "inline" }}>
              <span className="font-weight-bold">Description: </span>
              {this.props.obj.purchased_item_description}
            </small>
            <br />
            <small className="font-weight-bold">
              Seller:{" "}
              <span className="text-primary">{this.props.obj.sellers}</span>
            </small>
            <br />
            <small className="font-weight-bold">
              Buyer:{" "}
              <span className="text-primary">{this.props.obj.buyer_username}</span>
            </small>
            <br />
            <small className="font-weight-bold">
              Price:{" "}
              <span className="text-info">&euro; {this.props.obj.purchases_price}</span>
            </small>
            <br/>
            
          </div>

          <div className="col">
            <img className="pt-2" src={this.props.obj.purchased_item_product_image} alt="product image" />
          </div>
        </div>
      </>
    );
  }
}

export default Items;
