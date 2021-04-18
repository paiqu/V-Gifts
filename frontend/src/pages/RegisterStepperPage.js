import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import RegisterPage from './RegisterPage';
import InterestSelectionPage from './InterestSelectionPage';
import NavBar from '../components/NavBar';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepLabel from '@material-ui/core/StepLabel';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
  },
  backButton: {
    marginRight: theme.spacing(1),
  },
  instructions: {
    marginTop: theme.spacing(1),
    marginBottom: theme.spacing(1),
  },
}));

function getSteps() {
  return [
    'Register your personal info',
    'Select your interests',
    'Browse the market'
  ];
}



function RegisterStepperPage({ setAuth, ...props }) {
  const classes = useStyles();
  const [activeStep, setActiveStep] = React.useState(0);
  const steps = getSteps();

  
  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };
  
  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };
  
  const handleReset = () => {
    setActiveStep(0);
  };
  
  function getStepContent(index) {
    switch(index) {
      case 0:
        return (
          <RegisterPage 
            handleNext={handleNext} 
            setAuth={setAuth}
          />
        );
      case 1:
        return (
          <InterestSelectionPage 
            handleBack={handleBack}
            handleNext={handleNext}
          />
        );
      case 2:
        return "Go to the market now"
    }
  }

  return (
    <div className={classes.root}>
      <NavBar />
      <Stepper activeStep={activeStep} alternativeLabel>
        {steps.map((label, index) => (
            <Step key={label}>
              <StepLabel>
                {label}
                {index === 1 ? 
                  <Typography variant="caption" style={{display: "block"}}>Optional</Typography>
                  : ""
                }
              </StepLabel>
            </Step>
        ))}
      </Stepper>
      <div>
        {activeStep === steps.length ? (
          <div>
            <Typography className={classes.instructions}>All steps completed</Typography>
            <Button onClick={handleReset}>Reset</Button>
          </div>      
        ) : (
          <div>
            {getStepContent(activeStep)}
          </div>
        )}
      </div>
    </div>
  );
}

export default RegisterStepperPage;