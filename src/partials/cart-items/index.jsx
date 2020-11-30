import React from "react";
import axios from "axios";
import Item from "./item";
//import $ from "jquery";

class CartItems extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      item: "",
      boughtItems: [],
      items: [],
      purchases: [],
      bill: "",
      itemID: "",
      deleted: false,
      purchased: false,
      stock: [],
      total: "",
    };
    this.handleDeleteAll = this.handleDeleteAll.bind(this);
    this.purchaseItem = this.purchaseItem.bind(this);
  }

  getItem = () => {
    let endpoint = process.env.REACT_APP_ENDPOINT_USER_CART;
    let key = localStorage.getItem("token");

    axios
      .get(endpoint, { headers: { Authorization: `Token ${key}` } })
      .then((response) => {
        this.setState({
          items: [...response.data.results],
          bill: response.data.bill,
          itemID: response.data.results.id,
        });
        let item = this.state.items;
        let total = this.state.items.reduce(function (cnt, o) {
          return cnt + o.item_price_dec;
        }, 0);

        this.setState({ total: total });
      })
      .catch((error) => {
        console.log(error);
      });
  };

  componentDidMount() {
    this.getItem();
  }

  purchaseItem = (event) => {
    let purchases = this.state.items;
    let arr = purchases.slice();
    this.setState({ boughtItems: arr }, () => {
      let p = arr.map(({ id }) => id);
      //console.log(this.state.boughtItems);
      let endpoint = process.env.REACT_APP_ENDPOINT_PURCHASE;
      let key = localStorage.getItem("token");
      let data = {
        purchases: p,
      };
      const promises = Promise.all(
        arr.map(({ id }) =>
          axios.post(endpoint, (data = { purchases: id }), {
            headers: { Authorization: `Token ${key}` },
          })
        )
      ).then((response) => {
        this.setState({ purchased: true });
        localStorage.setItem("purchased", "yes");
        window.location = "/shop";
        //console.log(this.state.boughtItems)
      });
    });
  };

  deleteItem = (id) => {
    //const items = this.state.items.filter((i) => i.id !== item.id);
    //this.setState({ items });

    let endpoint = process.env.REACT_APP_ENDPOINT_USER_CART;
    let key = localStorage.getItem("token");
    //let cartItemID = this.state.itemID;

    axios
      .delete(endpoint.concat(`${id}/`), {
        headers: { Authorization: `Token ${key}` },
      })
      .then((response) => {
        //let items = response.data;
        if (response.status === 204) {
          this.setState({ deleted: true });
          // return axios.get(endpoint, { headers: { Authorization: `Token ${key}` } })
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  handleDelete = (itemId) => {
    const items = this.state.items.filter((item) => item.id !== itemId);
    let endpoint = process.env.REACT_APP_ENDPOINT_USER_CART;
    let key = localStorage.getItem("token");

    //alert('Deleting item: ', itemId)
    //console.log(itemId)
    axios
      .delete(endpoint.concat(`${itemId}/`), {
        headers: { Authorization: `Token ${key}` },
      })
      .then((response) => {
        //let items = response.data;
        if (response.status === 204) {
          this.setState({ deleted: true, items: items });
          window.location = "/shop";
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  handleDeleteAll = () => {
    let endpoint = process.env.REACT_APP_ENDPOINT_USER_CART_DELETE_ALL;
    let key = localStorage.getItem("token");

    axios
      .delete(endpoint, {
        headers: { Authorization: `Token ${key}` },
      })
      .then((response) => {
        //let items = response.data;
        if (response.status === 204) {
          ///this.setState({ items: response.data })
          window.location = "/shop";
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  render() {
    const deleted = this.state.deleted;
    const merchandise = this.state.items;
    const purchased = this.state.purchased;
    let purchased_ = localStorage.getItem("purchased");
    const bill = this.state.bill;
    const boughtItems = this.state.boughtItems;

    // const stock = this.state.stock.map((obj, id) => {
    //   return(obj.purchases_price_dec)
    // })
    // console.log(stock)
    const list = merchandise.map((obj, id) => {
      return (
        <Item obj={obj} key={obj[id]} id={id} onDelete={this.handleDelete} />
      );
    });

    return (
      <>
        <div className="dropdown-menu">
          <ul className="nav py-2">
            <li className="nav-item">
              <span className="pl-4">Item</span>
            </li>
            <li className="nav-item">
              <span className="pl-3 pr-3">Price</span>
            </li>
            <li className="nav-item">
              <span
                onClick={this.handleDeleteAll}
                className="border-bottom border-danger text-danger font-weight-bold"
              >
                Remove All
              </span>
            </li>
          </ul>
          <div className="dropdown-divider"></div>
          {merchandise.map((item, i, id) => (
            <Item key={i} obj={item} id={id} onDelete={this.handleDelete} />
          ))}

          {/* {list} */}

          <small className="dropdown-item font-weight-bold">
            Total:{" "}
            <span style={{ paddingLeft: "7rem" }} className="text-primary">
          <span className="border border-info px-1 py-1">{bill}</span>
            </span>
          </small>

          <div className="dropdown-divider"></div>
          {!purchased && !purchased_ ? (
            <button
              className="dropdown-item font-weight-bold text-primary"
              onClick={this.purchaseItem}
              value={this.state.items}
            >
              Buy
            </button>
          ) : (
            <button className="dropdown-item text-success" disabled>
              Thank you for shopping
            </button>
          )}
        </div>
      </>
    );
  }
}

export default CartItems;
