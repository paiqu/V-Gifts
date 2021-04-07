import React, { useState } from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import ButtonBase from '@material-ui/core/ButtonBase';
import { Link } from 'react-router-dom';
import moment from 'moment';
import Rating from '@material-ui/lab/Rating';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import StarBorderIcon from '@material-ui/icons/StarBorder';

const useStyles = makeStyles((theme) => ({
    root: {
      margin: 5,
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
      width: "10rem",
      // maxWidth: "100%",
      // margin: 10,
      padding: 10,
    },
  }));

export default function OrderCard(props) {
    const classes = useStyles();
    const theme = useTheme();
    const date = moment(parseFloat(props.purchase_date*1000)).format("YYYY-MM-DD HH:mm:ss");
    const [value, setValue] = React.useState(0);

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
        spacing={3}
        alignItems="center"
      >
        <Grid item xs={3}>
          {/* <ButtonBase
            className={classes.image}
            component={Link}
            to={`/product/${props.product_id}`}
          >
            <img className={classes.img} src={props.pic_link} alt='props.product_id' />
          </ButtonBase> */}
          <img className={classes.img} src={props.pic_link} alt='props.product_id'
            // style={{
            //   border: `1px solid ${theme.palette.primary.contrastText}`
            // }}
          />
        </Grid>

        <Grid item xs={4}>
          {props.product_name}
        </Grid>
        <Grid item xs={1}>
          <p>Quantity: {props.amount}</p>
          <p>${props.cost}</p>
        </Grid>
        <Grid item xs={2}>
            <p>{date}</p>
        </Grid>
        <Grid item xs={2}>
          <Box component="fieldset" mb={3} borderColor="transparent">
            <Rating
              name="customized-empty"
              defaultValue={0}
              precision={0.5}
              emptyIcon={<StarBorderIcon fontSize="inherit" />}
            />
      </Box>
        </Grid>
      </Grid>
    </div>
  );
}