import React, { useEffect } from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { useHistory } from 'react-router'
import Chip from '@material-ui/core/Chip';

import FavoriteBorderOutlinedIcon from '@material-ui/icons/FavoriteBorderOutlined';
import AttachMoneyOutlinedIcon from '@material-ui/icons/AttachMoneyOutlined';
// import AttachMoneyIcon from '@material-ui/icons/AttachMoney';
import ListAltIcon from '@material-ui/icons/ListAlt';
import FaceIcon from '@material-ui/icons/Face';
// import ShoppingCartIcon from "@material-ui/icons/ShoppingCart";
import ShoppingCartOutlinedIcon from '@material-ui/icons/ShoppingCartOutlined';

const iconSize = 8;

const useStyles = makeStyles((theme) => ({
  root: {

  },
  gridItem: {
    height: theme.spacing(65),
  },
  cardTitle: {
    display: "flex",
    alignItems: "center",
    marginBottom: theme.spacing(1),
  },
  cardIcon: {
    width: theme.spacing(iconSize),
    height: theme.spacing(iconSize),
    marginRight: theme.spacing(0.5),
  },
  cardTitleText: {
    textDecoration: "none",
    fontWeight: "200",
    color: theme.palette.primary.contrastText,
  },
  cardContent: {
    display: "flex",
    flexDirection: "column",
    alignItems: "start",
  }
}));


function UserHome(props) {
    const classes = useStyles();
    const theme = useTheme();
    const history = useHistory();

    const token = props.token;
    const profile = props.profile;
    const [fundToAdd, setFundToAdd] = React.useState(profile['fund']);
    const [cart, setCart] = React.useState([]);

    const handleFundToAddChange = (e) => {
      setFundToAdd(e.target.value);
    }

    const handleAddFund = () => {
      axios.post("/user/profile/fund/add", {
        token: token,
        num: fundToAdd,
      }).then((response) => {
        const data = response.data;
        console.log(data);
        history.go(0);
      })
      .catch((err) => {});
    }

    useEffect((() => {
      axios.get('/user/cart/list', {
        params: {
          token,
        }
      })
      .then((response) => {
        const data = response.data;
        console.log(data);
        setCart(data);
      })
      .catch((err) => {});

      axios.get('/user/cart/list', {
        params: {
          token,
        }
      })
      .then((response) => {
        const data = response.data;
        console.log(data);
        setCart(data);
      })
      .catch((err) => {});
    }), [token]);
  

    return (
      <div classeName={classes.root}>
        <Grid container spacing={3}>
          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem} variant="outlined">
              <CardContent className={classes.cardContent}>
                <div className={classes.cardTitle}>
                  <FaceIcon className={classes.cardIcon}/>
                  <Typography variant="h4" classname={classes.cardTitleText}>
                    My Details
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  Name: {profile["first_name"]} {profile["last_name"]}
                </Typography>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  Username: {profile["username"]}
                </Typography>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  Email: {profile["email"]}
                </Typography>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  Address: {profile["address"]}
                </Typography>
              </CardContent>
            </Card>
          </Grid> 

          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem}  variant="outlined">
              <CardContent className={classes.cardContent}>
                <div 
                  className={classes.cardTitle}
                >
                  <AttachMoneyOutlinedIcon className={classes.cardIcon}/>
                  <Typography variant="h4" classname={classes.cardTitleText}>
                    Balance
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  {`\$${profile['fund']} left`} 
                </Typography>

                <Typography variant="h5" color={theme.palette.primary.contrastText} style={{marginTop: "1rem"}}>
                  Add Fund:
                </Typography>
                <TextField
                  id="outlined-number"
                  label="Number"
                  type="number"
                  size="small"
                  value={fundToAdd}
                  InputLabelProps={{
                    shrink: true,
                  }}
                  variant="outlined"
                  style={{
                    marginBottom: "1rem",
                  }}
                  inputProps={{
                    step: 100,
                    min: 0,
                  }}
                  onChange={handleFundToAddChange}
                />
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleAddFund}
                >
                  Add
                </Button>
              </CardContent>
            </Card>
          </Grid>
          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem} variant="outlined">
              <CardContent className={classes.cardContent}>
                <div className={classes.cardTitle}>
                  <FavoriteBorderOutlinedIcon className={classes.cardIcon}/>
                  <Typography variant="h4" classname={classes.cardTitleText}>
                    My Interests
                  </Typography>
                </div>
                <div
                  style={{
                    display: "flex"
                  }}
                >
                  <Chip label="healthy" />
                  <Chip label="whiskey" />
                  <Chip label="vagan" color="secondary" />
                  <Chip label="pens" vairant="outlined"  />
                </div>
              </CardContent>
            </Card>
          </Grid> 
          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem} variant="outlined">
              <CardContent className={classes.cardContent}>
                <div className={classes.cardTitle}>
                  <ListAltIcon className={classes.cardIcon}/>
                  <Typography variant="h4" classname={classes.cardTitleText}>
                    Orders
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  {props.ordersNum} orders in total
                </Typography>
                <div className={classes.cardTitle}>
                  <ShoppingCartOutlinedIcon className={classes.cardIcon}/>
                  <Typography variant="h4" classname={classes.cardTitleText}>
                    Cart
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  {cart.length} items in cart
                </Typography>
              </CardContent>
            </Card>
          </Grid> 
        </Grid>
      </div>
    );
}

export default UserHome;