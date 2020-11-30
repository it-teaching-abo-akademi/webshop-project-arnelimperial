import React from "react";
import axios from "axios";
import Header from "../../partials/header/index";
import AddItemForm from "../../partials/add-item-form/index";
import OwnItems from "../../partials/own-items/index";
import DisplayItems from "../../partials/post-items/index";
import BoughtItems from "../../partials/bought-items/index";
import SoldItems from "../../partials/sold-items/index";

class MyItems extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showForm: false,

      items: [],
    };
  }

  showForm = () => {
    return <AddItemForm />;
  };


  getUserItems = () => {
    const endpoint = process.env.REACT_APP_ENDPOINT_USER_ITEMS;
    const key = localStorage.getItem("token");

    axios
      .get(endpoint, { headers: { Authorization: `Token ${key}` } })
      .then((response) => {
        this.setState({ items: [...response.data] });
        //console.log("REsults: ", response.data.results);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  displayItems() {
    return this.state.items.map((item, i) => {
      return <DisplayItems obj={item} key={i} />;
    });
  }

  componentDidMount() {
    this.getUserItems();
  }

  render() {
    return (
      <>
        <Header />
        <div className="container">
          <div className="my-5">
            <button onClick={() => this.setState({ showForm: true })} className="btn btn-outline-primary">
              Add Item
            </button>
            {this.state.showForm ? this.showForm() : null}
       
          </div>
          <div className="mt-2 mb-5">
            <OwnItems />
          </div>
          <hr />
          <div className="mt-2 mb-2">
            <BoughtItems />
          </div>
          <hr />
          <div className="mt-2 mb-2">
          
            <SoldItems />
          </div>
        
        </div>
      </>
    );
  }
}

export default MyItems;
