import React from 'react';
import Typography from "@material-ui/core/Typography";
import { DataGrid } from '@material-ui/data-grid';


export default function ProductsManagement(props) {
  const token = props.token;

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


  return (
    <div style={{width: '100%'}}>
      <Typography variant="h5">Products in the system</Typography>
      <DataGrid 
        rows={rows} 
        columns={columns} 
        pageSize={7} 
        checkboxSelection 
        autoHeight
      />
    </div>
  );
}

