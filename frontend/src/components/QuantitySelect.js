import React, { useState } from "react";
import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";
import { makeStyles, useTheme } from '@material-ui/core/styles';


const useStyles = makeStyles((theme) => ({
  disabledButton: {
    backgroundColor: theme.palette.secondary,
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