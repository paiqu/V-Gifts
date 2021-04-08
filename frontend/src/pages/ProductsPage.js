import React, { useRef, useEffect } from "react";
import ProductCard from "../components/ProductCard";
import ProductFilter from "../components/ProductFilter";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Pagination from "@material-ui/lab/Pagination";
import Box from "@material-ui/core/Box";
import NavBar from "../components/NavBar";
import axios from 'axios';


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

  const query = new URLSearchParams(props.location.search);
  // const token = query.get('token');
  const keyword = query.get('keyword');
  // const page = query.get('page');
  // const category = query.get('category');

  function usePrevious(value) {
    const ref = useRef();
    useEffect(() => {
      ref.current = value;
    });
    return ref.current;
  }

  const prevKeyword = usePrevious(keyword);
  const prevPage = usePrevious(currPage);

  const retrieveProducts = () => {
    if (keyword == null || keyword == "") {    
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
    } else {
      axios.post('/product/search', {
        token: "",
        // "page": (page == null || page == "") ? 1 : page,
        page: prevKeyword !== keyword ? 1 : currPage, 
        keyword: keyword,
        category: [],
        price_range: [],
      })
      .then((response) => {
        const data = response.data;

        setTotalPages(data['total_pages']);
        setProducts(data['product_lst']);
        if (prevKeyword !== keyword) {
          setCurrPage(1);
        }
      })
    }
  };

  React.useEffect(retrieveProducts, [currPage, keyword]);


  const handlePageChange = (event, number) => {
    setCurrPage(number);
  };

  const renderSearchTitle = (
    (keyword == null || keyword == "") ?
      <h3 /> : <h3>Search result of "{keyword}"</h3>
  );

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
              <Grid item xs={12}>
                {/* <h3>Search result of {keyword}</h3> */}
                {renderSearchTitle}
              </Grid>
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
