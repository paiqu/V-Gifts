import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import ListSubheader from '@material-ui/core/ListSubheader';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Collapse from '@material-ui/core/Collapse';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import Checkbox from '@material-ui/core/Checkbox';
import CheckboxList from './CheckboxList';
import ListIcon from '@material-ui/icons/List';


export default function CollapseCategories () {
    const [open, setOpen] = React.useState(true);

    const handleClick = () => {
        setOpen(!open);
    };

    return (
        <List>
            <ListItem onClick={handleClick}>
                    <ListItemIcon>
                        <ListIcon />
                    </ListItemIcon>
                    <ListItemText primary="Categories"/>
                    {/* {open ? <ExpandLess /> : <ExpandMore />} */}
            </ListItem>
            <Collapse in={open} timeout="auto" unmountOnExit>
                    <List component="div" disablePadding>
                        <CheckboxList list={["For Him", "For Her", "For Baby", "For Pet"]} />
                    </List>
            </Collapse>
            {/* <CheckboxList list={["For Him", "For Her", "For Baby", "For Pet"]} /> */}
        </List>
    );

}