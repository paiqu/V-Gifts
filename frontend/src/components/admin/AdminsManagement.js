import React from 'react';
import Typography from "@material-ui/core/Typography";
import { DataGrid } from '@material-ui/data-grid';

export default function AdminsManagement(props) {
  const token = props.token;
  const columns = [
    { field: "id", headerName: 'Admin ID', width: 150},
    { field: "username", headerName: 'Admin Name', width: 180 },
    { field: "email", headerName: 'Admin Email', width: 250 },
  ];

  const rows = props.admins.map(x => {
    return {
      "id": x["admin_id"],
      "username": x["username"],
      "email": x["email"],
    };
  });

  return (
    <div style={{ height: "100%", width: '100%'}}>
      <Typography>Admins in the system</Typography>
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