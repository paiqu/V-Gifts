import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';

import AdminPage from './pages/AdminPage';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import ProfilePage from './pages/ProfilePage';
import RegisterPage from './pages/RegisterPage';
import ProductsPage from './pages/ProductsPage';


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


class App extends React.Component  {
  render() {
    return (
			<ThemeProvider theme={theme}>
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
			</ThemeProvider>
	);
  }
}

export default App;
