import React, {useState} from "react";
import ProductCard from "../components/ProductCard";
import ProductFilter from "../components/ProductFilter";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Pagination from "@material-ui/lab/Pagination";
import Box from "@material-ui/core/Box";
import NavBar from "../components/NavBar";
import axios from 'axios';
import PurchaseSucessModal from '../components/modals/PurchaseSuccessModal';
import NotLoginModal from '../components/modals/NotLoginModal';
// import AuthContext from '../AuthContext';
import AuthContext from '../AuthContext';


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

  const token = React.useContext(AuthContext).user;
  // const token = "";
  const [psModalOpen, setPsModalOpen] = useState(false);
  const [nlModalOpen, setNlModalOpen] = useState(false);

  const handlePsModalOpen = () => {
    setPsModalOpen(true);
  };

  const handlePsModalClose = () => {
    setPsModalOpen(false);
  };
  const handleNlModalOpen = () => {
    setNlModalOpen(true);
  };

  const handleNlModalClose = () => {
    setNlModalOpen(false);
  };


  const retrieveProducts = () => {
    axios.get('/product/get_all', {
      params: {
        token: "",
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
          >
            <Grid
              className={classes.productsGrid}
              container
              item
              xs={12}
              spacing={2}
            >
              {products.map((x) =>
                <Grid key={`product-${x['product_id']}`} item xs={12} sm={4}>
                  <ProductCard
                    key={`product-${x['product_id']}`}
                    id={x['product_id']}
                    name={x['name']}
                    price={x['price']}
                    rating={x['rating']}
                    img={x['pic_link']}
                    handlePsModalOpen={handlePsModalOpen}
                    handlePsModalClose={handlePsModalClose}
                    handleNlModalOpen={handleNlModalOpen}
                    handleNlModalClose={handleNlModalClose}
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
      <PurchaseSucessModal
        handleClose={handlePsModalClose}
        open={psModalOpen}
        token={token}
      />
      <NotLoginModal
        handleClose={handleNlModalClose}
        open={nlModalOpen}
        token={token}
      />
    </div>
  );
}

export default ProductsPage;
