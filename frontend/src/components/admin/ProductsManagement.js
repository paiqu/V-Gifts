import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from "@material-ui/core/Typography";
import { DataGrid } from '@material-ui/data-grid';
import TextField from '@material-ui/core/TextField';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { Grid } from '@material-ui/core';
import ImageIcon from '@material-ui/icons/Image';
import DoneIcon from '@material-ui/icons/Done';

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
    img: null,
  });
  const [selectedProduct, setSelectedProduct] = useState({
    name: "",
    price: 0,
    description: "",
    delivery: "",
    img: null,
  });

  const [isUploaded, setIsUploaded] = useState(false);
  const [selectionModel, setSelectionModel] = useState([]);

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

    let imgData = new FormData();
    imgData.append("img", newProduct.img)
  };

  const handleFileUpload = (event) => {
    setNewProduct({
      ...newProduct,
      img: event.target.files[0],
    });
    setIsUploaded(true);
  }

  useEffect((() => {
    if (selectionModel.length != 0) {    
      axios.get('/product/get_info', {
          params: {
            id: parseInt(selectionModel),
          }
        })
      .then((response) => {
        const data = response.data;
        
        setSelectedProduct({
          name: data['name'],
          price: data['price'],
          description: data['description'],
          // delivery: data['delivery'],
          // rating: data['rating'],
          // img: data['pic_link'],
        });
      })
      .catch((err) => {});
    }
  }), [selectionModel]);

  return (
    <div style={{width: '100%'}}>
      <Typography variant="h5">Products in the system</Typography>
      <DataGrid 
        rows={rows} 
        columns={columns} 
        pageSize={5} 
        checkboxSelection 
        autoHeight
        selectionModel={selectionModel}
        hideFooterSelectedRowCount
        // disableMultipleSelection={true}
        onSelectionModelChange={(selection) => {
          const newSelectionModel = selection.selectionModel;

          if (newSelectionModel.length > 1) {
            const selectionSet = new Set(selectionModel);
            const result = newSelectionModel.filter(
              (s) => !selectionSet.has(s)
            );

            setSelectionModel(result);
          } else {
            setSelectionModel(newSelectionModel);
          }
        }}
      />
      <Grid container>
        <Grid container item xs={6}>
          <form className={classes.form} onSubmit={handleAddProduct}>
            <Grid
              container
              spacing={2}
              xs={12}
            >
              <Grid item xs={12}>
                <Typography variant="h5" style={{marginBottom: "1rem"}}>
                  Add a New Product
                </Typography>
              </Grid>
              <Grid
                container
                item
                xs={12}
                spacing={2}
              >
                <Grid item xs={5}>
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
                <Grid item xs={5}>
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
                <Grid item xs={10}>
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
              <Grid
                container
                item
                xs={12}
                spacing={2}
              >
                <Grid item xs={5}>
                  { !isUploaded &&
                    <Button
                      variant="contained"
                      component="label"
                      color="primary"
                      style={{
                        width: "100%"
                      }}
                    >
                      <ImageIcon />Upload Image
                      <input
                        type="file"
                        accept="image/*"
                        hidden
                        onChange={handleFileUpload}
                      />
                    </Button>
                  }
                  { isUploaded &&
                    <Button
                      variant="contained"
                      component="label"
                      color="primary"
                      style={{
                        width: "100%"
                      }}
                    >
                      <DoneIcon />Image Uploaded
                      <input
                        type="file"
                        accept="image/*"
                        hidden
                        onChange={handleFileUpload}
                      />
                    </Button>
                  }
                </Grid>
                <Grid item xs={5}>
                  <Button
                    type="submit"
                    variant="contained"
                    color="secondary"
                    style={{
                      width: "100%",
                    }}
                  >
                    Add New Product
                  </Button>
                </Grid>
              </Grid>
            </Grid>
          </form>
        </Grid>
        <Grid container item xs={6}>
          <form className={classes.form} onSubmit={handleAddProduct}>
            <Grid
              container
              spacing={2}
            >
            <Grid item xs={12}>
              <Typography variant="h5" style={{marginBottom: "1rem"}}>
                Edit an Existed Product (Current Selected: id-{selectionModel})
              </Typography>
            </Grid>
              <Grid
                container
                item
                xs={12}
                spacing={2}
              >
                <Grid item xs={5}>
                  <TextField
                    required
                    id="product-name"
                    label="Name"
                    placeholder="Product Name"
                    variant="outlined"
                    onChange={handleChange('name')}
                    InputLabelProps={{shrink: true}}
                    style={{
                      marginRight: "1rem",
                      width: "100%",
                    }}
                    value={selectedProduct.name}
                  />
                </Grid>
                <Grid item xs={5}>
                  <TextField
                    required
                    id="product-price"
                    label="Price"
                    // placeholder="Product Price"
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
                    value={selectedProduct.price}
                  />
                </Grid>
              </Grid>
              <Grid
                container
                item
                xs={12}
                spacing={2}
              >
                <Grid item xs={10}>
                  <TextField
                    required
                    id="product-description"
                    label="Description"
                    // placeholder="Product Description"
                    variant="outlined"
                    onChange={handleChange('description')}
                    style={{
                      marginRight: "1rem",
                      width: "100%",
                    }}
                    multiline
                    rows={4}
                    rowsMax={4}
                    value={selectedProduct.description}
                  />
                </Grid>
              </Grid>
              <Grid
                container
                item
                xs={12}
                spacing={2}
              >
                <Grid item xs={5}>
                  { !isUploaded &&
                    <Button
                      variant="contained"
                      component="label"
                      color="primary"
                      style={{
                        width: "100%"
                      }}
                    >
                      <ImageIcon />Upload Image
                      <input
                        type="file"
                        accept="image/*"
                        hidden
                        onChange={handleFileUpload}
                      />
                    </Button>
                  }
                  { isUploaded &&
                    <Button
                      variant="contained"
                      component="label"
                      color="primary"
                      style={{
                        width: "100%"
                      }}
                    >
                      <DoneIcon />Image Uploaded
                      <input
                        type="file"
                        accept="image/*"
                        hidden
                        onChange={handleFileUpload}
                      />
                    </Button>
                  }
                </Grid>
                <Grid item xs={5}>
                  <Button
                    type="submit"
                    variant="contained"
                    color="secondary"
                    style={{
                      width: "100%",
                    }}
                  >
                    Confirm Edit
                  </Button>
                </Grid>
              </Grid>
            </Grid>
          </form>
        </Grid>
      </Grid>
    
    </div>
  );
}

