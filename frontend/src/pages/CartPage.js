import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AuthContext from '../AuthContext';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import NavBar from '../components/NavBar';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import CartProductCard from '../components/cart/CartProductCard';
import Box from '@material-ui/core/Box';
import Divider from '@material-ui/core/Divider';
import Button from '@material-ui/core/Button'

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
  const token = React.useContext(AuthContext);

  const [totalItems, setTotalItems] = useState(0);
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
  }), [])

  return (
    <div>
      <NavBar />
      <Box ml={theme.spacing(3)} mr={theme.spacing(3)}>
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
                <Grid item xs={12}>
                  <CartProductCard item={x} />
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
                  Items
                </Typography>
                {products.length}
                <Typography variant="h5">
                  Total
                </Typography>
                {totalPayment}
                <Button 
                  className={classes.checkoutBtn} 
                  variant="contained" 
                  color="secondary"
                  style={{
                    marginTop: "2rem",
                  }}
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