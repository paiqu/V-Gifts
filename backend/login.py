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