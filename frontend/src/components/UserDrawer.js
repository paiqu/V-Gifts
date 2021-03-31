import React from 'react';
import clsx from 'clsx';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import { Link } from 'react-router-dom';
import Avatar from '@material-ui/core/Avatar';
import Box from '@material-ui/core/Box';
import GroupIcon from '@material-ui/icons/Group';
import AttachMoneyIcon from '@material-ui/icons/AttachMoney';
import StoreIcon from '@material-ui/icons/Store';
import UsersDataGrid from './UsersDataGrid';
import OrdersDataGrid from './OrdersDataGrid';
import HomeIcon from '@material-ui/icons/Home';
import UserHome from './UserHome';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import AuthContext from '../AuthContext';


const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginRight: 36,
  },
  hide: {
    display: 'none',
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
    whiteSpace: 'nowrap',
  },
  drawerOpen: {
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerClose: {
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    overflowX: 'hidden',
    width: theme.spacing(7) + 1,
    [theme.breakpoints.up('sm')]: {
      width: theme.spacing(9) + 1,
    },
  },
  toolbar: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: theme.spacing(0, 1),
    // necessary for content to be below app bar
    ...theme.mixins.toolbar,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  logo: {
    margin: "auto",
    textAlign: 'center',
    maxWidth: "auto",
    maxHeight: '7vh',
    marginRight: "0.5rem",
  },
  title: {
    flexGrow: 1,
  }
}));



export default function UserDrawer(props) {
  const classes = useStyles();
  const theme = useTheme();
  
  const token = React.useContext(AuthContext);
  const profile = props.profile;

  const [open, setOpen] = React.useState(false);
  const [display, setDisplay] = React.useState({
    home: true,
    orders: false,
    users: false,
  });

  const renderUsers = (
    <UsersDataGrid />
  );

  const renderOrders = (
    <OrdersDataGrid />
  );

  const renderUserHome = (
    <UserHome />
  );

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  const displayHome = () => {
    setDisplay({
      home: true,
      orders: false,
      users: false,
    });
  }

  const displayUsers = () => {
    setDisplay({
      home: false,
      orders: false,
      users: true,
    });
  }

  const displayOrders = () => {
    setDisplay({
      home: false,
      orders: true,
      users: false,
    });
  }

  const handleLogout = (event) => {
    axios.post('/user/logout', { token })
      .then((response) => {
        console.log(response);
      
        localStorage.removeItem('id');
        localStorage.removeItem('token');

        // after log out, redirect to home page
        props.history.push('/');
      }) 
      .catch((err) => {console.log(err)});
  };

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar
        position="fixed"
        className={clsx(classes.appBar, {
          [classes.appBarShift]: open,
        })}
        style={{
          boxShadow: 'none',
        }}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            className={clsx(classes.menuButton, {
              [classes.hide]: open,
            })}
          >
            <MenuIcon />
          </IconButton>
          <Typography
						style={{
							textDecoration: "none",
              fontWeight: "200",
              color: theme.palette.primary.contrastText
						}}
						color="inherit"
						component={Link}
						to={'/products/1'}
						className={classes.title} 
						variant="h4"
						noWrap
					>
            V-Gifts | My Profile
          </Typography>
          <Button variant="contained" color="secondary" onClick={handleLogout}>
            Log out
          </Button>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        className={clsx(classes.drawer, {
          [classes.drawerOpen]: open,
          [classes.drawerClose]: !open,
        })}
        classes={{
          paper: clsx({
            [classes.drawerOpen]: open,
            [classes.drawerClose]: !open,
          }),
        }}
      >
        <div className={classes.toolbar}>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
          </IconButton>
        </div>
        <Divider />
        <List>
          <ListItem button key={"Home"} onClick={displayHome}>
            <ListItemIcon><HomeIcon /></ListItemIcon>
            <ListItemText primary={"Home"} />
          </ListItem>
          <ListItem button key={"Inbox"}>
            <ListItemIcon><InboxIcon /></ListItemIcon>
            <ListItemText primary={"Inbox"} />
          </ListItem>
          <ListItem button key={"Market"}>
            <ListItemIcon><StoreIcon /></ListItemIcon>
            <ListItemText primary={"Market"} />
          </ListItem>
          <ListItem button key={"Users"} onClick={displayUsers}>
            <ListItemIcon><GroupIcon /></ListItemIcon>
            <ListItemText primary={"Users"} />
          </ListItem>
          <ListItem button key={"Orders"} onClick={displayOrders}>
            <ListItemIcon><AttachMoneyIcon /></ListItemIcon>
            <ListItemText primary={"Orders"} />
          </ListItem>
          <ListItem button key={"Logout"} onClick={handleLogout} >
            <ListItemIcon><ExitToAppIcon /></ListItemIcon>
            <ListItemText primary={"Log out"} />
          </ListItem>
        </List>
        <Divider />
        {/* <List>
          {['All mail', 'Trash', 'Spam'].map((text, index) => (
            <ListItem button key={text}>
              <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
              <ListItemText primary={text} />
            </ListItem>
          ))}
        </List> */}
      </Drawer>
      <main className={classes.content}>
        <div className={classes.toolbar} />
        <Box
          display="flex" 
          flexDirection="column"
          alignItems="center"
        >
          <Avatar 
            alt="Admin Avartar"
            src="/img/profile/profile-1.jpg"
            variant="rounded" 
            style={{
              border: `1px solid ${theme.palette.primary.contrastText}`,
              width: theme.spacing(20),
              height: theme.spacing(20),
              marginBottom: theme.spacing(5),
            }}
          />
          <Typography>
            Hello {`${profile['first_name']} ${profile['last_name']}`}
          </Typography>
        </Box>
        {display.home && renderUserHome}
        {display.users && renderUsers}
        {display.orders && renderOrders}
      </main>
    </div>
  );
}
