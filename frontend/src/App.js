import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';

import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';

class App extends React.Component  {
  render() {
    return (
		<Router>
			<Switch>
				<Route exact path="/" component={HomePage} />
				<Route exact path="/login" component={LoginPage} />
			</Switch>
		</Router>
	);
  }
}

export default App;
