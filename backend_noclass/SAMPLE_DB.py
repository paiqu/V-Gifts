'''
    This file provides a sample database
'''
import database as db
import user as us
import admin as ad
import webpage as wb
import random as rd

def generate_sample_db_0():
    '''
        Usage:
             [admin_1, user_1, user_2, user_3] = generate_sample_db()
        This function generates a sample DB
        with functions in 
        database.py
        admin.py
        user.py
        webpage.py
    '''
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    # add some product/user/admin
    # admin
    admin_1 = ad.new_admin('admin','123456','123@unsw')
    db.add_admin(admin_1)
    # user
    user_1 = us.new_user('user_1', '123', '123@unsw', 'somewhere')
    user_2 = us.new_user('user_2', '123', '123@unsw', 'somewhere')
    user_3 = us.new_user('user_3', '123', '123@unsw', 'somewhere')
    db.add_user(user_1)
    db.add_user(user_2)
    db.add_user(user_3)
    # prod
    prod_01 = ad.new_product('prod_01', 10,     'test_use', [1, 0, 0],  5)
    prod_02 = ad.new_product('prod_02', 20,     'test_use', [0, 1, 0],  7)
    prod_03 = ad.new_product('prod_03', 50,     'test_use', [0, 0, 1],  2)
    prod_04 = ad.new_product('prod_04', 100,    'test_use', [1, 1, 0],  12)
    prod_05 = ad.new_product('prod_05', 500,    'test_use', [1, 0, 1],  1)
    prod_06 = ad.new_product('prod_06', 1000,   'test_use', [0, 1, 1],  1)
    prod_07 = ad.new_product('prod_07', 15,     'test_use', [1, 1, 1],  5)
    prod_08 = ad.new_product('prod_08', 62,     'test_use', [2, -1, 1], 3)
    prod_09 = ad.new_product('prod_09', 9999,   'test_use', [8, 0, 0],  1)
    prod_10 = ad.new_product('prod_10', 222,    'test_use', [3, 1, -4], 4)
    prod_11 = ad.new_product('prod_11', 315,    'test_use', [2, 0, 0],  5)
    prod_12 = ad.new_product('prod_12', 37345,  'test_use', [1, 2, 1],  30)
    prod_13 = ad.new_product('prod_13', 1,      'test_use', [1, 3, 3],  50)
    prod_14 = ad.new_product('prod_14', 2,      'test_use', [0, 7, 2],  40)
    prod_15 = ad.new_product('prod_15', 5,      'test_use', [1, 1, 1],  10)
    prod_16 = ad.new_product('prod_16', 218,    'test_use', [0, 0, 5],  3)
    prod_17 = ad.new_product('prod_17', 99,     'test_use', [-9, -9, -9], 99)
    prod_18 = ad.new_product('prod_18', 73,     'test_use', [-5, -4, -3], 100)
    prod_19 = ad.new_product('prod_19', 77,     'test_use', [0, -8, 7],   101)
    prod_20 = ad.new_product('prod_20', 64,     'test_use', [-7, 20, -9], 102)
    db.add_prod(prod_01)
    db.add_prod(prod_02)
    db.add_prod(prod_03)
    db.add_prod(prod_04)
    db.add_prod(prod_05)
    db.add_prod(prod_06)
    db.add_prod(prod_07)
    db.add_prod(prod_08)
    db.add_prod(prod_09)
    db.add_prod(prod_10)
    db.add_prod(prod_11)
    db.add_prod(prod_12)
    db.add_prod(prod_13)
    db.add_prod(prod_14)
    db.add_prod(prod_15)
    db.add_prod(prod_16)
    db.add_prod(prod_17)
    db.add_prod(prod_18)
    db.add_prod(prod_19)
    db.add_prod(prod_20)
    # order
    # other pre-settings
    us.edit_user_interest(user_1['id'], [2,1,1])
    us.edit_user_interest(user_2['id'], [0,4,1])
    us.edit_user_interest(user_3['id'], [3,-5,7])
    us.add_fund(user_1['id'], 10000)
    us.add_fund(user_2['id'], 1000)
    us.add_fund(user_3['id'], 100)

    return [admin_1, 
            user_1,
            user_2,
            user_3]

def generate_sample_db_1(prod_num = 50):
    '''
        Usage:
             [admin_1, user_1, user_2, user_3] = generate_sample_db()
        This function generates a sample DB
        with functions in 
        database.py
        admin.py
        user.py
        webpage.py
    '''
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    # add some product/user/admin
    # admin
    admin_1 = ad.new_admin('admin','123456','123@unsw')
    db.add_admin(admin_1)
    # user
    user_1 = us.new_user('user_1', '123', '123@unsw', 'somewhere')
    user_2 = us.new_user('user_2', '123', '123@unsw', 'somewhere')
    user_3 = us.new_user('user_3', '123', '123@unsw', 'somewhere')
    db.add_user(user_1)
    db.add_user(user_2)
    db.add_user(user_3)
    # prod
    for i in range(prod_num):
        name = 'prod' + str(i)
        price = int(rd.randint(1, 500))
        feature = [int(rd.randint(-10, 10)), 
                  int(rd.randint(-10, 10)),
                  int(rd.randint(-10, 10))]
        deli_day = rd.randint(1, 30)
        prod = ad.new_product(name, price, 'test_use', feature, deli_day)
        db.add_prod(prod)
    # other pre-settings
    interest_1 = [int(rd.randint(-10, 10)), 
                  int(rd.randint(-10, 10)),
                  int(rd.randint(-10, 10))]
    interest_2 = [int(rd.randint(-10, 10)), 
                  int(rd.randint(-10, 10)),
                  int(rd.randint(-10, 10))]
    interest_3 = [int(rd.randint(-10, 10)), 
                  int(rd.randint(-10, 10)),
                  int(rd.randint(-10, 10))]
    us.edit_user_interest(user_1['id'], interest_1)
    us.edit_user_interest(user_2['id'], interest_2)
    us.edit_user_interest(user_3['id'], interest_3)
    us.add_fund(user_1['id'], 10000)
    us.add_fund(user_2['id'], 1000)
    us.add_fund(user_3['id'], 100)

    return [admin_1, 
            user_1,
            user_2,
            user_3]