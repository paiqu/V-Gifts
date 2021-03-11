'''
    This file includes functions related to login/register
    for both user and admin, they are separated functions
    with similar layout. They are always used in different
    website (user only / admin only).
'''
import database
import user
import hashlib
import re

# user part
def register_user(name, password, email):
    '''
        this function register user and initialize their info,
        upon register, webpage should let user to further
        configure their personal information

        calls login_user()
    '''
    # Filter SQL injection
    pattern = re.compile("[a-zA-Z0-9_]")
    if pattern.search(name) is None:
        print("Incorrect user name! Please try again.")
        return false 

    # Check whether the user name has been registered
    try:
        check_user_exist(name)
    except:
        print("Name is already exist! Please try another one.")

    # Encrypt password 
    encrypt_password = encrypt_password(password)
    # One more user added into ID_DB["USER_DB"]
    number_of_exist_user = ID_DB["USER_DB"]
    ID_DB["USER_DB"] += 1
    new_user = user(name, encrypt_password, email)
    new_user.id = number_of_exist_user
    # Transfer new user object to a dict
    USER_DB[str(number_of_exist_user)] = new_user.to_dict()

    return new_user

# Login user
def login_user(name, password):
    '''
        this function login user
        returns user_id
    '''
    pattern = re.compile("[a-zA-Z0-9_]")
    
    if pattern.search(name) is None:
        print("Incorrect user name! Please try again.")
        return false

    for user_name in USER_DB:
        if user_name["password"] = encrypt_password(password)
            token = token(name)
    token_DB[str(name)] = token
    return token
    
    
def logout_user(name):
    '''
        this function logout user
        takes user back to login page
    '''
    token_DB.pop[str(name)]
    return true



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


# Helper function

# Check whether user has already exist when register
def check_user_exist(name):
    for user_list in USER_DB:
        for user_name in user_list["name"]:
            if user_name is name:
                return True
    return False

# Encrypt the password with sha256 and store in database
def encrypt_password(password):

    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    
    return sha_signature

# Verify the password mathch in db
def verify_password(password):
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    for user in USER_DB:
        if user['password'] = sha_signature
            return True
    return False

