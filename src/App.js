import React, { lazy } from "react";
//import { HelmetProvider } from "react-helmet-async";
import { Switch, Route, Redirect } from "react-router-dom";
import ProtectedRoute from "./partials/protectedRoute/index";
//import { connect } from "react-redux";
//import setCurrentUser from './redux/user/user.actions';
import "./App.css";

const Home = lazy(() => import("./pages/home/index"));
const Login = lazy(() => import("./pages/login/index"));
const SignUp = lazy(() => import("./pages/signup/index"));
const Logout = lazy(() => import("./pages/logout/index"));
const Shop = lazy(() => import("./pages/shop/index"));
const MyItems = lazy(() => import("./pages/myitems/index"));
const Account = lazy(() => import("./pages/account/index"));
const NotFound = lazy(() => import("./pages/404/index"));
const SingleItem = lazy(() => import("./pages/singleItem/index"));
const EditItem = lazy(() => import("./pages/editItem/index"));


function App() {
  return (
    <>
      <Switch>
        <Route exact path="/" component={Home}></Route>
        <Route exact path="/signup" component={SignUp}></Route>
        <Route exact path="/login" component={Login}></Route>
        <Route path="/shop" component={Shop}></Route>
        <Route exact path="/item/:slug" component={SingleItem}></Route>

        <ProtectedRoute path="/myitems">
          <MyItems />
        </ProtectedRoute>
        <ProtectedRoute path="/logout">
          <Logout />
        </ProtectedRoute>
        <ProtectedRoute path="/account">
          <Account />
        </ProtectedRoute>
        <ProtectedRoute path="/item/edit/:slug">
          <EditItem />
        </ProtectedRoute>
        

        <Route component={NotFound}></Route>
      </Switch>
    </>
  );
}

export default App;
