import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import AuthContext from '../AuthContext';
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

  const [totalItems, setTotalItems] = useState(0);
  const [totalPayment, setPayment] = useState(0);

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
              <Grid item xs={12}>
                <CartProductCard />
              </Grid>
              <Grid item xs={12}>
                <CartProductCard />
              </Grid>
              <Grid item xs={12}>
                <CartProductCard />
              </Grid>
              <Grid item xs={12}>
                <CartProductCard />
              </Grid>
              <Grid item xs={12}>
                <CartProductCard />
              </Grid>
              <Grid item xs={12}>
                <CartProductCard />
              </Grid>
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
                {totalItems}
                <Typography variant="h5">
                  Total
                </Typography>
                {totalItems}
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