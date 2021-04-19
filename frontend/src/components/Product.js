import React, { useState } from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Rating from '@material-ui/lab/Rating';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';
import axios from 'axios';
import QuantitySelect from './QuantitySelect';
import AuthContext from '../AuthContext';
import PurchaseSucessModal from '../components/modals/PurchaseSuccessModal';
import NotLoginModal from '../components/modals/NotLoginModal';


const useStyles = makeStyles((theme) => ({
  image: {
    width: 550,
    height: 550,
  },
  imageContainer: {
    display: "flex",
    justifyContent: "flex-end",
  },
  details: {
    display: "flex",
    flexDirection: "column",
  }
}));

export default function Product(props) {
  const classes = useStyles();
  // eslint-disable-next-line
  const theme = useTheme();
  const token = React.useContext(AuthContext).user;

  const id = props.id;
  const [infos, setInfos] = React.useState({
    id: props.id,
    name: "",
    price: 100,
    description: "",
    delivery: "",
    rating: "",
    img: "",
  });
  const [amount, setAmount] = React.useState(1);

  React.useEffect((() => {
    axios.get('/product/get_info', {
      params: {
        id,
      }
    })
      .then((response) => {
        const data = response.data;
        
        setInfos({
          name: data['name'],
          price: data['price'],
          description: data['description'],
          delivery: data['delivery'],
          rating: data['rating'],
          img: data['pic_link'],
        });
      })
      .catch((err) => {});
  }), [id]);

  const handleIncrement = () => {
    setAmount(amount + 1);
  };

  const handleDecrement = () => {
    if (amount - 1 >= 1) {
      setAmount(amount - 1);
    } else {
      setAmount(1);
    }
  };

  const [psModalOpen, setPsModalOpen] = useState(false);
  const [nlModalOpen, setNlModalOpen] = useState(false);
  const [modalType, setModalType] = useState(1);


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


  const handlePurchase = () => {
    if (!token) {
      handleNlModalOpen();
      return;
    }

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
      setModalType(1);
      handlePsModalOpen();
    })
    .catch((err) => {
      console.log(err);
    });
  };

  const handleAddToCart = () => {
    if (!token) {
      handleNlModalOpen();
      return;
    }

    axios.post("/user/cart/add",
      {
        token: token,
        product_id: id,
        amount: amount,
      }
    )
    .then((response) => {
      setModalType(2);
      handlePsModalOpen();
    })
    .catch((err) => {});
  };


  return (
    <div>
      <Grid
        container 
        spacing={5}
        direction="row"
        justify="flex-end"
        style={{
          marginTop: "1rem",
        }}
      >
        <Grid
          className={classes.imageContainer}
          item 
          xs={5} 
        >
          <img className={classes.image} src={infos.img} alt="product"/>
        </Grid>
        <Grid
          className={classes.details}
          container
          direction="column"
          spacing={1}
          item 
          sm={7}
          xs={12} 
        >
          <Grid item xs={12}>
            <Typography variant="h4">
              {infos.name}
            </Typography>
          </Grid>
          <Grid item xs={12}>
            <Rating 
              name={`product-rating`} 
              value={infos.rating} 
              precision={0.5} 
              readOnly
            />
          </Grid>
          <Grid item xs={12}>
            <Typography variant="h4">
              ${infos.price}
            </Typography>
          </Grid>
          <Grid item xs={12}>
            <Typography
              variant='body1'
            >
              {infos.description}
            </Typography>
          </Grid>
          <Grid item xs={12}>
            <Typography
              variant='body1'
            >
              Delivery: ${infos.delivery}
            </Typography>
          </Grid>
          <Grid container item xs={12} alignItems="center">
            <Grid item xs={12}>
              <QuantitySelect
                amount={amount}
                handleIncrement={handleIncrement}
                handleDecrement={handleDecrement}
              />
            </Grid>
          </Grid>
          <Grid container item xs={12} alignItems="center">
            <Grid item xs={12}>
              <Typography variant='body1'>
                Total: ${amount * infos.price}
              </Typography>
            </Grid>
          </Grid>

          <Grid
            container
            item
            xs={12}
            alignItems="center"
            spacing={1}
          >
            {infos.description}
            <br />
            <br />
            Delivery: ${infos.delivery}
          </Typography>
          <QuantitySelect
            amount={amount}
            handleIncrement={handleIncrement}
            handleDecrement={handleDecrement}
          />

          <Box
            display="flex"
            flexDirection="row"
            mt={1}
          >
            <Button
              variant="contained" 
              color="primary" 
              style={{marginRight: "1rem"}}
              onClick={handlePurchase}  
            >
              Purchase
            </Button>
            <Button variant="outlined" color="secondary" onClick={handleAddToCart}>Add to Cart</Button>
          </Box>
        </Grid>
      </Grid>
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
    </div>
  );
}
