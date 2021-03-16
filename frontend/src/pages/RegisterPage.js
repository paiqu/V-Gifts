import React from 'react';
import NavBar from '../components/NavBar';

function RegisterPage(props) {
    return (
        <div>
            <NavBar />            
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