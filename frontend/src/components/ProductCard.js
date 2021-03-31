import React, { useState } from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import ButtonBase from '@material-ui/core/ButtonBase';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing(2),
        margin: 'auto',
        // maxWidth: 500,
    },
    image: {
        // width: 128,
        // height: 128,
    },
    img: {
        margin: 'auto',
        display: 'block',
        maxWidth: '100%',
        maxHeight: '100%',
    },

}));

export default function ProductCard(props) {
    const classes = useStyles();
    const theme = useTheme();

    // const [id, setID] = useState(null);
    // const [price, setPrice] = useState(100);

    const [infos, setInfos] = useState({
      id: props.infos['product_id'],
      name: props.infos['name'],
      price: props.infos['price'],
      rating: props.infos['rating'],
    });

    // React.useEffect((() => {
    //   setInfos({
    //     id: props.infos['product_id'],
    //     name: props.infos['name'],
    //     price: props.infos['price'],
    //     rating: props.infos['rating'],
    //   });
    // }), [props.infos]);

    return (
        <div className={classes.root}>
            <Paper className={classes.paper}>
                <Grid container spacing={2}>
                    <Grid item>
                        <ButtonBase
                          className={classes.image}
                          component={Link}
                          to={`/product/${infos.id}`}
                        >
                            <img className={classes.img} alt="complex" src="/img/products/mario-1.jpeg" />
                        </ButtonBase>
                    </Grid>
                    <Grid item xs={12} sm container>
                        <Grid item xs container direction="column" spacing={2}>
                        <Grid item xs>
                            <Typography gutterBottom variant="subtitle1">
                              {infos.name}
                            </Typography>
                            <Typography variant="body2" gutterBottom>
                                A normal product
                            </Typography>
                            <Typography variant="body2" color="textSecondary">
                              ID: {`${infos.id}`}
                            </Typography>
                        </Grid>
                        <Grid item>
                            <Button
                                color={theme.palette.primary.contrastText}
                            >
                                <Typography variant="body2" style={{ cursor: 'pointer' }}>
                                    <ShoppingCartIcon /> Add to Cart
                                </Typography>
                            </Button>
                        </Grid>
                        </Grid>
                        <Grid item>
                        <Typography variant="subtitle1">${infos.price}</Typography>
                        </Grid>
                    </Grid>
                </Grid>
            </Paper>
        </div>
    );
}
