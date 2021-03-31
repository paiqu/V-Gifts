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
    marginTop: "2rem"
  },

}));

function ProductsPage(props) {
  const classes = useStyles();

  console.log(`current page is ${props.match.params.page}`);

  const [infos, setInfos] = React.useState({
    currPage: props.match.params.page,
    totalPages: 0,
    products: [],
  })

  const [items, setItems] = React.useState([]);

  const token = "";

  const retrieveProducts = () => {
    axios.get('/product/get_all', {
      params: {
        token,
        "page": infos.currPage,
      }
    })
      .then((response) => {
        const data = response.data;       
        setInfos({
          ...infos,
          products: data['product_lst'],
          totalPages: data['total_pages'],
        });

        setItems(infos.products.map((x) => <Grid item xs={12} sm={4}><ProductCard infos={x} /></Grid>));
      })
  };

  React.useEffect(retrieveProducts, [infos.currPage]);


  const handlePageChange = (event, number) => {
    // setInfos({
    //   ...infos,
    //   currPage: number,
    // });

    props.history.push(`/products/${number}`);
  };

  return (
    <div className={classes.root}>
      <NavBar className={classes.navBar} />
      <Box 
        className={classes.main}
        display="flex" 
        flexDirection="column" 
        alignContent="center"
      >
        <Grid container spacing={10}>
          <Grid container item xs={12} sm={3} direction={"column"}>
            <ProductFilter />
          </Grid>
          <Grid
            className={classes.productsGrid}
            container
            item
            xs={12}
            sm={9}
            direction={"column"}
            alignItems="center"
            spacing={5}
            height="20%"
          >
            <Grid container item xs={12} spacing={3}>
              {/* {infos.products.map((x) => <Grid item xs={12} sm={4}><ProductCard infos={x} /></Grid>)} */}
              {items}
            </Grid>
            <Pagination
              item
              sm={6}
              m="auto"
              count={infos.totalPages}
              color="secondary"
              variant="outlined"
              shape="rounded"
              size="large"
              page={infos.currPage}
              renderItem={(item) => (
                <PaginationItem 
                  component={Link}
                  to={`/products/${item.page}`}
                  {...item}
                />
              )}
            />
            <p>page {infos.currPage} of {infos.totalPages}</p>
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default ProductsPage;
