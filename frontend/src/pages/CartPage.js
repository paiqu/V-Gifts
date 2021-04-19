import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AuthContext from '../AuthContext';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import NavBar from '../components/NavBar';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import CartProductCard from '../components/cart/CartProductCard';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button'
import { useHistory } from 'react-router'

const useStyles = makeStyles((theme) => ({
  title: {

  },
  checkoutBtn: {
    width: "100%",
  },
}));

function CartPage(props) {
  const classes = useStyles();
  const theme = useTheme();
  const token = React.useContext(AuthContext).user;
  const history = useHistory()

  // eslint-disable-next-line
  const [totalItems, setTotalItems] = useState(0);
  // eslint-disable-next-line
  const [totalPayment, setTotalPayment] = useState(0);
  const [products, setProducts] = useState([]);

  useEffect((() => {
    axios.get('/user/cart/list', {
      params: {
        token,
      }
    })
    .then((response) => {
      const data = response.data;
      console.log(data);
      setProducts(data);
    })
    .catch((err) => {});

    axios.get('/user/cart/cost', {
      params: {
        token,
      }
    })
    .then((response) => {
      const cost = response.data.cost;

      setTotalPayment(cost);
    })
    .catch((err) => {});

  }), [token]);


  const handleTotalPaymentChange = (change) => {
    setTotalPayment(totalPayment + change);
  };

  const handleCheckout = () => {
    let cartProducts = products.map((x) => [x["product_id"], x["amount"]]);

    let payload = {
      token: token,
      list: cartProducts,
    };

    axios({
      url: "/order/new",
      method: "post",
      data: payload,
    })
    .then(response => {
      console.log(response.data);
      history.go(0);
    })
    .catch((err) => {
      console.log(err);
    });
  };

  return (
    <div>
      <NavBar />
      <Box 
        ml={theme.spacing(1)} mr={theme.spacing(1)}
      >
        <Grid
          container
          spacing={2}
        >
          <Grid item xs={12}>
            <Typography variant="h3" align="center">
              My Cart
            </Typography>
          </Grid>
          <Grid container item xs={12} spacing={2}>
            <Grid container item xs={9} spacing={2}>
              {products.map((x) => 
                <Grid key={`${x["product_id"]}-${x["product_name"]}-${x["amount"]}`} item xs={12}>
                  <CartProductCard 
                    item={x} 
                    history={history} 
                    handleTotalPaymentChange={handleTotalPaymentChange}
                  />
                </Grid>
              )}
            </Grid>
            <Grid item xs={3}>
              <Box
                p={2}
                border={1}
                borderColor={theme.palette.primary.contrastText}
                borderRadius={5}
              >
                <Typography variant="h5">
                  Total Products in Cart
                </Typography>
                {products.length}
                <Typography variant="h5">
                  Total Payment
                </Typography>
                <b>{`$${totalPayment}`}</b>
                <Button 
                  className={classes.checkoutBtn} 
                  variant="contained" 
                  color="secondary"
                  style={{
                    marginTop: "2rem",
                  }}
                  onClick={handleCheckout}
                >
                  CHECKOUT
                </Button>
              </Box>
            </Grid>
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default CartPage;