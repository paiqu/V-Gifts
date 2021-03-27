import React from 'react';
import AdminDrawer from '../components/AdminDrawer';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({

  }));


function AdminPage(props) {
    const classes = useStyles();

    return (
      <div>
        <AdminDrawer />
      </div>
    );
}

// function AdminPage(props) {
//     return (
//         <div>
//             <NavBar />
//             <main className="d-flex justify-content-center align-items-center flex-column">
//                 <div className="row justify-content-center pt-3">
//                     <div className="col">
//                         <img className="img-thumbnail" style={{width: "10rem", height: "auto"}} src="img/admin/admin-1.png" alt="" />
//                     </div>
//                 </div>
//                 <h1 className="mt-3">Hello Admin <span className="text-primary">Lakitu</span>!</h1>
//                 <h2>Manage your website here</h2>

//                 <div className="d-grid container-fluid w-75 gap-4">
//                     <hr />
//                     <div className="row">
//                         <div className="col d-flex flex-column align-items-end justify-content-center">
//                             <button className="btn btn-dark btn-lg w-50">
//                                 <i className="bi bi-card-checklist"></i> Market Management
//                             </button>
//                         </div>
//                         <div className="col d-flex flex-column align-items-start">
//                             <button className="btn btn-dark btn-lg w-50">
//                                 <i className="bi bi-emoji-smile"></i> Manage Customers Info
//                             </button>
//                         </div>
//                     </div>
//                     <div className="row">
//                         <div className="col d-flex flex-column align-items-end">
//                             <button className="btn btn-dark btn-lg w-50">
//                                 <i className="bi bi-cash"></i> Manage Orders
//                             </button>
//                         </div>
//                         <div className="col d-flex flex-column align-items-start">
//                             <button className="btn btn-dark btn-lg w-50">
//                                 <i className="bi bi-chat-left-text"></i> Received Requests
//                             </button>
//                         </div>
//                     </div>
//                 </div>
//             </main>
//         </div>
//     );
// }

export default AdminPage;