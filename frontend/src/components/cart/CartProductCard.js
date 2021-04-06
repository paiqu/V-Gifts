import React, { useState, useEffect } from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import AuthContext from '../../AuthContext';
import Grid from '@material-ui/core/Grid';
import IconButton from '@material-ui/core/IconButton';
import AddCircleOutlineIcon from '@material-ui/icons/AddCircleOutline';
import RemoveCircleOutlineIcon from '@material-ui/icons/RemoveCircleOutline';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Button from '@material-ui/core/Button'
import axios from 'axios';

const useStyles = makeStyles((theme) => ({
  root: {
    borderRadius: 5,
    overflow: "hidden",
    // height: "10rem",
    width: "100%",
  },
  grid: {
    //height: "10rem",
  },
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
	const token = React.useContext(AuthContext);
  const item = props.item;

  const [id, setID] = useState(item["product_id"]);
  const [img, setImg] = useState(item["pic_link"]);
  const [name, setName] = useState(item["product_name"]);
  const [price, setPrice] = useState(item["price"]);
  const [amount, setAmount] = useState(item["amount"]);
  const [cost, setCost] = useState(item["cost"]);

  const handleDecrement = () => {
    if (amount - 1 <= 0) {
      setAmount(0);
    } else {
      setAmount(amount - 1);
    }

    axios.post("/user/cart/change", {
      token: token,
      "product_id": id,
      amount: amount-1,
    })
    .then((response) => {
      setCost(cost-price);
      if (amount - 1 == 0) {
        props.handleTotalPaymentChange(-price);
        

        props.history.go(0);
      }
    })
    .catch((err) => {});
  };

  const handleIncrement = () => {
    setAmount(amount + 1);

    axios.post("/user/cart/change", {
      token: token,
      "product_id": id,
      amount: amount+1,
    })
    .then((response) => {
      props.handleTotalPaymentChange(price);
      setCost(cost + price);
    })
    .catch((err) => {});
  };

  const handlePurchase = () => {
    let info = [
      [id, amount]
    ];

    let payload = {
      token: token,
      list: info,
    };

    axios({
      url: "/order/new",
      method: "post",
      data: payload,
    })
    .then(response => {
      console.log(response.data);
      props.history.go(0);
    })
    .catch((err) => {
      console.log(err);
    });
  }

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
        <Grid item xs={2}>
          <p>Quantity: {amount}</p>
          <p>{`Item price: \$${price}`}</p>
          <p>{`Total price: \$${cost}`}</p>
        </Grid>
        <Grid container item xs={4} justify="flex-end">
          <Grid item xs={12}>
              <ButtonGroup>
                <IconButton color="secondary" onClick={handleDecrement} >
                  <RemoveCircleOutlineIcon />
                </IconButton>
                <IconButton color="secondary" onClick={handleIncrement} >
                  <AddCircleOutlineIcon />
                </IconButton>
                <Button variant="contained" color="primary" onClick={handlePurchase}>
                  Buy
                </Button>
              </ButtonGroup>
          </Grid>
        </Grid>
        <div>
        </div>
      </Grid>
    </div>
  );
}

export default CartProductCard;