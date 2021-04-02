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
    pic: "",
  });

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
          pic: data['pic'],
        });
      })
      .catch((err) => {});
  }), [id]);

  const handlePurchase = (event) => {

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
          <img className={classes.image} src={infos.pic} alt="product"/>
        </Grid>
        <Grid item xs={7} className={classes.details}>
          <Typography variant="h3">{infos.name}</Typography>
          {/* <Typography variant="h5">Subtitle</Typography> */}
          <Box display="flex" alignItems="center">
            <Rating name={`product-rating`} value={infos.rating} readOnly/>
            <Typography variant="caption">100 reviews</Typography>
          </Box>
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

          <QuantitySelect />

          <Box
            display="flex"
            flexDirection="row"
            mt={1}
          >
            <Button variant="contained" color="primary" style={{marginRight: "1rem"}}>Purchase</Button>
            <Button variant="outlined" color="secondary">Add to Cart</Button>
          </Box>
        </Grid>
      </Grid>
    </div>
  );
}