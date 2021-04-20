import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";
import { makeStyles, useTheme } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import ButtonBase from '@material-ui/core/ButtonBase';

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    display: "flex",
  },
  disabledButton: {
    backgroundColor: theme.palette.secondary,
  },
  quantityButton: {
    width: "200rem",
  },
  quantityText: {
    width: "2rem",
    textAlign: "center",
  },
}));

function QuantitySelect(props) {
  const classes = useStyles();
  const theme = useTheme();

  return (
    <ButtonGroup color="secondary" variant="contained" disableElevation style={{width: "100%"}}>
      <Button onClick={props.handleDecrement}>-</Button>
      <Button
        color="primary"
      >
        {props.amount}
      </Button>
      <Button onClick={props.handleIncrement}>+</Button>
    </ButtonGroup>
  );
}

export default QuantitySelect;