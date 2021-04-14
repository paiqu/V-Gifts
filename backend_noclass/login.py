"""
    This file includes functions related to login/register
    for both user and admin, they are separated functions
    with similar layout. They are always used in different
    website (user only / admin only).
"""
import user as us
import database as db 
import admin as ad
import hashlib
import re
import generate_token as gt
import error as err


# User part fuctions 
def register_user(account_name, first_name, last_name, password, email, address, city, country):
    """
        this function register user and initialize their info,
        upon register, webpage should let user to further
        configure their personal information

        Calls login_user() at the end
    """
    # check the if the input account name and email is in valid format
    name_pattern = re.compile("[a-zA-Z0-9_]")
    if name_pattern.search(account_name) is None:
        raise err.InvalidUsername(description = "Incorrect syntax! You can only use number, letter and underline.")
    email_pattern = re.compile("^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$")
    if email_pattern.search(email) is None:
        raise err.InvalidEmail(description = "Incorrect email format! Please try again.")

    # check whether the account name and email has been registered
    if check_user_exist(account_name) is True:
        raise err.UsernameAlreadyExit(description = "Name is already exist! Please try another one.")
    if check_email_exist(email, "USER_DB"):
        raise err.EmailAlreadyExit(description = "Email is already exist! Please try another one.")

    # encrypt password 
    encryption = encrypt_password(password)
    # add new user to databse
    new = us.new_user(account_name, first_name, last_name, encryption, email, address, city, country)
    db.add_user(new)

    # auto login user after register
    return login_user(account_name, password)


def login_user(name, password):
    """
        This function login user
        returns user id and token
    """
    pattern = re.compile("[a-zA-Z0-9_]")
    
    if pattern.search(name) is None:
        raise err.IncorrectUsername(description = "Incorrect account name! Please try again.")

    login_token = ""
    temp = db.load_json()
    uid = 0
    for user_id, user_info in temp["USER_DB"].items():
        if user_info["name"] == name:
            if user_info["password"] == encrypt_password(password):
                login_token = gt.token(name)
                uid = user_id
                temp["TOKEN_DB"][login_token] = uid
                db.to_json(temp)
                return {
                    "id": uid,
                    "token":login_token
                }

    raise err.InvalidPassword(description = "Login fail! Invalid password or account name! Please try again.")

# def logout_user(iid):
def logout_user(token):
    """
        this function logout user
        takes user back to login page
    """
    temp = db.load_json()

    # if us.check_token(iid): 
    if us.check_token_token(token): 
        temp["TOKEN_DB"].pop(token)
        db.to_json(temp)
        print("You have been logged out.")
        return True
    else:
        print("User already logout.")
        return False



# admin part

def register_admin(name, password, email):
    """
        this function register admin and initialize their info,
        upon register, webpage should let admin to further
        configure their personal information
        
        calls login_admin()
    """
    # Filter SQL injection
    pattern = re.compile("[a-zA-Z0-9_]")
    if pattern.search(name) is None:
        raise err.InvalidUsername(description = "Incorrect syntax! You can only use number, letter and underline.")

    email_pattern = re.compile("^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$")
    if email_pattern.search(email) is None:
        raise err.InvalidEmail(description = "Incorrect email format! Please try again.")

    # Check whether the user name has been registered
    if check_admin_exist(name) is True:
        raise err.UsernameAlreadyExit(description = "Name is already exist! Please try another one.")

    if check_email_exist(email, "ADMIN_DB"):
        raise err.EmailAlreadyExit(description = "Email is already exist! Please try another one.")

    # Encrypt password 
    encryption = encrypt_password(password)
    # New user added to db
    new = ad.new_admin(name, encryption, email)
    db.add_admin(new)
    #info = login_admin(name, password)
    

    return login_admin(name, password)

def register_adm_nologin(name, password, email):
    # Filter SQL injection
    pattern = re.compile("[a-zA-Z0-9_]")
    if pattern.search(name) is None:
        raise err.InvalidUsername(description = "Incorrect syntax! You can only use number, letter and underline.")

    email_pattern = re.compile("^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$")
    if email_pattern.search(email) is None:
        raise err.InvalidEmail(description = "Incorrect email format! Please try again.")

    # Check whether the user name has been registered
    if check_admin_exist(name) is True:
        raise err.UsernameAlreadyExit(description = "Name is already exist! Please try another one.")

    if check_email_exist(email, "ADMIN_DB"):
        raise err.EmailAlreadyExit(description = "Email is already exist! Please try another one.")

    # Encrypt password 
    encryption = encrypt_password(password)
    # New user added to db
    new = ad.new_admin(name, encryption, email)
    db.add_admin(new)
    return {}

def login_admin(name, password):
    """
        this function login admin
        returns admin_id
    """
    pattern = re.compile("[a-zA-Z0-9_]")
    
    if pattern.search(name) is None:
        raise err.IncorrectUsername(description = "Incorrect account name! Please try again.")

    login_token = ""
    temp = db.load_json()
    aid = 0
    for admin_id, admin_info in temp["ADMIN_DB"].items():
        if admin_info["name"] == name:
            if admin_info["password"] == encrypt_password(password):
                login_token = gt.token(name)
                aid = admin_id
                temp["TOKEN_DB"][login_token] = aid
                db.to_json(temp)
                return {
                    "id": aid,
                    "token":login_token
                }
    
    raise err.InvalidPassword(description = "Login fail! Invalid password or account name! Please try again.")

def logout_admin(token):
    """
        this function logout admin
        takes admin back to login page
    """
    temp = db.load_json()
    if us.check_token_token(token):
        temp["TOKEN_DB"].pop(token)
        db.to_json(temp)
        print("You have been logged out.")
        return True
    else:
        print("Admin already logout.")
        return False

# Helper function

# Check whether user has already exist when register
def check_user_exist(name):
    temp = db.load_json()
    if temp["USER_DB"] is None:
        return True
    for user_id, user_info in temp["USER_DB"].items():
        if user_info["name"] == name: 
            return True
    return False
    
# Check whether admin has already exist when register
def check_admin_exist(name):
    temp = db.load_json()
    if temp["ADMIN_DB"] is None:
        return True
    for admin_id, admin_info in temp["ADMIN_DB"].items():
        if admin_info["name"] == name: 
                return True
    return False

def check_email_exist(email, option):
    """
        option in ["ADMIN_DB", "USER_DB"]
    """
    temp = db.load_json()
    for idd, info in temp[option].items():
        if info["email"] == email: 
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
    for user_id, user_info in temp["USER_DB"]:
        if user_info["password"] == sha_signature:
            return True
    return False

def token_to_idd(token):
    temp = db.load_json()
    for key, attr in temp["TOKEN_DB"].items():
        if key == token:
            return attr
    raise err.InvalidToken(description = "Invalid token!")