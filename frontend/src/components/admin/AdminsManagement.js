import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from "@material-ui/core/Typography";
import { DataGrid } from '@material-ui/data-grid';
import TextField from '@material-ui/core/TextField';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { useHistory } from 'react-router'

const useStyles = makeStyles((theme) => ({
  form: {
    marginTop: "2rem",
  },
}));

export default function AdminsManagement(props) {
  const classes = useStyles();

  const history = useHistory();

  const token = props.token;
  const [admins, setAdmins] = useState([]);
  const [newAdmin, setNewAdmin] = useState({
    name: "",
    password: "",
    email: "",
  })
  const [loading, setLoading] = useState(false);
  const [state, setState] = useState({
    nameError: false,
    emailError: false,
    passwordError: false,
    help_text: ""
  });

  const handle_error = () => event => {
    setState({
      nameError: false,
      emailError: false,
      passwordError: false,
      help_text: ""
    });
  };

  const handleChange = name => event => {
    setNewAdmin({
      ...newAdmin,
      [name]: event.target.value
    });
  };

  const handleAddAdmin = (event) => {
    event.preventDefault();

    axios.post("/admin/add_admin", {
      token,
      name: newAdmin.name,
      password: newAdmin.password,
      email: newAdmin.email,
    })
    .then((response) => {
      const data = response.data;
      if (data.code == 402) {
        // invalid email
        setState({
          ...state,
          emailError: true,
          help_text: "The entered email is invalid"
        });
      } else if (data.code == 404) {
        // invalid user name
        setState({
          nameError: true,
          help_text: "The admin name is invalid"
        });
      } else if (data.code == 403) {
        // username exist
        setState({
          nameError: true,
          help_text: "The admin name is already existed"
        });
      } else if (data.code == 408) {
        // email existed
        setState({
          ...state,
          emailError: true,
          help_text: "The admin email is already existed"
        });
      } else {
        setLoading(true);
      }
      
    })
    .catch((err) => {});
  }

  useEffect((() => {
    axios.get("/admin/all_admin", {
      params: {
        token,
      }
    })
    .then((response) => {
      const data = response.data;

      setAdmins(data);
    })
    .catch((err) => {});
  }), [loading]);



  const columns = [
    { field: "id", headerName: 'Admin ID', width: 150},
    { field: "username", headerName: 'Admin Name', width: 180 },
    { field: "email", headerName: 'Admin Email', width: 250 },
  ];

  const rows = admins.map(x => {
    return {
      "id": x["admin_id"],
      "username": x["username"],
      "email": x["email"],
    };
  });

  return (
    <div style={{ width: '100%'}}>
      <Typography variant="h5">Admins in the system</Typography>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={7}
        checkboxSelection
        autoHeight
      />
      <form className={classes.form} onSubmit={handleAddAdmin}>
        <Typography variant="h5" style={{marginBottom: "1rem"}}>
          Add a New Admin
        </Typography>
        <Box
          display="flex"
        >
          <TextField
            required
            id="admin-name"
            label="Admin Name"
            placeholder="Admin Name"
            variant="outlined"
            error={state.nameError}
            helperText={state.help_text}
            onChange={handleChange('name')}
            onClick={handle_error()}
            style={{
              marginRight: "1rem",
            }}
          />
          <TextField
            required
            id="admin-email"
            label="Admin Email"
            placeholder="Admin Email"
            variant="outlined"
            error={state.emailError}
            helperText={state.help_text}
            onChange={handleChange('email')}
            onClick={handle_error()}
            style={{
              marginRight: "1rem",
            }}
          />
          <TextField
            required
            id="admin-password"
            label="Admin Password"
            placeholder="Admin Password"
            variant="outlined"
            error={state.passwordError}
            helperText={state.help_text}
            onChange={handleChange('password')}
            onClick={handle_error()}
          />
          <Button 
            type="submit"
            variant="contained" 
            color="primary"
            style={{
              marginLeft: "1rem",
              height: "100%",
            }}
          >
            Add
          </Button>
        </Box>
      </form>
    </div>
  );
}