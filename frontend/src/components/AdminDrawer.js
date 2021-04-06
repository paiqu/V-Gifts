import React, { useState } from 'react';
import clsx from 'clsx';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
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
import AdminHome from './AdminHome';
import axios from 'axios';
import AuthContext from '../AuthContext';
import Button from '@material-ui/core/Button';


const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    display: "flex",
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
    whiteSpace: 'nowrap',
  },
  drawerPaper: {
    width: drawerWidth,
  },
  drawerContainer: {
    overflow: 'auto',
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
  },
  logoutButton: {

  }
}));



export default function AdminDrawer(props) {
  const classes = useStyles();
  const theme = useTheme();

  const token = React.useContext(AuthContext).admin;
  const profile = props.profile;


  const [open, setOpen] = useState(false);
  const [display, setDisplay] = useState({
    home: true,
    orders: false,
    users: false,
  });
  const [users, setUsers] = useState([]);

  // React.useEffect((() => {
  //   axios.get('admin/all_user')
  //   .then((response) => {
  //     const data = response.data;

  //     setUsers(data);
  //   })
  //   .catch((err) => {});
  // }), []);

  const renderUsers = (
    <UsersDataGrid users={users} />
  );

  const renderOrders = (
    <OrdersDataGrid />
  );

  const renderAdminHome = (
    <AdminHome usersNum={users.length} profile={profile} token={token}/>
  );

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
    axios.post('/admin/logout', { token })
      .then((response) => {
        console.log(response);
      
        localStorage.removeItem('admin_token');
        localStorage.removeItem('admin_id');

        // after log out, redirect to home page
        props.history.push('/');
      }) 
      .catch((err) => {console.log(err)});
  };

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="fixed" className={classes.appBar} elevation={0}>
        <Toolbar>
          <Typography
						style={{
							textDecoration: "none",
              fontWeight: "200",
              color: theme.palette.primary.contrastText
						}}
						color="inherit"
						component={Link}
						to={'/'}
						className={classes.title} 
						variant="h4"
						noWrap
					>
            V-Gifts | Admin Page
          </Typography>
          <Button className={classes.logoutButton} variant="contained" color="secondary" onClick={handleLogout}>
            Log out
          </Button>
        </Toolbar>
      </AppBar>
      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <Toolbar />
        <div className={classes.drawerContainer}>
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
          </List>
        </div>
      </Drawer>
      <main className={classes.content}>
        <Toolbar />
        <Box
          display="flex" 
          flexDirection="column"
          alignItems="center"
        >
          <Avatar 
            alt="Admin Avartar"
            src="/img/admin/admin-1.png"
            variant="rounded" 
            style={{
              border: `1px solid ${theme.palette.primary.contrastText}`,
              width: theme.spacing(20),
              height: theme.spacing(20),
              marginBottom: theme.spacing(5),
            }}
          />
          <Typography>
            {`Hello Admin ${profile['name']}(${profile['email']})`}
          </Typography>
        </Box>
        {display.home && renderAdminHome}
        {display.users && renderUsers}
        {display.orders && renderOrders}
      </main>
    </div>
  );
}
