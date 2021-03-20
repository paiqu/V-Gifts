// import React, { useState } from 'react';
// import { makeStyles } from '@material-ui/core/styles';
// import Grid from '@material-ui/core/Grid';
// import Typography from '@material-ui/core/Typography';
// import Button from '@material-ui/core/Button';


// export default function ProductFilter(props) {
//     return (
//         <React.Fragment>
//             <Grid container item xs={12} spacing={3}>
//                 <Grid item xs={12}>

//                 </Grid>
//             </Grid>
//         </React.Fragment>
//     );
// }

import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ListSubheader from '@material-ui/core/ListSubheader';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Collapse from '@material-ui/core/Collapse';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import DraftsIcon from '@material-ui/icons/Drafts';
import SendIcon from '@material-ui/icons/Send';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import StarBorder from '@material-ui/icons/StarBorder';
import { right } from '@popperjs/core';
import Checkbox from '@material-ui/core/Checkbox';
import IconButton from '@material-ui/core/IconButton';
import CheckboxList from './CheckboxList';
import ListIcon from '@material-ui/icons/List';
import AttachMoneyIcon from '@material-ui/icons/AttachMoney';
import LocalShippingIcon from '@material-ui/icons/LocalShipping';

const useStyles = makeStyles((theme) => ({
    root: {
        width: '100%',
        maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
    },
    nested: {
        paddingLeft: theme.spacing(4),
    },
    ListItemText: {
        marginRight: 5,
    },
}));

export default function ProductFilter() {
    const classes = useStyles();
    const [catOpen, setCatOpen] = React.useState(true);
    const [priceOpen, setPriceOpen] = React.useState(true);

    const handleCatClick = () => {
        setCatOpen(!catOpen);
    };

    const handlePriceClick = () => {
        setPriceOpen(!priceOpen);
    };

  return (
    <List
        component="nav"
        aria-labelledby="nested-list-subheader"
        subheader={
            <ListSubheader component="div" id="nested-list-subheader">
            Filter
            </ListSubheader>
        }
        className={classes.root}
    >

      <ListItem button onClick={handleCatClick}>
            <ListItemIcon>
                <ListIcon />
            </ListItemIcon>
            <ListItemText primary="Categories"/>
            {catOpen ? <ExpandLess /> : <ExpandMore />}
      </ListItem>
      <Collapse in={catOpen} timeout="auto" unmountOnExit>
            <List component="div" disablePadding>
                <CheckboxList list={["For Him", "For Her", "For Baby", "For Pet"]} />
            </List>
      </Collapse>
      <ListItem button onClick={handlePriceClick}>
            <ListItemIcon>
                <AttachMoneyIcon />
            </ListItemIcon>
            <ListItemText primary="Price Filter" />
            {priceOpen ? <ExpandLess /> : <ExpandMore />}
      </ListItem>
      <Collapse in={priceOpen} timeout="auto" unmountOnExit>
            <List component="div" disablePadding>
                <CheckboxList  list={["Up to $25", "$100 - $200", "$200 & Above"]} />
            </List>
      </Collapse>
      <ListItem button>
            <ListItemIcon>
                <LocalShippingIcon />
            </ListItemIcon>
            <ListItemText primary="Eligible for Free Delivery" />
            <ListItemIcon>
                    <Checkbox
                        edge="start"
                        tabIndex={-1}
                        disableRipple
                    />
            </ListItemIcon>
      </ListItem>
    </List>
  );
}
