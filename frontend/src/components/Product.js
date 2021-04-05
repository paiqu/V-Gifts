import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Rating from '@material-ui/lab/Rating';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';
import axios from 'axios';
import QuantitySelect from './QuantitySelect';
import AuthContext from '../AuthContext';

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
  const token = React.useContext(AuthContext);

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


  const handlePurchase = () => {
    if (!token) {
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
      console.log(response.data)
    })
    .catch((err) => {
      console.log(err);
    });

  };

  return (
    <div>
      <Grid
        container 
        spacing={2}
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
        <Grid item xs={7} className={classes.details}>
          <Typography variant="h3">{infos.name}</Typography>
          <Box display="flex" alignItems="center">
            <Rating name={`product-rating`} value={infos.rating} readOnly/>
            <Typography variant="caption">100 reviews</Typography>
          </Box>
          <Typography variant="h4">
            ${infos.price}
          </Typography>
          <Typography
            variant='body1'
            style={{
              marginTop: "1rem",
              marginRight: "5rem",
              marginBottom: "3rem",
            }}
          >
            {infos.description}
            <br />
            <br />
            Delivery: {infos.delivery}
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
            >Purchase</Button>
            <Button variant="outlined" color="secondary">Add to Cart</Button>
          </Box>
        </Grid>
      </Grid>
    </div>
  );
}