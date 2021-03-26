import React from 'react';
import { Redirect, Route } from 'react-router-dom';
import AuthContext from '../AuthContext';

export default function ProtectedRoute(props) {
  const id = React.useContext(AuthContext);
  console.log(id);
  if (!id) {
    return <Redirect to="/login" />;
  }
  return <Route {...props} />;
}
