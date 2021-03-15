import React from 'react';

function RegisterPage(props) {
    return (
        <div>
            <nav id="my-nav" className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <a className="navbar-brand" href="/">V-Gifts</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse navbar-right d-flex" id="navbarNavDropdown">
                        <ul className="navbar-nav flex-grow-1">
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="products-page.html">Market</a>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Categories
                                </a>
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                    <li><a className="dropdown-item" href="#">For Him</a></li>
                                    <li><a className="dropdown-item" href="#">For Her</a></li>
                                    <li><a className="dropdown-item" href="#">For Babbies</a></li>
                                    <li><a className="dropdown-item" href="#">For Pets</a></li>
                                    <li><a className="dropdown-item" href="#">Customize</a></li>
                                </ul>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Contact</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">About us</a>
                            </li>
                            <li className="nav-item flex-grow-1">
                                <form className="d-flex">
                                    <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                                    <button className="btn btn-outline-success" type="submit">Search</button>
                                </form>
                            </li>
                        </ul>
                        <ul className="navbar-nav ml-auto nav-flex-icons navbar-right">
                            <li className="nav-item">
                                <a className="nav-link">
                                    <button type="button" className="btn btn-light"><i className="bi bi-cart"></i>Cart</button>
                                </a>
                            </li>
            
                            <li className="nav-item">
                                <a className="nav-link" href="profile-page.html">
                                    <button type="button" className="btn btn-primary"><i className="bi bi-person-fill"></i>My Account</button>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            
            <blockquote className="blockquote text-center" style={{marginTop: 40}}>
                <h1>Become to V-Gift member</h1>
            </blockquote>
            <main className="container">
                <form>
                    <div className="row" style={{marginTop: 80}}>
                        <div className="col-sm-6 form-group">
                            <label>First Name</label>
                            <input type="text" placeholder="Enter First Name Here.." className="form-control" />
                        </div>
                        <div className="col-sm-6 form-group">
                            <label>Last Name</label>
                            <input type="text" placeholder="Enter Last Name Here.." className="form-control" />
                        </div>
                    </div>
                    <div className="form-group">
                        <label>Email Address</label>
                        <input type="text" placeholder="Enter Email Address Here.." className="form-control" />
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input type="password" placeholder="Enter Password Here.." className="form-control" />
                    </div>
                    <div className="form-group">
                        <label>Confirmed Password</label>
                        <input type="password" placeholder="Enter Password Here.." className="form-control" />
                    </div>
                    <div className="row">
                        <div className="col-sm-6 form-group">
                            <label>City</label>
                            <input type="text" placeholder="Enter City Name Here.." className="form-control" />
                        </div>
                        <div className="col-sm-6 form-group">
                            <label>Country</label>
                            <input type="text" placeholder="Select Country Name Here.." className="form-control" />
                        </div>
                    </div>
                    <button type="button" className="btn btn-lg btn-info">Create profile</button>
                </form>
            </main>
        </div>

    );
}

export default RegisterPage;