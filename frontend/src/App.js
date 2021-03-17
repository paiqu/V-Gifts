import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// import './App.css';

import AdminPage from './pages/AdminPage';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import ProfilePage from './pages/ProfilePage';
import RegisterPage from './pages/RegisterPage';
import ProductsPage from './pages/ProductsPage';

function App() {
	// using hooks here to set state for the App
	const [authDetails, setAuthDetails] = React.useState(
		localStorage.getItem('token')
	);

	// define a function to store details into local storage
	const setAuth = (token, u_id) => {
		localStorage.setItem('token', token);
		localStorage.setItem('u_id', u_id);
		setAuthDetails(token);
	}
	

    return (
		<Router>
			<Switch>
				<Route exact path="/" component={HomePage} />
				<Route exact path="/login" component={LoginPage} />
				<Route exact path="/register" component={RegisterPage} />
				<Route exact path="/products" component={ProductsPage} />
				<Route exact path="/profile" component={ProfilePage} />
				<Route exact path="/admin" component={AdminPage} />
			</Switch>
		</Router>
	);
}

export default App;
