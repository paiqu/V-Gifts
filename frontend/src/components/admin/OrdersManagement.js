import React from 'react';
import Typography from "@material-ui/core/Typography";
import { DataGrid } from '@material-ui/data-grid';
import moment from 'moment';



export default function OrdersManagement(props) {

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
      "purchase_date": moment(parseFloat( x['purchase_date']*1000)).format("YYYY-MM-DD HH:mm:ss"),
    };
  });

  return (
    <div style={{ height: "100%", width: '100%'}}>
      <Typography variant="h5">Orders in the system</Typography>
      <DataGrid 
        rows={rows} 
        columns={columns} 
        pageSize={7} 
        autoHeight
        // checkboxSelection 
      />
    </div>
  );
}