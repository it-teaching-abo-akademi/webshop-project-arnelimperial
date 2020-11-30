import React from "react";
import axios from "axios";
import Header from "../../partials/header/index";
//import SHOP_DATA from "./shop.data.js";
//import CollectionPreview from "../../partials/collection-preview/index";
import { Redirect } from "react-router-dom";
import Pagination from "react-js-pagination";
import DisplayItems from "../../partials/post-items/index";

import "./style.css";

let num = 1;
class Shop extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      next: null,
      loadingItems: false,
      activePage: 1,
      itemsCount: 0,
      display: null,
    };
  }

  handlePageChange(pageNumber = 1) {
    console.log(`active page is ${pageNumber}`);
    this.setState({ activePage: pageNumber + this.state.activePage });

    let endpoint = process.env.REACT_APP_ENDPOINT_ITEM_DISPLAY;

    const key = process.env.REACT_APP_INITIAL_KEY;

    this.setState({ loadingItems: true });
    axios
      .get(endpoint.concat(`?page=${pageNumber}`), {
        headers: { Authorization: `Token ${key}` },
      })
      .then((response) => {
        //console.log(response.data.count);
        console.log(response.data.results);

        this.setState({
          items: [...response.data.results],
          itemsCount: response.data.count,
        });

        if (response.data.next) {
          this.setState({
            next: response.data.next,
            display: Math.ceil(response.data.count / 4),
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }

  componentDidMount() {
    this.handlePageChange();
    console.log("Page #: ", this.state.activePage);
  }

  displayItems() {
    return this.state.items.map((item, i) => {
      return <DisplayItems obj={item} key={i} />;
    });
  }

  render() {
    const itemsCount = this.state.itemsCount;
    return (
      <>
        <Header />
        <div className="container">
          <div className="parent my-2 px-2" id="display__items">
            {this.displayItems()}
            <div style={{ marginTop: "5rem" }}>
            
              <Pagination
                activePage={this.state.activePage}
                itemsCountPerPage={10}
                totalItemsCount={itemsCount}
                pageRangeDisplayed={this.state.display}
                onChange={this.handlePageChange.bind(this)}
                firstPageText="New"
                lastPageText="Old"
                innerClass="pagination"
                activeClass="active__page"
                itemClass="page-item"
                linkClass="page-link"
                linkClassFirst="bg-info text-white"
                linkClassPrev="bg-info text-white"
              />
            </div>
            <div className="my-1 container">
             
            </div>
          </div>
        </div>
      </>
    );
  }
}
export default Shop;
