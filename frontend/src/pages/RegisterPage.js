import React from 'react';
import NavBar from '../components/NavBar';
import axios from 'axios';
import { event } from 'jquery';

function RegisterPage(props) {
    const [infos, setInfos] = React.useState({
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        address: "",
        city: "",
        country: ""
    });

    const handleChange = name => event => {
        setInfos({
            ...infos,
            [name]: event.target.value
        });
    };

    const handleSubmit = (event) => {
        // prevent it from submitting a form
        event.preventDefault();

        // validate if all field have been entered
        if (!infos.email 
            || !infos.password
            || !infos.first_name
            || !infos.last_name
            || !infos.address
            || !infos.city
            || !infos.country) { return; }
        
        // send the infos to backend
        axios.post('/auth/register', { ...infos }
            .then((response) => {
                console.log(response);
                const data = response.data;
                // passed in a function from outside to authorise user later
                
                // direct the user to the market page
                props.history.push('/market');
            })
            .catch((err) => {})
        );
    };

    return (
        <div>
            <NavBar />            
            <blockquote className="blockquote text-center" style={{marginTop: 40}}>
                <h1>Become to V-Gift member</h1>
            </blockquote>
            <main className="container">
                <form onSubmit={handleSubmit}>
                    <div className="row" style={{marginTop: 80}}>
                        <div className="col-sm-6 form-group">
                            <label>First Name</label>
                            <input 
                                type="text"
                                placeholder="Enter First Name Here.." 
                                className="form-control"
                                id="first_name"
                                name="first_name"
                                onChange={handleChange('first_name')}
                                required
                             />
                        </div>
                        <div className="col-sm-6 form-group">
                            <label>Last Name</label>
                            <input
                                type="text" 
                                placeholder="Enter Last Name Here.." 
                                className="form-control" 
                                name="last_name"
                                onChange={handleChange('last_name')}
                                required
                            />
                        </div>
                    </div>
                    <div className="form-group">
                        <label>Email Address</label>
                        <input 
                            type="text" 
                            placeholder="Enter Email Address Here.." 
                            className="form-control" 
                            name="email"
                            onChange={handleChange('email')}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input 
                            type="password" 
                            placeholder="Enter Password Here.." 
                            className="form-control" 
                            name="password"
                            onChange={handleChange('password')}
                            required
                        />
                    </div>
                    {/* add a validation function later here */}
                    <div className="form-group">
                        <label>Confirmed Password</label>
                        <input 
                            type="password" 
                            placeholder="Enter Password Here.." 
                            className="form-control" 
                            name="password"
                            onChange={handleChange('password')} 
                            required   
                        />
                    </div>
                    <div className="row">
                        <div className="col-sm-6 form-group">
                            <label>City</label>
                            <input 
                                type="text" 
                                placeholder="Enter City Name Here.." 
                                className="form-control" 
                                name="city"
                                onChange={handleChange('city')}
                                required    
                            />
                        </div>
                        <div className="col-sm-6 form-group">
                            <label>Country</label>
                            <input 
                                type="text" 
                                placeholder="Select Country Name Here.." 
                                className="form-control" 
                                name="country"
                                onChange={handleChange('country')}
                                required 
                            />
                        </div>
                    </div>
                    <button type="submit" className="btn btn-lg btn-info">Create profile</button>
                </form>
            </main>
        </div>

    );
}

export default RegisterPage;