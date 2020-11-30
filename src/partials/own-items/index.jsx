import React from "react";
import axios from "axios";
//import Header from "../../partials/header/index";
import Items from "./items";
import "./style.css";

class OwnItems extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
    };
  }
  getItems = () => {
    let endpoint = process.env.REACT_APP_ENDPOINT_USER_ITEMS;
    let key = localStorage.getItem("token");

    axios
      .get(endpoint, { headers: { Authorization: `Token ${key}` } })
      .then((response) => {
        if (response.status === 200) {
          this.setState({ items: [...response.data] });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  };

  componentDidMount() {
    this.getItems();
  }

  displayItems() {
    return this.state.items.map((item, i) => {
      return <Items obj={item} key={i} />;
    });
  }

  render() {
    return (
      <>
        <h5>Items For Sale</h5>
        <div className="items__container" id="items__container-id">
          {this.displayItems()}
        </div>
      </>
    );
  }
}

export default OwnItems;
