import user
import admin
import database as db
from login import *
from user import * 


# User part

def test_user_register():
    # Check the format of name
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    #assert register_user("'", '', '', '123456','123@unsw.com','', '', '') == False
    #assert register_user("    ",'','', '123456','123@unsw.com','','','') == False

    register_user('Chenkai','Chenkai','lyu', '123456','123@unsw.com', '','','')

    temp_2 = db.load_json()
    assert temp_2['USER_ID'] == 1
    assert len(temp_2['USER_DB']) == 1
    
    assert temp_2['USER_DB']['1']['name'] == 'Chenkai'
    assert temp_2['USER_DB']['1']['id'] == 1
    assert temp_2['USER_DB']['1']['email'] == '123@unsw.com'

    register_user('Wang', '','','111111', 'x@unsw','','','')
    temp_3 = db.load_json()
    assert temp_3['USER_ID'] == 2
    assert len(temp_3['USER_DB']) == 2
    assert len(temp_3['TOKEN_DB']) == 2

def test_user_login():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    
    new = register_user('Chenkai','Chenkai','lyu', '123456','123@unsw.com', '','','')
    user_id = new['id']

    assert login_user('Chenkai', '111') == False
    assert login_user('Chen', '123456') == False
    
    
    logout_user(user_id)
    temp_2 = db.load_json()
    assert len(temp_2['TOKEN_DB']) == 0

    login_user('Chenkai', '123456')
    temp_3 = db.load_json()
    assert len(temp_3['TOKEN_DB']) == 1 

def test_user_logout():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    
    new = register_user('Chenkai','Chenkai','lyu', '123456','123@unsw.com', '','','')
    user_id = new['id']
    temp_2 = db.load_json()
    assert logout_user(user_id) == True
    temp_3 = db.load_json()
    assert len(temp_3['TOKEN_DB']) == 0
    

def test_change_password():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)

    new = register_user('Chenkai','Chenkai','lyu', '123456','123@unsw.com', '','','')
    token = new['token']
    temp_2 = db.load_json()

    assert change_password(token, '221313', '000000') == False
    assert change_password(token, '123456', '000000') == True
    temp_3 = db.load_json()
    assert change_password(token, '000000', '999') == False
    
# Admin part

def test_admin_register():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    

    # Check the format of name
    assert register_admin("'", '123456', 'god@unsw') == False
    assert register_admin("    ", '123456', 'qq@unsw') == False

    register_admin('God', '123456', 'god@unsw')
    temp_2 = db.load_json()
    assert temp_2['ADMIN_ID'] == 1
    assert len(temp_2['ADMIN_DB']) == 1
   
    assert temp_2['ADMIN_DB']['1']['name'] == 'God'
    assert temp_2['ADMIN_DB']['1']['id'] == 1
    assert temp_2['ADMIN_DB']['1']['email'] == 'god@unsw'

    register_admin('Queen', '111111', 'queen@unsw')
    temp_3 = db.load_json()
    assert temp_3['ADMIN_ID'] == 2
    assert len(temp_3['ADMIN_DB']) == 2

def test_admin_login():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    
    register_admin('God', '123456', 'god@unsw')

    assert login_admin('God', '111') == False
    assert login_admin('GGG', '123456') == False

    token = login_admin('God', '123456')
    temp_2 = db.load_json()
    assert len(temp_2['TOKEN_DB']) == 1 

def test_admin_logout():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    
    new = register_admin('God', '123456', 'god@unsw')
    admin_id = new['id']
    temp_2 = db.load_json()
    print(temp_2['TOKEN_DB'])
    assert logout_admin(admin_id) == True
    temp_3 = db.load_json()
    assert len(temp_3['TOKEN_DB']) == 0


    
