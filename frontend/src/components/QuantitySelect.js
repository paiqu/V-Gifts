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

  const [count, setCount] = useState(1);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    if (count - 1 >= 1) {
      setCount(count - 1);
    } else {
      setCount(1);
    }
  };

  return (
    <ButtonGroup color="secondary" variant="contained" disableElevation>
      <Button onClick={handleDecrement}>-</Button>
      <Button
        color="primary"
      >
        {count}
      </Button>
      <Button onClick={handleIncrement}>+</Button>
    </ButtonGroup>
  );
}

export default QuantitySelect;