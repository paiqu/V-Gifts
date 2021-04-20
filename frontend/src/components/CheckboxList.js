import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { useHistory } from 'react-router'



const useStyles = makeStyles((theme) => ({
    root: {
        width: '100%',
        // maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
    },
    nested: {
        paddingLeft: theme.spacing(8),
    },
}));

export default function CheckboxList(props) {
    const classes = useStyles();
    const history = useHistory();

    const categoryList = ["for men", "for women", "for children", "for friends", "for elder", "for relationship", "foods", "tools", "luxuries", "entertainment", "working"];
    // const categories = props.categories.numList;

    // // const [checked, setChecked] = useState([0]);
    // const [categories, setCategories] = useState(Array(11).fill(0));
    // // console.log(props);
    // if (props.categories.length > 0) {
    //   for (let i = 0; i < props.categories.length; i++) {
    //     if (categories.includes(props.categories[i])) {
    //       setCategories(categories.map(x => (
    //         x === props.categories[i] ? 1 : 0
    //       )));
    //     }
    //   }
    // }

    // const setChecked = (index) => {
    //   return !!categories[index];
    // }

    // const handleToggle = (value) => () => {
    //     const currentIndex = checked.indexOf(value);
    //     const newChecked = [...checked];

    //     if (currentIndex === -1) {
    //         newChecked.push(value);
    //     } else {
    //         newChecked.splice(currentIndex, 1);
    //     }

    //     setChecked(newChecked);
    // };

  return (
    <List className={classes.root}>
      <ListItem
        key={"all-products"} 
        role={undefined} 
        button 
        onClick={() => props.handleCategory("")}
        className={classes.nested}
      >
        <ListItemText 
          id={"list-label-all"} 
          primary={"All Products"} 
          style={{
            textTransform: "capitalize",
          }}
        />
      </ListItem>
      {categoryList.map((value, index) => {
          const labelId = `list-label-${value}`;

          return (
            <ListItem
              key={value} 
              role={undefined} 
              button 
              onClick={() => props.handleCategory(value)}
              className={classes.nested}
            >
              <ListItemText 
                id={labelId} 
                primary={value} 
                style={{
                  textTransform: "capitalize",
                }}
              />
            </ListItem>
          );
      })}
    </List>
  );
}
