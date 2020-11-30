// import React from "react";
// import axios from "axios";
// //import Header from "../../partials/header/index";
// //import Items from "./items";
// //import "./style.css";

// class Cart extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       items: [],
//       addItem: '',
//     };
//   }
//   toCart = () => {
//     let endpoint = process.env.REACT_APP_ENDPOINT_CART;
//     let key = localStorage.getItem("token");

//     axios
//       .post(endpoint, { headers: { Authorization: `Token ${key}` } })
//       .then((response) => {
//         if (response.status === 200) {
//           this.setState({ items: [...response.data] });
//         }
//       })
//       .catch((error) => {
//         console.log(error);
//       });
//   };

//   componentDidMount() {
//     this.toCart();
//   }

 
//   render() {
//     return (
//       <>
//        <form method="POST">
//          <input type="button" />

//        </form>
//       </>
//     );
//   }
// }

// export default OwnItems;
