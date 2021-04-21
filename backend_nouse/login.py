'''
    This file includes functions related to login/register
    for both user and admin, they are separated functions
    with similar layout. They are always used in different
    website (user only / admin only).
'''
from database import *
from user import *
import hashlib
import re
from generate_token import *
from admin import *

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
        return False 

    # Check whether the user name has been registered
    if check_user_exist(name) is True:
        raise Exception("Name is already exist! Please try another one.")

    # Encrypt password 
    encryption = encrypt_password(password)
    # One more user added into ID_DB["USER_DB"]
    number_of_exist_user = ID_DB['USER_DB'] + 1
    ID_DB["USER_DB"] += 1
    new_user = User(name, encryption, email)
    new_user.id = number_of_exist_user
    # Transfer new user object to a dict
    new_user_dict = new_user.to_dict()
    USER_DB[str(number_of_exist_user)] = new_user_dict

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
        return False

    login_token = ''
    for user_id, user_info in USER_DB.items():
        if user_info["name"] is name:
            if user_info["password"] == encrypt_password(password):
                login_token = token(name)
                TOKEN_DB[str(name)] = login_token
                return login_token
    
    print("Login fail! Invalid password or name! Please try again.")
    return False

    
    
def logout_user(name, token):
    '''
        this function logout user
        takes user back to login page
    '''
    if check_token(token): 
        del TOKEN_DB[name]
        print("You have been logged out.")
        return True
    else:
        print("User already logout.")
        return False



# admin part

def register_admin(name, password, email):
    '''
        this function register admin and initialize their info,
        upon register, webpage should let admin to further
        configure their personal information
        
        calls login_admin()
    '''
    # Filter SQL injection
    pattern = re.compile("[a-zA-Z0-9_]")
    if pattern.search(name) is None:
        print("Incorrect admin name! Please try again.")
        return False 

    # Check whether the user name has been registered
    
    if check_admin_exist(name) is True:
        raise Exception("Name is already exist! Please try another one.")

    # Encrypt password 
    encryption = encrypt_password(password)
    # One more user added into ID_DB["ADMIN_DB"]
    number_of_exist_admin = ID_DB["ADMIN_DB"] + 1
    print(number_of_exist_admin)
    ID_DB["ADMIN_DB"] += 1
    new_admin = Admin(name, encryption, email)
    new_admin.id = number_of_exist_admin
    # Transfer new user object to a dict
    new_admin_dict = new_admin.to_dict()
    ADMIN_DB[str(number_of_exist_admin)] = new_admin_dict

    return new_admin
    # return {
    #     'id': 1,
    #     'name': name,
    # }

def login_admin(name, password):
    '''
        this function login admin
        returns admin_id
    '''
    pattern = re.compile("[a-zA-Z0-9_]")
    
    if pattern.search(name) is None:
        print("Incorrect admin name! Please try again.")
        return False
    
    login_token = ''
    for admin_id, admin_info in ADMIN_DB.items():
        if admin_info["name"] is name and admin_info["password"] == encrypt_password(password):
            login_token = token(name)
            TOKEN_DB[str(name)] = login_token
            return login_token

    print('Invalid password or name! Please try again.')
    return False

def logout_admin(name, token):
    '''
        this function logout admin
        takes admin back to login page
    '''
    if check_token(token):
        del TOKEN_DB[name]
        print("You have been logged out.")
        return True
    else:
        print("Admin already logout.")
        return False

# User forget password and reset
def forget_password(name, email):
    '''
    Check the email exist
    Send reset url to the email
    return new password
    '''
    # Need flask to complete it


    return None

# Users change password
def change_password(token, old_password, new_password):
    '''
    Check the name and password match
    Reset the password
    '''
    
    if check_token(token) is not True:
        print('Invalid Token!')
        return False

    for user_id, user_info in USER_DB.items():
        if user_info["password"] == encrypt_password(old_password):
            user_info["password"] = encrypt_password(new_password)
            logout_user(user_info["name"], token)
            return True
    return False


# Helper function

# Check whether user has already exist when register
def check_user_exist(name):
    if USER_DB is None:
        return True
    for user_id, user_info in USER_DB.items():
        if user_info['name'] is name:
            return True
    return False
    
# Check whether admin has already exist when register
def check_admin_exist(name):
    if ADMIN_DB is None:
        return True
    for admin_id, admin_info in ADMIN_DB.items():
        if admin_info['name'] is name:
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
        if user['password'] is sha_signature:
            return True
    return False

# Check token is available
def check_token(token):
    for name, user_token in TOKEN_DB.items():
        if user_token is token:
            return True
    return False

