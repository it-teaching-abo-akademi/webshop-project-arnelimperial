import React, { Suspense } from "react";
import ReactDOM from "react-dom";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

import { BrowserRouter as Router } from "react-router-dom";
//import { Provider } from "react-redux";
//import store from './redux/store';

import "../node_modules/bootswatch/dist/spacelab/bootstrap.min.css";
import "../node_modules/jquery/dist/jquery.min.js";
import "../node_modules/jquery/dist/jquery.slim.min.js";
import "../node_modules/bootstrap/dist/js/bootstrap.bundle.min.js";
//import "../node_modules/bootstrap/dist/js/bootstrap.min.js";

import "../node_modules/@popperjs/core/dist/umd/popper-base.min.js";
import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    
      <Suspense
        fallback={
          <div>
            <h3>Loading...</h3>
            <div className="loader"></div>
          </div>
        }
      >
        <Router>
          <App />
        </Router>
      </Suspense>
    
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
