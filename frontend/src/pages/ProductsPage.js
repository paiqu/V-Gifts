import React from "react";
import ProductCard from "../components/ProductCard";
import ProductFilter from "../components/ProductFilter";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Pagination from "@material-ui/lab/Pagination";
import Box from "@material-ui/core/Box";
import NavBar from "../components/NavBar";
import axios from 'axios';
import { Link, Redirect } from 'react-router-dom';
import PaginationItem from '@material-ui/lab/PaginationItem';
import { MemoryRouter, Route } from 'react-router';


const useStyles = makeStyles((theme) => ({
  main: {
    padding: 10,
  },
  leftContainer: {

  },
  rightContainer: {
    // overflowX: "hidden",
    padding: 50,
  },
  pagination: {
    justifySelf: "end",
  }
}));

function ProductsPage(props) {
  const classes = useStyles();

  const [currPage, setCurrPage] = React.useState(1);
  const [totalPages, setTotalPages] = React.useState(0);
  const [products, setProducts] = React.useState([]);

  const token = "";


  const retrieveProducts = () => {
    axios.get('/product/get_all', {
      params: {
        token,
        "page": currPage,
      }
    })
      .then((response) => {
        const data = response.data;

        setTotalPages(data['total_pages']);
        setProducts(data['product_lst']);
      })
  };

  React.useEffect(retrieveProducts, [currPage]);


  const handlePageChange = (event, number) => {
    setCurrPage(number);
  };

  return (
    <div className={classes.root}>
      <NavBar className={classes.navBar} />
      <Box
        className={classes.main}
      >
        <Grid container spacing={0}>
          <Grid className={classes.leftContainer} container item xs={12} sm={3}>
            <ProductFilter />
          </Grid>

          <Grid 
            className={classes.rightContainer} 
            container item xs={12} sm={9} spacing={3}
            // direction="column"
            // justify="space-between"
            // alignItems="center"
          >
            <Grid
              className={classes.productsGrid}
              container
              item
              xs={12}
              spacing={2}
            >
              {/* <Grid container item xs={12} spacing={3}> */}
              {products.map((x) =>
                <Grid key={`product-${x['product_id']}`} item xs={12} sm={4}>
                  {/* <p>{x['product_id']}</p>
                  <p>{x['name']}</p>
                  <p>{x['price']}</p>
                  <p>{x['rating']}</p> */}
                  <ProductCard
                    key={`product-${x['product_id']}`}
                    id={x['product_id']}
                    name={x['name']}
                    price={x['price']}
                    rating={x['rating']}
                    img={x['pic_link']}
                  />
                </Grid>
              )}
              {/* </Grid> */}
            </Grid>
            <Grid
              className={classes.pagination}
              item
              xs={12}
            >
              <Pagination
                count={totalPages}
                color="secondary"
                variant="outlined"
                shape="rounded"
                size="large"
                page={currPage}
                onChange={handlePageChange}
              />
              <p>page {currPage} of {totalPages}</p>
            </Grid>

          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default ProductsPage;
