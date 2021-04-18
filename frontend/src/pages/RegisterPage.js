import React from 'react';
// import NavBar from '../components/NavBar';
import NavBar from '../components/NavBar';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';

const EXISTED_NAME = 403;
const EXISTED_EMAIL = 408;


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

    const handle_error = () => event => {
        setState({
            email_error: false,
            account_error: false,
            password_error: false,
            email_text: "",
            account_text: "",
            password_text: ""
        })
    };

    const handle_error_email = () => event =>{
        let pattern = /^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$/;
        if (!pattern.test(event.target.value) && event.target.value !== "") {
            setState({
                email_error: true,
                email_text: "Invalid E-mail format"
            });
        }
    };

    const handle_password = () => event =>{
        if (infos.password !== event.target.value && event.target.value !== "" && infos.password !== "") {
            setState({
                password_error: true,
                password_text: "Password does not match"
            });
        }
    };

    const handleSubmit = (event, handleNext) => {
        // prevent it from submitting a form
        event.preventDefault();
        
        handleNext();
        // send the infos to backend
        // axios.post('user/register', { ...infos })
        //   .then((response) => {
        //       const data = response.data;
        //       if (data.code === EXISTED_NAME ) {
        //         setState({
        //           account_error: true,
        //           account_text: "Account name exists"
        //         })
        //       } else if (data.code === EXISTED_EMAIL ) {
        //         setState({
        //           email_error: true,
        //           email_text: "Email exists"
        //         })
        //       }
        //       else {
        //         // mark the user as signed-in in local storage, it will be removed when it is logged out
        //         setAuth(data.token, data.user_id);
                
        //         handleNext();
        //         // direct the user to the market page
        //         // props.history.push('/products');
        //       }
              
        //   })
        //   .catch((err) => {});
    };

    return (
        <div>
            {/* <NavBar />             */}
            <blockquote className="blockquote text-center" style={{marginTop: 40}}>
                <h1>Become to V-Gift member</h1>
            </blockquote>
            <main className="container">
                <form 
                  onSubmit={(e) => {
                    handleSubmit(e, props.handleNext)
                  }}
                >
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
                            onClick={handle_error()}
                            onBlur={handle_error_email()}
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
                            onClick={handle_error()}
                            variant="outlined"
                            fullWidth
                            required
                        />
                    </div>
                    <div className="form-group">
                        <TextField 
                            style={{margin: 10}}
                            label="Password"
                            type="password"
                            placeholder="Enter Password Here.." 
                            name="password"
                            onChange={handleChange('password')}
                            onClick={handle_error()}
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
                            onClick={handle_error()}
                            onBlur={handle_password()}
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