import React, { useRef, useEffect, useState } from "react";
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
import AuthContext from '../AuthContext';
import Fab from '@material-ui/core/Fab';
import ChatIcon from '@material-ui/icons/Chat';
import Popper from '@material-ui/core/Popper';
import Chat from '../components/chat/Chat';

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
  },
  fab: {
    position: "fixed",
    bottom: 40,
    right: 20,
  },
  popper: {
    marginRight: "1rem",
  }
}));

const steps = [
  {
    id: '0',
    message: 'Welcome to react chatbot!',
    trigger: '1',
  },
  {
    id: '1',
    message: 'Bye!',
    end: true,
  },
];

function ProductsPage(props) {
  const classes = useStyles();

  const [currPage, setCurrPage] = React.useState(1);
  const [totalPages, setTotalPages] = React.useState(0);
  const [products, setProducts] = React.useState([]);
  const [result, setResult] = React.useState(true);
  // const token = "";

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
          token: "",
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
        const flag = data.flag;
        if (!flag) {
          setResult(false);
        } else {
          setResult(true);
        }

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
    result ? 
      ((keyword == null || keyword == "") ?
        <h3 /> : <h3>Search result of "{keyword}"</h3>)
      : <h3>Sorry, no result of "{keyword}". Take a look at our other products instead</h3>
  );



  const [modalType, setModalType] = useState(1);

  const [anchorEl, setAnchorEl] = useState(null);
  const [open, setOpen] = useState(false);
  const [placement, setPlacement] = React.useState();

  const handleOpen = (event) => {
    setAnchorEl(event.currentTarget);
    setOpen(!open);
  };

  const id = open ? 'simple-popper' : undefined;

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
              container
              item
              xs={12}
              spacing={2}
            >
              <Grid item xs={12}>
                <h3>Recommended for you:</h3>
              </Grid>
              <Grid item xs={12} sm={4}>
                empty
              </Grid>
              <Grid item xs={12} sm={4}>
                empty
              </Grid>
              <Grid item xs={12} sm={4}>
                empty
              </Grid>
            </Grid>
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
                    setModalType={setModalType}
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
        type={modalType}
      />
      <NotLoginModal
        handleClose={handleNlModalClose}
        open={nlModalOpen}
        token={token}
      />
      <Fab
        className={classes.fab} 
        color="secondary"
        aria-label="chat"
        aria-describedby={id}
        onClick={handleOpen}
      >
        <ChatIcon />
      </Fab>
      <Popper
        className={classes.popper}
        id={id}
        open={open}
        anchorEl={anchorEl}
        placement={'top'}
      >
        <Chat />
      </Popper>
    </div>
  );
}

export default ProductsPage;
