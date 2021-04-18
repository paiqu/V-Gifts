import React, { useState, useEffect, useContext } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import InterestChips from '../components/InterestsChips';
import Button from '@material-ui/core/Button'
import AuthContext from '../AuthContext';

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  grid: {
    width: "75%",
  },
}));

function InterestSelectionPage(props) {
  const classes = useStyles();
  const token = useContext(AuthContext).user;
  
  const [interests, setInterets] = useState(props.interests);

  const handleUserInterests = (handleNext) => {
    axios.post("/user/set_interest", {
      token: token,
      interest_lst: interests,
    })
    .then((response) => {
      handleNext();
    })
    .catch((err) => {});
  };

  return(
    <div className={classes.root}>
      <Grid className={classes.grid} container spacing={2}>
        <Grid item xs={12}>
          <Typography variant="h3" style={{textAlign: "center"}}>
            Interests:
          </Typography>
          <Typography variant="subtitle1" style={{textAlign: "center"}}>
            Register completed! Welcome to V-Gifts. Now you can select your interests for better recommendations send to you
          </Typography>
        </Grid>
        <Grid item xs={12}>
          <InterestChips interests={interests} />
        </Grid>
        <Grid container item xs={12} spacing={2}>
          <Grid item xs={6} />
          <Grid item xs={3}>
            <Button
              variant="outlined" 
              color="secondary"
              style={{width: "100%"}} 
              onClick={props.handleNext} 
            >
              Skip
            </Button>
          </Grid>
          <Grid item xs={3}>
            <Button 
              variant="contained" 
              color="secondary" 
              style={{ width: "100%" }}
              onClick={() => handleUserInterests(props.handleNext)}
            >
              Finish
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </div>
  );
}

export default InterestSelectionPage;