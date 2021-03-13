import user
import admin
import database
from login import *


# User part

def test_user_register():
    # Check the format of name
    assert register_user("'", '123456','123@unsw.com') == False
    assert register_user("    ", '123456','123@unsw.com') == False

    register_user('Chenkai', '123456','123@unsw.com')
    assert ID_DB['USER_DB'] == 2
    assert len(USER_DB) == 2
   
    assert USER_DB['2']['name'] == 'Chenkai'
    assert USER_DB['2']['id'] == 2
    assert USER_DB['2']['email'] == '123@unsw.com'

    register_user('Wang', '111111', 'x@unsw')
    assert ID_DB['USER_DB'] == 3
    assert len(USER_DB) == 3

def test_user_login():
    assert login_user('Chenkai', '111') == False
    assert login_user('Chen', '123456') == False

    token = login_user('Chenkai', '123456')
    assert len(TOKEN_DB) == 1 

def test_user_logout():
    assert logout_user('Chenkai', token) == True
    assert len(TOKEN_DB) == 0

def test_change_password():
    token = login_user('Chenkai', '123456')
    assert change_password(token, '221313', '000000') == False
    assert change_password(token, '123456', '000000') == True
    assert change_password(token, '000000', '999') == False
    
# Admin part

def test_admin_register():
    # Check the format of name
    assert register_admin("'", '123456', 'god@unsw') == False
    assert register_admin("    ", '123456', 'qq@unsw') == False

    register_admin('God', '123456', 'god@unsw')
    assert ID_DB['ADMIN_DB'] == 2
    assert len(ADMIN_DB) == 2
   
    assert ADMIN_DB['2']['name'] == 'God'
    assert ADMIN_DB['2']['id'] == 2
    assert ADMIN_DB['2']['email'] == 'god@unsw'

    register_admin('Queen', '111111', 'queen@unsw')
    assert ID_DB['ADMIN_DB'] == 3
    assert len(ADMIN_DB) == 3

def test_admin_login():
    assert login_admin('God', '111') == False
    assert login_admin('GGG', '123456') == False

    token = login_admin('God', '123456')
    assert len(TOKEN_DB) == 1 

def test_admin_logout():
    assert logout_admin('God', token) == True
    assert len(TOKEN_DB) == 0
    
