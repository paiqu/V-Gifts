import React, { useState } from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import ButtonBase from '@material-ui/core/ButtonBase';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';
import AuthContext from '../AuthContext';
import axios from 'axios';



const useStyles = makeStyles((theme) => ({
    root: {
        // flexGrow: 1,
        height: "100%",
    },
    paper: {
        padding: theme.spacing(2),
        margin: 'auto',
        height: "100%",
    },
    image: {
        // width: 128,
        // height: 128,
        width: '9rem',
        height: '9rem',
    },
    img: {
        margin: 'auto',
        display: 'block',
        maxWidth: '100%',
        maxHeight: '100%',
        padding: 9,
    },

}));

export default function ProductCard(props) {
    const classes = useStyles();
    const theme = useTheme();
    const token = React.useContext(AuthContext).user;

    const [id, setId] = useState(props.id);
    const [name, setName] = useState(props.name);
    const [price, setPrice] = useState(props.price);
    const [rating, setRating] = useState(props.rating);
    const [img, setImg] = useState(props.img);

    const handleAddToCart = () => {
      axios.post("/user/cart/add",
        {
          token: token,
          product_id: id,
          amount: 1,
        }
      )
      .then((response) => {

      })
      .catch((err) => {});
    };

    return (
        <div className={classes.root}>
            <Paper className={classes.paper}>
                <Grid container spacing={0}>
                    <Grid item>
                        <ButtonBase
                          className={classes.image}
                          component={Link}
                          to={`/product/${id}`}
                        >
                            <img className={classes.img} alt="product image" src={img} />
                        </ButtonBase>
                    </Grid>
                    <Grid item xs={12} sm container>
                        <Grid item xs container direction="column" spacing={2}>
                        <Grid item xs>
                            <Typography gutterBottom variant="subtitle1">
                              {`${name.split(" ").splice(0, 11).join(" ")} ...`}
                            </Typography>
                            <Typography variant="body2" gutterBottom>
                              A normal product
                            </Typography>
                            <Typography variant="body2" color="textSecondary">
                              ID: {`${id}`}
                            </Typography>
                        </Grid>
                        <Grid item>
                            <Button
                              color={theme.palette.primary.contrastText}
                              onClick={handleAddToCart}
                            >
                              <Typography variant="body2" style={{ cursor: 'pointer' }}>
                                  <ShoppingCartIcon /> Add to Cart
                              </Typography>
                            </Button>
                        </Grid>
                        </Grid>
                        <Grid item>
                          <Typography variant="subtitle1">${price}</Typography>
                        </Grid>
                    </Grid>
                </Grid>
            </Paper>
        </div>
    );
}
