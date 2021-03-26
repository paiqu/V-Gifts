import React from 'react';
import '../css/login.css';


function LoginPage() {
		const handleSubmit = (event) => {

		}

    return (
        <div>
            <div className="sidenav">
                <div className="login-main-text">
                    <h1><span id="login-yellow">Log in</span> to your<br /> V-Gift account</h1>
                </div>
            </div>
            <main className="main">
                <div className="col-md-6 col-sm-12">
                    <form className="login-form d-flex flex-column" onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label>User Name</label>
                            <input id="login_user_name" type="text" className="form-control" placeholder="User Name" />
                        </div>
                        <div className="form-group">
                            <label>Password</label>
                            <input id="login_user_password" type="password" className="form-control" placeholder="Password" />
                        </div>
                        <button type="button" className="btn btn-primary btn-lg btn-block mb-3">Log in</button>
                        <a role="button" className="btn btn-secondary btn-lg btn-block"  href="/register">Not a member? Sign up</a>
                        <a href="/admin">
                            <button type="button" className="btn btn-light btn-lg btn-block" style={{position: "absolute", bottom: "2rem"}}>Admin Log in</button>
                        </a>
                    </form>
                </div>
            </main>
        </div>
    );
}

export default LoginPage;