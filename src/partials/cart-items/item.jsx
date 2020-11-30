import React from "react";
import $ from "jquery";
import axios from "axios";

class Item extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      deleted: false,
      id: this.props.obj.id,
    };
    //this.handleClick = this.handleClick.bind(this);
  }
  // handleClick() {

  //   let endpoint = process.env.REACT_APP_ENDPOINT_USER_CART;
  //   let key = localStorage.getItem("token");
  //   let cart_id = this.props.obj.id;
  //   //let value = e.target.value;
  //   axios
  //     .delete(endpoint.concat(cart_id + "/"), {
  //       headers: { Authorization: `Token ${key}` },
  //     })
  //     .then((response) => {
  //       if (response.status === 204) {
  //         this.setState({ deleted: true });
  //       }
  //     });
  // }

  handleClick = (e) => {
    console.log(e.target.value);
  };

  //  componentDidMount() {
  //   this.handleClick()
  //  }

  render() {
    let deleted = this.state.deleted;
    let purchased = localStorage.getItem('purchased');
    let on_stock = this.props.obj.on_stock;
    return (
      <>
      <div>
        {on_stock === true ? 
        <>
        <small className="dropdown-item">
          {this.props.obj.item_name}{" "}
          <span style={{ paddingLeft: "5px" }} className="text-info" id="obj">
            {this.props.obj.item_price} {" "}
          </span>
          <button
            className="text-warning"
            onClick={() => this.props.onDelete(this.props.obj.id)}
            value={this.props.obj.id}
           
          >
            X {this.props.obj.id}
          </button>
        </small>
       
        <div className="dropdown-divider"></div>
        
        </>
        :
        null}
       
     
      </div>
   
    
      </>
    );
  }
}

export default Item;
