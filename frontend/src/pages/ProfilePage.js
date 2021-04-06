import React from 'react';
import axios from 'axios';
import AuthContext from '../AuthContext';
import UserDrawer from '../components/UserDrawer';

export default function ProfilePage(props) {
	// const { profile } = props.match.params;
	const token = React.useContext(AuthContext).user;
  const [profile, setProfile] = React.useState({
    "first_name": "",
    "last_name": "",
    "username": "",
    "email": "",
    "address": "",
    "fund": 0,
  });

	React.useEffect((() => {
		axios.get('/user/profile', { 
      params: {
        token,
      }
    })
    .then((response) => {
      const data = response.data;

      setProfile({
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "username": data["username"],
        "email": data["email"],
        "address": data["address"],
        "fund": data["fund"],
      });
    })
    .catch((err) => {});
	}), [token]);
    
  return (
    <div>
      <UserDrawer profile={profile} history={props.history}/>
    </div>
  );

}

// function ProfilePage(props) {
//   const id = React.useContext(AuthContext);

//   const handleLogout = (event) => {
//     axios.post('/user/logout', { id })
//       .then((response) => {
//         console.log(response);

//         localStorage.removeItem('id');
        
//         // after log out, redirect to home page
//         props.history.push('/');
//       })
//       .catch((err) => {});

//   };

//   return (
//         <div>
//             <NavBar />
//             <main className="d-flex justify-content-center align-items-center flex-column">
//                 <div className="row justify-content-center pt-3">
//                     <div className="col">
//                         <img className="img-thumbnail" style={{width: "10rem", height: "auto"}} src="/img/profile/profile-1.jpg" alt="" />
//                     </div>
//                 </div>
//                 <h1 className="mt-3">Hello <span className="text-primary">Pai</span>!</h1>
//                 <h2>Here's your account details</h2>

//                 <div className="d-grid container-fluid w-75">
//                     <hr />
//                     <div className="row">
//                         <div className="col d-flex flex-column align-items-center">
//                             <button className="btn btn-dark btn-lg w-75">
//                                 <i className="bi bi-book"></i> Your orders
//                             </button>
//                         </div>
//                         <div className="col d-flex flex-column align-items-center">
//                             <button className="btn btn-dark btn-lg w-75">
//                                 <i className="bi bi-house-door"></i> Your addresses
//                             </button>
//                         </div>
//                         <div className="col d-flex flex-column align-items-center">
//                             <button className="btn btn-dark btn-lg w-75">
//                                 <i className="bi bi-wallet2"></i> Your payments
//                             </button>
//                         </div>
//                     </div>
//                     <Button 
//                       variant="contained" 
//                       color="primary"
//                       onClick={handleLogout}
//                     >
//                       Log out
//                     </Button>

//                 </div>

//             </main>
//         </div>
//     );
// }

// export default ProfilePage;