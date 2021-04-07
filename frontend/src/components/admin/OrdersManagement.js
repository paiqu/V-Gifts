import React, { useState } from 'react';
import Typography from "@material-ui/core/Typography";
import axios from 'axios';
import { DataGrid } from '@material-ui/data-grid';



export default function OrdersManagement(props) {
  const token = props.token;

  const columns = [
    { field: 'id', headerName: 'Order ID', width: 150},
    { field: 'user_id', headerName: 'User ID', width: 180 },
    { field: 'product_id', headerName: 'Product ID', width: 180 },
    { field: 'product_name', headerName: 'Product Name', width: 250 },
    { field: 'amount', headerName: 'Amount', width: 100 },
    { field: 'cost', headerName: 'Cost', width: 100 },
    { field: 'purchase_date', headerName: 'Purchase Date', width: 300 },    
  ];

  const rows = props.orders.map(x => {
    return {
      "id": x['order_id'],
      "user_id": x['user_id'],
      "product_id": x['product_id'],
      "product_name": x['product_name'],
      "amount": x['amount'],
      "cost": x['cost'],
      "purchase_date": x['purchase_date'],
    };
  });

  return (
    <div style={{ height: "100%", width: '100%'}}>
      <Typography variant="h5">Orders in the system</Typography>
      <DataGrid 
        rows={rows} 
        columns={columns} 
        pageSize={7} 
        // checkboxSelection 
      />
    </div>
  );
}