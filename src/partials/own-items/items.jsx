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
              Name: {this.props.obj.title}
            </small>
            <br />
            <small style={{ display: "inline" }}>
              <span className="font-weight-bold">Description: </span>
              {this.props.obj.description}
            </small>
            <br />
            <small className="font-weight-bold">
              Seller ID:{" "}
              <span className="text-primary">{this.props.obj.merchant}</span>
            </small>
            <br />
            <small className="font-weight-bold">
              Price:{" "}
              <span className="text-info">&euro; {this.props.obj.price}</span>
            </small>
            <br/>
            <button className="btn btn-sm btn-warning mt-2">
              <Link to={`/item/edit/${this.props.obj.slug}`} className="text-white">
               Edit
              </Link>
            </button>
          </div>

          <div className="col">
            <img className="pt-2" src={this.props.obj.product_image} alt="" />
          </div>
        </div>
      </>
    );
  }
}

export default Items;
