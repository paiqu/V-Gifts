import React from 'react';
import NavBar from '../components/NavBar';

function ProfilePage(props) {
    return (
        <div>
            <NavBar />
            <main className="d-flex justify-content-center align-items-center flex-column">
                <div className="row justify-content-center pt-3">
                    <div className="col">
                        <img className="img-thumbnail" style={{width: "10rem", height: "auto"}} src="img/profile/profile-1.jpg" alt="" />
                    </div>
                </div>
                <h1 className="mt-3">Hello <span className="text-primary">Pai</span>!</h1>
                <h2>Here's your account details</h2>

                <div className="d-grid container-fluid w-75">
                    <hr />
                    <div className="row">
                        <div className="col d-flex flex-column align-items-center">
                            <button className="btn btn-dark btn-lg w-75">
                                <i className="bi bi-book"></i> Your orders
                            </button>
                        </div>
                        <div className="col d-flex flex-column align-items-center">
                            <button className="btn btn-dark btn-lg w-75">
                                <i className="bi bi-house-door"></i> Your addresses
                            </button>
                        </div>
                        <div className="col d-flex flex-column align-items-center">
                            <button className="btn btn-dark btn-lg w-75">
                                <i className="bi bi-wallet2"></i> Your payments
                            </button>
                        </div>
                    </div>

                </div>

            </main>
        </div>
    );
}

export default ProfilePage;