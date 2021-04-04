import React, { useState } from 'react';
import Box from '@material-ui/core/Box';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import IconButton from '@material-ui/core/IconButton';
import AddCircleOutlineIcon from '@material-ui/icons/AddCircleOutline';
import RemoveCircleOutlineIcon from '@material-ui/icons/RemoveCircleOutline';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Divider from '@material-ui/core/Divider';
import Button from '@material-ui/core/Button'

const useStyles = makeStyles((theme) => ({
  root: {
    borderRadius: 5,
    overflow: "hidden",
    // height: "10rem",
  },
  grid: {
    //height: "10rem",
  },
  // item: {
  //   height: "100%",
  // },
  img: {
    //width: "10rem",
    height: "10rem",
    maxWidth: "100%",
    // margin: 10,
    padding: 10,
  },
}));

function CartProductCard(props) {
  const classes = useStyles();
  const theme = useTheme();

  const [img, setImg] = useState("/img/products/h001.jpg");
  const [name, setName] = useState("Product name");
  const [amount, setAmount] = useState(1);

  const handleDecrement = () => {
    if (amount - 1 == 0) {
      // remove the product from cart in database
    }
    setAmount(amount - 1);
  };

  const handleIncrement = () => {
    setAmount(amount + 1);
  };

  return (
    <div
      className={classes.root}
      style={{
        border: `1px solid ${theme.palette.primary.contrastText}`
      }}
    >
      <Grid
        className={classes.grid}
        container 
        spacing={2}
        alignItems="center"
      >
        <Grid item xs={3}>
          <img className={classes.img} src={img} 
            // style={{
            //   border: `1px solid ${theme.palette.primary.contrastText}`
            // }}
          />
        </Grid>
        
        <Grid item xs={3}>
          {name}
        </Grid>
        <Grid item xs={3}>
          Quantity: {amount}
        </Grid>
        <Grid item xs={3}>
          <ButtonGroup>
            <IconButton color="secondary" onClick={handleDecrement} >
              <RemoveCircleOutlineIcon />
            </IconButton>
            <IconButton color="secondary" onClick={handleIncrement} >
              <AddCircleOutlineIcon />
            </IconButton>
            <Button variant="contained" color="primary">
              PURCHASE
            </Button>
          </ButtonGroup>
        </Grid>
        <div>
        </div>
      </Grid>
    </div>
  );
}

export default CartProductCard;