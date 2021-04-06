import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import axios from 'axios';


function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="/">
        V-Gift
            </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100vh',
  },
  image: {
    backgroundImage: `url(/img/home/home-4.jpeg)`,
    backgroundRepeat: 'no-repeat',
    backgroundColor:
      theme.palette.type === 'light' ? theme.palette.grey[50] : theme.palette.grey[900],
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',

  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  adminButton: {
    position: "fixed",
    bottom: 10,
    right: 10,
  }
}));

function AdminLoginPage({ setAdminAuth, ...props }) {
  const [infos, setInfos] = React.useState({
    name: "",
    password: "",
  });

  const handleChange = name => event => {
    setInfos({
      ...infos,
      [name]: event.target.value
    });
  };

  const [state, setState] = React.useState({
    nameError: false,
    passwordError: false,
    help_text: ""
  });

  const handle_error = () => event => {
    setState({
      nameError: false,
      passwordError: false,
      help_text: ""
    });
  };


  const handleSubmit = (event) => {
    event.preventDefault();

    if (!infos.name || !infos.password) {
      setState({
        // error: true,
        nameError: true,
        passwordError: true,
        help_text: "All fields have to be finished before logging you in"
      });
      return;
    }

    axios.post('admin/login', { 
      name: infos.name,
      password: infos.password,
     })
    .then((response) => {
      const data = response.data;
      if (data.code == 404) {
        // admin name does not exist
        setState({
          nameError: true,
          help_text: "The entered admin name does not exist"
        });
      } else if (data.code == 405) {
        // wrong password
        setState({
          passwordError: true,
          help_text: "The password entered is incorrect"
        });
      } else {
        setAdminAuth(data.token, data.user_id);
        props.history.push(`/admin/${data.token}`);
      }
    })
    .catch((err) => { });
  }

  const classes = useStyles();
  const theme = useTheme();


  return (
    <Grid container component="main" className={classes.root}>
      <CssBaseline />
      <Grid item xs={false} sm={4} md={7} className={classes.image} />
      <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            V-Gifts Admin Sign in
          </Typography>
          <form className={classes.form} noValidate onSubmit={handleSubmit}>
            <TextField
              error={state.nameError}
              helperText={state.help_text}
              variant="outlined"
              margin="normal"
              required
              fullWidth
              label="Admin Account Name"
              autoFocus
              onChange={handleChange('name')}
              onClick={handle_error()}
            />
            <TextField
              error={state.passwordError}
              helperText={state.help_text}
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Admin Password"
              type="password"
              id="password"
              autoComplete="current-password"
              onChange={handleChange('password')}
              onClick={handle_error()}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Sign In
            </Button>
            <Box mt={5}>
              <Copyright />
            </Box>
          </form>
        </div>
      </Grid>
    </Grid>
  );
}

export default AdminLoginPage;
