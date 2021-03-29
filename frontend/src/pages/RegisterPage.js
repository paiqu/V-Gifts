import React from 'react';
// import NavBar from '../components/NavBar';
import NavBar from '../components/NavBar';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';

function RegisterPage({ setAuth, ...props }) {
    const [infos, setInfos] = React.useState({
      account_name: "",
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

    const [state, setState] = React.useState({
        email_error: false,
        account_error: false,
        password_error: false,
        email_text: "",
        account_text: "",
        password_text: ""
    });

    const handleClick = () => event => {
        setState({
            email_error: false,
            account_error: false,
            password_error: false
        })
    };

    const handleSubmit = (event) => {
        // prevent it from submitting a form
        event.preventDefault();

        // validate if all field have been entered
        // if (!infos.email 
        //     || !infos.password
        //     || !infos.first_name
        //     || !infos.last_name
        //     || !infos.address
        //     || !infos.city
        //     || !infos.country) { return; }
        
        // send the infos to backend
        axios.post('user/register', { ...infos })
          .then((response) => {
              const data = response.data;
              if (data.code === 403) {
                  setState({
                      account_error: true,
                      account_text: "Account name exists"
                  })
              }
              else {
                // mark the user as signed-in in local storage, it will be removed when it is logged out
                setAuth(data.token, data.user_id);

                // direct the user to the market page
                props.history.push('/products');
              }
              
          })
          .catch((err) => {});
    };

    return (
        <div>
            <NavBar />            
            <blockquote className="blockquote text-center" style={{marginTop: 40}}>
                <h1>Become to V-Gift member</h1>
            </blockquote>
            <main className="container">
                <form onSubmit={handleSubmit}>
                    <div className="row" style={{marginTop: 60}}>
                        <div className="col-sm-6 form-group">
                            <TextField 
                                style={{margin: 10}}
                                label="First name"
                                placeholder="Enter First Name Here.." 
                                id="first_name"
                                name="first_name"
                                // onChange={handleChange('first_name')}
                                onChange={handleChange('first_name')}
                                variant="outlined"
                                fullWidth
                                required
                             />
                        </div>
                        <div className="col-sm-6 form-group">
                            <TextField
                                style={{margin: 10}}
                                label="Last name"
                                placeholder="Enter Last Name Here.." 
                                name="last_name"
                                onChange={handleChange('last_name')}
                                variant="outlined"
                                fullWidth
                                required
                            />
                        </div>
                    </div>
                    <div className="form-group">
                        <TextField 
                            error={state.email_error}
                            helperText={state.email_text}
                            style={{margin: 10}}
                            label="E-mail"
                            placeholder="Enter Email Address Here.." 
                            className="form-control" 
                            name="email"
                            onChange={handleChange('email')}
                            variant="outlined"
                            fullWidth
                            required
                        />
                    </div>
                    <div className="form-group">
                        <TextField 
                            error={state.account_error}
                            helperText={state.account_text}
                            style={{margin: 10}}
                            label="Account name"
                            placeholder="Enter your account name here.." 
                            name="account_name"
                            onChange={handleChange('account_name')}
                            onClick={handleClick()}
                            variant="outlined"
                            fullWidth
                            required
                        />
                    </div>
                    <div className="form-group">
                        <TextField 
                            error={state.password_error}
                            helperText={state.password_text}
                            style={{margin: 10}}
                            label="Password"
                            type="password"
                            placeholder="Enter Password Here.." 
                            name="password"
                            onChange={handleChange('password')}
                            variant="outlined"
                            fullWidth
                            required
                        />
                    </div>
                    {/* add a validation function later here */}
                    <div className="form-group">
                        <TextField 
                            error={state.password_error}
                            helperText={state.password_text}
                            style={{margin: 10}}
                            label="Confirmed Password"
                            type="password" 
                            placeholder="Enter Confirmed Password Here.." 
                            name="password"
                            onChange={handleChange('password')} 
                            variant="outlined"
                            fullWidth
                            required   
                        />
                    </div>
                    <div className="form-group">
                        <TextField 
                            style={{margin: 10}}
                            label="Address"
                            // type="password" 
                            placeholder="Enter your Address Here.." 
                            name="address"
                            onChange={handleChange('address')} 
                            variant="outlined"
                            fullWidth
                            required   
                        />
                    </div>
                    <div className="row">
                        <div className="col-sm-6 form-group">
                            <TextField 
                                style={{margin: 10}}
                                label="City"
                                placeholder="Enter City Name Here.." 
                                name="city"
                                onChange={handleChange('city')}
                                variant="outlined"
                                fullWidth
                                required    
                            />
                        </div>
                        <div className="col-sm-6 form-group">
                            <TextField
                                style={{margin: 10}}
                                label="Country"
                                placeholder="Select Country Name Here.." 
                                className="form-control" 
                                name="country"
                                onChange={handleChange('country')}
                                variant="outlined"
                                fullWidth
                                required  
                            />
                        </div>
                    </div>
                    <button type="submit" style={{margin: 10}} className="btn btn-outline-primary">Create profile</button>
                
                </form>
            </main>
        </div>

    );
}

export default RegisterPage;