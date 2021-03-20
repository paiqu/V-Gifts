import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import ButtonBase from '@material-ui/core/ButtonBase';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing(2),
        margin: 'auto',
        maxWidth: 500,
    },
    image: {
        width: 128,
        height: 128,
    },
    img: {
        margin: 'auto',
        display: 'block',
        maxWidth: '100%',
        maxHeight: '100%',
    },
}));

export default function Product(props) {
    const classes = useStyles();

    const [id, setID] = useState(null);
    const [price, setPrice] = useState(100);

    return (
        <div className={classes.root}>
        <Paper className={classes.paper}>
            <Grid container spacing={2}>
            <Grid item>
                <ButtonBase className={classes.image}>
                <img className={classes.img} alt="complex" src={`img/products/${props.name}.jpeg`} />
                </ButtonBase>
            </Grid>
            <Grid item xs={12} sm container>
                <Grid item xs container direction="column" spacing={2}>
                <Grid item xs>
                    <Typography gutterBottom variant="subtitle1">
                    {props.name}
                    </Typography>
                    <Typography variant="body2" gutterBottom>
                        A normal Mario
                    </Typography>
                    <Typography variant="body2" color="textSecondary">
                    ID: {`${props.name}`}
                    </Typography>
                </Grid>
                <Grid item>
                    <Button
                        color="On Primary"
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
