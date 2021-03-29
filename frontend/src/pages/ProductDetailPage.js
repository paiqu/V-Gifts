import React from 'react';
import NavBar from '../components/NavBar';
import Product from '../components/Product';
import axios from 'axios';

export default function ProductDetailPage(props) {
  const id = props.match.params.id;

  return (
    <div>
      <NavBar />
      <Product id={id} />
    </div>
  );
}