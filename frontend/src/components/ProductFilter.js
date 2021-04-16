import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ListSubheader from '@material-ui/core/ListSubheader';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Checkbox from '@material-ui/core/Checkbox';
import LocalShippingIcon from '@material-ui/icons/LocalShipping';
import CollapseCategories from './CollapseCategories';
import CollapsePriceFilter from './CollapsePriceFilter';

const useStyles = makeStyles((theme) => ({
    root: {
        width: '100%',
        // maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
    },
    nested: {
        paddingLeft: theme.spacing(4),
    },
    ListItemText: {
        marginRight: 5,
    },
}));

export default function ProductFilter(props) {
    const classes = useStyles();

  return (
    <div>
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
            <CollapseCategories 
              // categories={props.categories} 
              handleCategory={props.handleCategory}
            />
            {/* <CollapsePriceFilter /> */}
            {/* <ListItem button>
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
            </ListItem> */}
        </List>
    </div>
  );
}
