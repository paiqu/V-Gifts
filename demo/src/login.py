'''
    This file includes functions related to login/register
    for both user and admin, they are separated functions
    with similar layout. They are always used in different
    website (user only / admin only).
'''
import database as db
from user import *
from admin import *
import hashlib
import re
from generate_token import *


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
        print("Incorrect syntax! You can only use number, letter and underline.")
        return False 

    # Check whether the user name has been registered
    if check_user_exist(name) is True:
        raise Exception("Name is already exist! Please try another one.")

    # Encrypt password 
    encryption = encrypt_password(password)
    # New user added to db
    new_user(name, encryption, email, '')

    return new_user

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
    temp = db.load_json()

    for user_id, user_info in temp['USER_DB'].items():
        if user_info["name"] is name:
            if user_info["password"] == encrypt_password(password):
                login_token = token(name)
                temp['TOKEN_DB'][str(name)] = login_token
                return login_token
    
    print("Login fail! Invalid password or name! Please try again.")
    return False

def logout_user(name):
    '''
        this function logout user
        takes user back to login page
    '''
    temp = db.load_json()
    if check_token(token): 
        del temp['TOKEN_DB'][name]
        print("You have been logged out.")
        return True
    else:
        print("User already logout.")
        return False



# admin part

def register_admin(name, password):
    '''
        this function register admin and initialize their info,
        upon register, webpage should let admin to further
        configure their personal information
        
        calls login_admin()
    '''
    # Filter SQL injection
    pattern = re.compile("[a-zA-Z0-9_]")
    if pattern.search(name) is None:
        print("Incorrect syntax! You can only use number, letter and underline.")
        return False 

    # Check whether the user name has been registered
    if check_admin_exist(name) is True:
        raise Exception("Name is already exist! Please try another one.")

    # Encrypt password 
    encryption = encrypt_password(password)
    # New user added to db
    new_admin(name, encryption, email)

    return new_admin

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
    temp = db.load_json()

    for admin_id, admin_info in temp['ADMIN_DB'].items():
        if admin_info["name"] is name:
            if admin_info["password"] == encrypt_password(password):
                login_token = token(name)
                temp['TOKEN_DB'][str(name)] = login_token
                return login_token
    
    print("Login fail! Invalid password or name! Please try again.")
    return False

def logout_admin(name):
    '''
        this function logout admin
        takes admin back to login page
    '''
    temp = db.load_json()
    if check_token(token):
        del temp['TOKEN_DB'][name]
        print("You have been logged out.")
        return True
    else:
        print("Admin already logout.")
        return False

# Helper function

# Check whether user has already exist when register
def check_user_exist(name):
    temp = db.load_json()
    if temp['USER_DB'] is None:
        return True
    for user_id, user_info in temp['USER_DB'].items():
        if user_info['name'] is name:
            return True
    return False
    
# Check whether admin has already exist when register
def check_admin_exist(name):
    temp = db.load_json()
    if temp['ADMIN_DB'] is None:
        return True
    for admin_id, admin_info in temp['ADMIN_DB'].items():
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
    temp = db.load_json()
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    for user_id, user_info in temp['USER_DB']:
        if user_info['password'] is sha_signature:
            return True
    return False
