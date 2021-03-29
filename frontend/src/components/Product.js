import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Rating from '@material-ui/lab/Rating';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';

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
  const theme = useTheme();

  const id = props.id;
  const [infos, setInfos] = React.useState({
    id: props.id,
    title: "",
    price: 100,

  });

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
          <img className={classes.image} src="/img/products/mario-1.jpeg" />
        </Grid>
        <Grid item xs={7} className={classes.details}>
          <Typography variant="h3">Mario {infos.id}</Typography>
          <Typography variant="h5">Brand New Mario Figure</Typography>
          <Box display="flex" alignItems="center">
            <Rating name={`product-rating`} value={4} readOnly/>
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
            This is a Mario holding a green turtle shell. A great gift for your special ones. 
            This is a Mario holding a green turtle shell. A great gift for your special ones. 
            This is a Mario holding a green turtle shell. A great gift for your special ones. 
            This is a Mario holding a green turtle shell. A great gift for your special ones. 
            This is a Mario holding a green turtle shell. A great gift for your special ones. 
            This is a Mario holding a green turtle shell. A great gift for your special ones. 
            This is a Mario holding a green turtle shell. A great gift for your special ones. 
          </Typography>
          <Box
            display="flex"
            flexDirection="row"
          >
            <Button variant="contained" color="primary" style={{marginRight: "1rem"}}>Purchase</Button>
            <Button variant="outlined" color="secondary">Add to Cart</Button>
          </Box>
        </Grid>
      </Grid>
    </div>
  );
}