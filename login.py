'''
    This file includes functions related to login/register
    for both user and admin, they are separated functions
    with similar layout. They are always used in different
    website (user only / admin only).
'''

# user part
def register_user(name, password):
    '''
        this function register user and initialize their info,
        upon register, webpage should let user to further
        configure their personal information

        calls login_user()
    '''
    return {
        'id': 1,
        'name': name,
    }

def login_user(name, password):
    '''
        this function login user
        returns user_id
    '''
    return {
        'id': 1,
        'name': name,
    }
#import hashlib
def encrypt_password(password):
    '''
    Encrypt the password with sha256 and store in database
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    '''
    return sha_signature
    
def logout_user(id):
    '''
        this function logout user
        takes user back to login page
    '''
    return {
    }



# admin part

def register_admin(name, password):
    '''
        this function register admin and initialize their info,
        upon register, webpage should let admin to further
        configure their personal information
        
        calls login_admin()
    '''
    return login_admin(name, password)
    # return {
    #     'id': 1,
    #     'name': name,
    # }

def login_admin(name, password):
    '''
        this function login admin
        returns admin_id
    '''
    return {
        'id': 1,
        'name': name,
    }

def logout_admin(id):
    '''
        this function logout admin
        takes admin back to login page
    '''
    return {
    }

# User forget password and reset
def forget_password(name, email):
    '''
    Check the email exist
    Send reset url to the email
    return new password
    '''
    return new_password

# Users change password
def change_password(name,old_password):
    '''
    Check the name and password match
    Reset the password
    '''
    return new_password
