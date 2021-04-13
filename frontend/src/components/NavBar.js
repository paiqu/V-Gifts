import React from "react";
import { fade, makeStyles, useTheme } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import InputBase from "@material-ui/core/InputBase";
import Badge from "@material-ui/core/Badge";
import MenuItem from "@material-ui/core/MenuItem";
import Menu from "@material-ui/core/Menu";
import SearchIcon from "@material-ui/icons/Search";
import AccountCircle from "@material-ui/icons/AccountCircle";
import MailIcon from "@material-ui/icons/Mail";
import NotificationsIcon from "@material-ui/icons/Notifications";
import ShoppingCartIcon from "@material-ui/icons/ShoppingCart";
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';
import AuthContext from '../AuthContext';
import axios from "axios";
import { useHistory } from 'react-router'
import { Grid } from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
  grow: {
    // flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
		marginRight: theme.spacing(2),
  },
	marketButton: {
		marginRight: theme.spacing(2),
	},
  search: {
    position: "relative",
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    "&:hover": {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginRight: theme.spacing(2),
    marginLeft: 0,
    width: "100%",
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: "100%",
    position: "absolute",
    pointerEvents: "none",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  inputRoot: {
    color: "inherit",
    width: "50rem",
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create("width"),
    width: "100%",
  },
  sectionDesktop: {
    display: 'flex',
  },
  toolBar: {
    minHeight: "10vh",
  },
  logo: {
    margin: "auto",
    textAlign: 'center',
    maxWidth: "auto",
    maxHeight: '7vh',
    marginRight: "0.5rem",
  },
}));

export default function NavBar() {
  const token = React.useContext(AuthContext).user;

  const classes = useStyles();
  const theme = useTheme();
  const history = useHistory();

  const [searchInput, setSearchInput] = React.useState("");

  const handleSearchChange = event => {
    setSearchInput(event.target.value);
  }

  const handleSearch = () => {
    history.push(`/products?keyword=${searchInput}`);
  };

  const NotLoggedIn = (
    <Button>
      Login
    </Button>
  );

  const LoggedInProfile = (
    <Button
      component={Link}
      to={ token ? `/profile/${token}` : "/login"}
      edge="end"
      aria-label="account of current user"
      color="inherit"
      startIcon={<AccountCircle />}
    >
      Logged in as Pai
    </Button>
  );

  const renderProfile = () => {
    if (token) {
      return <LoggedInProfile />
    } else {
      return <NotLoggedIn />
    }
  };


  return (
    <div className={classes.grow}>
      {/* <Grid
        container
        spacing={2}
      >
        <Grid
          item
          xs={}
        >
          
        </Grid>
        <Grid
          item
          xs={}
        >

        </Grid>
        <Grid
          item
          xs={}
        >

        </Grid>
        <Grid
          item
          xs={}
        >

        </Grid>
        <Grid
          item
          xs={}
        >

        </Grid>
      </Grid> */}
      <AppBar position="static" style={{boxShadow: 'none'}}>
        <Toolbar className={classes.toolBar}>
          <img 
            className={classes.logo} 
            src="/img/logo/logo-1.png" 
            alt="V-Gifts logo"
          />
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
            V-Gifts
          </Typography>
					<Button
						className={classes.marketButton}
						component={Link}
						to={{
              pathname: '/products',
            }}
						style={{color: theme.palette.primary.contrastText}}
						variant="outlined"
					>
            Market
					</Button>
          <div className={classes.search}>
            <div className={classes.searchIcon}>
              <SearchIcon />
            </div>
            <InputBase
              placeholder="Search…"
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ "aria-label": "search" }}
              onChange={handleSearchChange}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  handleSearch();
                }
              }}
            />
          </div>
          {/* <div className={classes.grow} /> */}
          <div className={classes.sectionDesktop}>
            <IconButton 
              aria-label="cart" 
              color="inherit"
              component={Link}
              to={ `/profile/${token}/cart`}
            >
            <Badge badgeContent={0} color="secondary">
                <ShoppingCartIcon />
              </Badge>
            </IconButton>
            {/* <IconButton
							component={Link}
							to={ token ? `/profile/${token}` : "/login"}
              edge="end"
              aria-label="account of current user"
              color="inherit"
            >
              <AccountCircle />
            </IconButton> */}
            {/* <renderProfile /> */}
          </div>
        </Toolbar>
      </AppBar>
    </div>
  );
}
