import React, { useEffect } from 'react';
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import axios from 'axios';

export default function ProductsManagement(props) {
  const [currPage, setCurrPage] = React.useState(1);
  const [totalPages, setTotalPages] = React.useState(0);
  const [products, setProducts] = React.useState([]);

  // const retrieveProducts = () => {
  //   axios.get('/product/get_all', {
  //     params: {
  //       token,
  //       "page": currPage,
  //     }
  //   })
  //     .then((response) => {
  //       const data = response.data;

  //       setTotalPages(data['total_pages']);
  //       setProducts(data['product_lst']);
  //     })
  // };

  return (
    <div>
      Products
    </div>
  );
}

