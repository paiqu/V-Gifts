import React from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import StoreIcon from '@material-ui/icons/Store';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import GroupIcon from '@material-ui/icons/Group';
import AttachMoneyIcon from '@material-ui/icons/AttachMoney';

const iconSize = 8;

const useStyles = makeStyles((theme) => ({
  root: {

  },
  gridItem: {
    height: theme.spacing(65),
  },
  cardTitle: {
    display: "flex",
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


function AdminHome(props) {
    const classes = useStyles();
    const theme = useTheme();

    const token = props.token;
    const profile = props.profile;

    return (
      <div classeName={classes.root}>
        <Grid container spacing={3}>
          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem}  variant="outlined">
              <CardContent className={classes.cardContent}>
                <div className={classes.cardTitle}>
                  <InboxIcon className={classes.cardIcon}/>
                  <Typography variant="h3" classname={classes.cardTitleText}>
                    Inbox
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  12 messages in total
                  <br />
                  <br />
                  3 unread messages
                </Typography>
              </CardContent>
            </Card>
          </Grid> 
          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem} variant="outlined">
              <CardContent className={classes.cardContent}>
                <div className={classes.cardTitle}>
                  <StoreIcon className={classes.cardIcon}/>
                  <Typography variant="h3" classname={classes.cardTitleText}>
                    Market
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  12 messages in total
                  <br />
                  <br />
                  3 unread messages
                </Typography>
              </CardContent>
            </Card>
          </Grid> 
          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem} variant="outlined">
              <CardContent className={classes.cardContent}>
                <div className={classes.cardTitle}>
                  <GroupIcon className={classes.cardIcon}/>
                  <Typography
                    variant="h3"
                    classname={classes.cardTitleText}
                  >
                    Users
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  {props.usersNum} users registered
                </Typography>
              </CardContent>
            </Card>
          </Grid> 
          <Grid item md={3} xs={12}>
            <Card className={classes.gridItem} variant="outlined">
              <CardContent className={classes.cardContent}>
                <div className={classes.cardTitle}>
                  <AttachMoneyIcon className={classes.cardIcon}/>
                  <Typography variant="h3" classname={classes.cardTitleText}>
                    Orders
                  </Typography>
                </div>
                <Typography variant="h5" color={theme.palette.primary.contrastText} component="p">
                  {props.ordersNum} orders in total
                </Typography>
              </CardContent>
            </Card>
          </Grid> 
        </Grid>
      </div>
    );
}

export default AdminHome;