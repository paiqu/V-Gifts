import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';

import AdminPage from './pages/AdminPage';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import ProfilePage from './pages/ProfilePage';
import RegisterPage from './pages/RegisterPage';
import ProductsPage from './pages/ProductsPage';

class App extends React.Component  {
  render() {
    return (
		<Router>
			<Switch>
				<Route exact path="/" component={HomePage} />
				<Route exact path="/login" component={LoginPage} />
				<Route exact path="/register" component={RegisterPage} />
				<Route exact path="/products" component={ProductsPage} />
				{/* <Route exact path="/profile" component={ProfilePage} /> */}
				<Route exact path="/admin" component={AdminPage} />
			</Switch>
		</Router>
	);
  }
}

export default App;
