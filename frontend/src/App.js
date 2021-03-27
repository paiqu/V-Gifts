import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import './axios';

import AdminPage from './pages/AdminPage';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import ProfilePage from './pages/ProfilePage';
import RegisterPage from './pages/RegisterPage';
import ProductsPage from './pages/ProductsPage';
import { AuthProvider } from './AuthContext';
import ProtectedRoute from './utils/ProtectedRoute';

// https://material.io/resources/color/#!/?view.left=0&view.right=0&secondary.color=2196F3&secondary.text.color=FAFAFA&primary.color=FFC400
const theme = createMuiTheme({
	palette: {
		primary: {
			light: '#fff64f',
			main: '#ffc400',
			dark: '#c79400',
			contrastText: '#000000',
    },
		secondary: {
      light: '#6ec6ff',
      main: '#2196f3',
      dark: '#0069c0',
      contrastText: '#fafafa',
		},
	},
});


function App() {
	// using hooks here to set state for the App
  // eslint-disable-next-line
	const [authDetails, setAuthDetails] = React.useState(
    // localStorage.getItem('token');
		localStorage.getItem('token')
	);


	// define a function to store details into local storage
  // eslint-disable-next-line
	const setAuth = (token, id) => {
		localStorage.setItem('token', token);
		localStorage.setItem('id', id);

		// setAuthDetails(token);
    setAuthDetails(token);
	}
	
  return (
			<ThemeProvider theme={theme}>
				<AuthProvider value={authDetails}>
          <Router>
            <Switch>
              <Route exact path="/" component={HomePage} />
              <Route 
                exact 
                path="/login"
                render={(props) => {
                  return <LoginPage {...props} setAuth={setAuth} />;
                }} 
              />
              <Route 
                exact 
                path="/register" 
                render={(props) => {
                  return <RegisterPage {...props} setAuth={setAuth} />;
                }}  
              />
              <Route exact path="/products" component={ProductsPage} />
              <ProtectedRoute exact path="/profile/:id" component={ProfilePage} />
              <Route exact path="/admin" component={AdminPage} />
            </Switch>
          </Router>
        </AuthProvider>
			</ThemeProvider>
	);
}

export default App;
