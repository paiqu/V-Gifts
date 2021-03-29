import React from "react";
// import NavBar from "../components/NavBar";
// import '../css/products-page.css';
import ProductCard from "../components/ProductCard";
import ProductFilter from "../components/ProductFilter";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Pagination from "@material-ui/lab/Pagination";
import Box from "@material-ui/core/Box";
import NavBar from "../components/NavBar";

const useStyles = makeStyles((theme) => ({
    main: {
        marginTop: "2rem"
    },

}));

function ProductsPage(props) {
  const classes = useStyles();

  // Hook for page number
  const [page, setPage] = React.useState(1);

  const products = ["mario-1", "mario-2", "mario-3"];
  const items = [];

  for (let i = 0; i < 3; i++) {
    items.push(
      <Grid item xs={12} sm={4}>
        <ProductCard key={products[i]} name={products[i]} />
      </Grid>
    );
  }

  const handlePageChange = (event, number) => {
    setPage(number);
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
              {items}
            </Grid>
            <Grid container item xs={12} spacing={3}>
              {items}
            </Grid>
            <Grid container item xs={12} spacing={3}>
              {items}
            </Grid>

            <Pagination
              item
              sm={6}
              m="auto"
              count={10}
              color="secondary"
              variant="outlined"
              shape="rounded"
              size="large"
              onChange={handlePageChange}
              page={page}
            />
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default ProductsPage;
