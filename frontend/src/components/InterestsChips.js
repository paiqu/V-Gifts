import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CustomChip from './CustomChip';

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    display: 'flex',
    justifyContent: 'center',
    flexWrap: 'wrap',
    '& > *': {
      margin: theme.spacing(1),
    },
  },
}));

export default function InterestsChips(props) {
  const [interests, setInterests] = useState(props.interests);
  const [selected, setSelected] = useState([]);

  useEffect((() => {
    setInterests(props.interests);
  }), []);

  const handleAdd = (interest) => {
    setSelected(prevSelected => [...prevSelected, interest]);
  };

  const handleRemove = (interest) => {
    setSelected(selected.filter(item => item !== interest));
  }

  return (
    <div>
      {interests.map((x) => (
        <CustomChip
          key={x} 
          label={x}
          handleAdd={handleAdd}
          handleRemove={handleRemove}
        />
      ))}
    </div>
  );
}