import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from "@material-ui/core/Typography";
import { DataGrid } from '@material-ui/data-grid';
import TextField from '@material-ui/core/TextField';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { Grid } from '@material-ui/core';


const useStyles = makeStyles((theme) => ({
  form: {
    marginTop: "2rem",
  },
}));

export default function ProductsManagement(props) {
  const classes = useStyles();
  const token = props.token;
  const [newProduct, setNewProduct] = useState({
    name: "",
    price: 0,
    description: "",
    delivery: "",
    img: "",
  });

  const columns = [
    { field: 'id', headerName: 'Product ID', width: 150},
    { field: "name", headerName: 'Product Name', width: 350 },
    { field: "price", headerName: 'Price', width: 180 },
    { field: "rating", headerName: 'Rating', width: 250 },
    // { field: "pic_link", headerName: 'Amount', width: 100 },
  ];

  const rows = props.products.map(x => {
    return {
      "id": x["product_id"],
      "name": x["name"],
      "price": `\$${x["price"]}`,
      "rating": `${x["rating"]}/5`,
    };
  });

  const handleChange = name => event => {
    setNewProduct({
      ...newProduct,
      [name]: event.target.value
    });
  };

  const handleAddProduct = (event) => {
    event.preventDefault();
  };


  return (
    <div style={{width: '100%'}}>
      <Typography variant="h5">Products in the system</Typography>
      <DataGrid 
        rows={rows} 
        columns={columns} 
        pageSize={5} 
        checkboxSelection 
        autoHeight
      />
      <form className={classes.form} onSubmit={handleAddProduct}>
        <Typography variant="h5" style={{marginBottom: "1rem"}}>
          Add a New Product
        </Typography>
        <Grid
          container
          spacing={2}
        >
          <Grid 
            container 
            item 
            xs={12} 
            spacing={2}
          >
            <Grid item xs={2}>
              <TextField
                required
                id="product-name"
                label="Product Name"
                placeholder="Admin Name"
                variant="outlined"
                onChange={handleChange('name')}
                style={{
                  marginRight: "1rem",
                  width: "100%",
                }}
              />
            </Grid>
            <Grid item xs={2}>
              <TextField
                required
                id="product-price"
                label="Price"
                placeholder="Product Price"
                type="number"
                variant="outlined"
                onChange={handleChange('price')}
                inputProps={{
                  step: 10,
                  min: 0,
                }}
                value={newProduct.price}
                style={{
                  width: "100%",
                }}
              />
            </Grid>
          </Grid>
          <Grid
            container
            item
            xs={12}
            spacing={2}
          >
            <Grid item xs={4}>
              <TextField
                required
                id="product-description"
                label="Description"
                placeholder="Product Description"
                variant="outlined"
                onChange={handleChange('description')}
                style={{
                  marginRight: "1rem",
                  width: "100%",
                }}
                multiline
                rows={4}
                rowsMax={4}
              />
            </Grid>
          </Grid>

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
        </Grid>
      </form>
    
    </div>
  );
}

