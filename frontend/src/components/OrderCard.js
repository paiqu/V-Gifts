import React, { useState } from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';


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

export default function OrderCard(props) {
    const classes = useStyles();
    const theme = useTheme();

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
          <img className={classes.img} src={props.pic_link} alt='' />
        </Grid>

        <Grid item xs={3}>
          {props.product_name} id: {props.product_id}
        </Grid>
        <Grid item xs={2}>
          <p>Quantity: {props.amount}</p>
        </Grid>
        <Grid item xs={1}>
            <p>${props.cost}</p>
        </Grid>
        <Grid item xs={2}>
            <p>${props.purchase_date}</p>
        </Grid>
      </Grid>
    </div>
  );
}