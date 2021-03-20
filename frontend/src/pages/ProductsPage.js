import React from 'react';
import NavBar from '../components/NavBar';
import '../css/products-page.css';
import Product from '../components/Product';


function ProductsPage(props) {
    const products = ["mario-1", "mario-2", "mario-3"];
    const items = [];
    for (let i = 0; i < 3; i++) {
        items.push(<Product name={products[i]}/>);
    }
    return (
        <div>
            <NavBar />
            {items}
        </div>
    );
}

// function ProductsPage(props) {
//     return (
//         <div>
//             <NavBar />
//             <main className="d-flex justify-content-center align-items-center flex-column">
//                 <div className="products-grid container-fluid w-75 d-grid gap-2">
//                     <div className="row">
//                         <div className="product-info col d-flex flex-column align-items-center me-2">
//                             <img className="mt-1" src="img/products/product_1.jpeg" alt="" />
//                             <p className="fs-3">Mario 1</p>
//                             <p className="fs-4">$299</p>
//                             <button className="btn btn-primary mb-2">
//                                 <i className="bi bi-cart-plus add-cart-icon"></i>
//                             </button>
//                         </div>
//                         <div className="product-info col d-flex flex-column align-items-center me-2">
//                             <img className="mt-1" src="img/products/product_2.jpeg" alt="" />
//                             <p className="fs-3">Mario 2</p>
//                             <p className="fs-4">$299</p>
//                             <button className="btn btn-primary mb-2">
//                                 <i className="bi bi-cart-plus add-cart-icon"></i>
//                             </button>
//                         </div>
//                         <div className="product-info col d-flex flex-column align-items-center me-2">
//                             <img className="mt-1" src="img/products/product_3.jpeg" alt="" />
//                             <p className="fs-3">Mario 3</p>
//                             <p className="fs-4">$299</p>
//                             <button className="btn btn-primary mb-2">
//                                 <i className="bi bi-cart-plus add-cart-icon"></i>
//                             </button>
//                         </div>
//                     </div>
//                     <div className="row">
//                         <div className="product-info col d-flex flex-column align-items-center me-2">
//                             <img className="mt-1" src="img/products/product_1.jpeg" alt="" />
//                             <p className="fs-3">Mario 1</p>
//                             <p className="fs-4">$299</p>
//                             <button className="btn btn-primary mb-2">
//                                 <i className="bi bi-cart-plus add-cart-icon"></i>
//                             </button>
//                         </div>
//                         <div className="product-info col d-flex flex-column align-items-center me-2">
//                             <img className="mt-1" src="img/products/product_2.jpeg" alt="" />
//                             <p className="fs-3">Mario 2</p>
//                             <p className="fs-4">$299</p>
//                             <button className="btn btn-primary mb-2">
//                                 <i className="bi bi-cart-plus add-cart-icon"></i>
//                             </button>
//                         </div>
//                         <div className="product-info col d-flex flex-column align-items-center me-2">
//                             <img className="mt-1" src="img/products/product_3.jpeg" alt="" />
//                             <p className="fs-3">Mario 3</p>
//                             <p className="fs-4">$299</p>
//                             <button className="btn btn-primary mb-2">
//                                 <i className="bi bi-cart-plus add-cart-icon"></i>
//                             </button>
//                         </div>
//                     </div>
//                 </div>
//                 <div className="container-fluid w-75 d-flex flex-column align-items-center">
//                     <p className="mt-3">Page 1 of 15</p>
//                     <div className="d-flex mb-3 btn-group">
//                         <button className="btn btn-lg btn-secondary" href="#">Last Page</button>
//                         <button className="btn btn-lg btn-primary ms-3">Next Page</button>
//                     </div>
//                 </div>
//             </main>
//         </div>
//     );
// }

export default ProductsPage;