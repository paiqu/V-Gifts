import user
import admin
import database
from login import *
from user import * 


# User part

def test_user_register():
    # Check the format of name
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()

    assert register_user("'", '123456','123@unsw.com') == False
    assert register_user("    ", '123456','123@unsw.com') == False

    register_user('Chenkai', '123456','123@unsw.com')
    assert temp_2['ID_DB']['USER_DB'] == 1
    assert len(temp_2['USER_DB']) == 1
   
    assert temp['USER_DB']['1']['name'] == 'Chenkai'
    assert temp['USER_DB']['1']['id'] == 1
    assert temp['USER_DB']['1']['email'] == '123@unsw.com'

    register_user('Wang', '111111', 'x@unsw')
    assert temp_2['ID_DB']['USER_DB'] == 2
    assert len(temp_2['USER_DB']) == 2

def test_user_login():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()
    register_user('Chenkai', '123456','123@unsw.com')

    assert login_user('Chenkai', '111') == False
    assert login_user('Chen', '123456') == False
    
    token = login_user('Chenkai', '123456')
    assert len(temp_2['TOKEN_DB']) == 1 

def test_user_logout():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()
    register_user('Chenkai', '123456','123@unsw.com')
    token = login_user('Chenkai', '123456')

    assert logout_user('Chenkai', token) == True
    assert len(temp_2['TOKEN_DB']) == 0

def test_change_password():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()
    token = login_user('Chenkai', '123456')

    assert change_password(token, '221313', '000000') == False
    assert change_password(token, '123456', '000000') == True
    assert change_password(token, '000000', '999') == False
    
# Admin part

def test_admin_register():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()

    # Check the format of name
    assert register_admin("'", '123456', 'god@unsw') == False
    assert register_admin("    ", '123456', 'qq@unsw') == False

    register_admin('God', '123456', 'god@unsw')
    assert temp_2['ID_DB']['ADMIN_DB'] == 1
    assert len(temp_2['ADMIN_DB']) == 1
   
    assert temp_2['ADMIN_DB']['1']['name'] == 'God'
    assert temp_2['ADMIN_DB']['1']['id'] == 1
    assert temp_2['ADMIN_DB']['1']['email'] == 'god@unsw'

    register_admin('Queen', '111111', 'queen@unsw')
    assert temp['ID_DB']['ADMIN_DB'] == 2
    assert len(temp_2['TOKEN_DB']) == 2

def test_admin_login():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()
    register_admin('God', '123456', 'god@unsw')

    assert login_admin('God', '111') == False
    assert login_admin('GGG', '123456') == False

    token = login_admin('God', '123456')
    assert len(temp['TOKEN_DB']) == 1 

def test_admin_logout():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()
    register_admin('God', '123456', 'god@unsw')

    assert logout_admin('God', token) == True
    assert len(temp['TOKEN_DB']) == 0
    
