'''
    Testing database read and write
'''
import database as db
import user as us
import admin as ad
import webpage as wb
import SAMPLE_DB as samp

# test 0
def test_0():
    print("reset Database")
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()
    assert temp_2['USER_ID'] == 0
    assert temp_2['ADMIN_ID'] == 1
    assert temp_2['ORDER_ID'] == 0
    assert temp_2['PRODUCT_ID'] == 0
    assert len(temp_2['USER_DB']) == 0
    assert len(temp_2['ADMIN_DB']) == 1
    assert len(temp_2['ORDER_DB']) == 0
    assert len(temp_2['PRODUCT_DB']) == 0

def test_1():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    # add some product/user/admin
    admin_1 = ad.new_admin('admin','123456','123@unsw')
    prod_1 = ad.new_product('prod_1', 50, 'test_use', [1, 0, 0], 5, "")
    db.add_admin(admin_1)
    db.add_prod(prod_1)
    # testing
    temp_2 = db.load_json()
    assert temp_2['USER_ID'] == 0
    assert temp_2['ADMIN_ID'] == 2
    assert temp_2['ORDER_ID'] == 0
    assert temp_2['PRODUCT_ID'] == 1
    assert len(temp_2['USER_DB']) == 0
    assert len(temp_2['ADMIN_DB']) == 2
    assert len(temp_2['ORDER_DB']) == 0
    assert len(temp_2['PRODUCT_DB']) == 1
    print(temp_2)

def test_2():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    # add some product/user/admin
    admin_1 = ad.new_admin('admin','123456','123@unsw')
    prod_1 = ad.new_product('prod_1', 50, 'test_use', [1, 0, 0], 5, "")
    user_1 = us.new_user('user_1', 'user_1', 'user_1', '123', '123@unsw', 'somewhere', 'city', 'country')
    db.add_admin(admin_1)
    db.add_prod(prod_1)
    db.add_user(user_1)
    us.add_fund(user_1['id'], 500)
    us.add_product_to_cart(user_1['id'], prod_1['id'], 7)
    us.purchase(user_1['id'], [[prod_1['id'],7],])
    # testing
    temp_2 = db.load_json()
    print(temp_2)
    assert temp_2['USER_DB'][str(user_1['id'])]['fund'] == (500 - 7*50)

def test_3():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    # add some product/user/admin
    admin_1 = ad.new_admin('admin','123456','123@unsw')
    prod_1 = ad.new_product('prod_1', 50, 'test_use', [1, 0, 0], 5, "")
    prod_2 = ad.new_product('prod_2', 30, 'test_use', [1, 1, 1], 5, "")
    user_1 = us.new_user('user_1', 'user_1', 'user_1', '123', '123@unsw', 'somewhere', 'city', 'country')
    db.add_admin(admin_1)
    db.add_prod(prod_1)
    db.add_prod(prod_2)
    db.add_user(user_1)
    us.edit_user_interest(user_1['id'], [2,1,1])
    us.add_fund(user_1['id'], 500)
    temp_2 = db.load_json()
    print(temp_2)
    print(wb.prod_picker(user_1['id']))
    print(wb.prod_recommendation(user_1['id']))

def test_4():
    admin_1, user_1, user_2, user_3 = samp.generate_sample_db_0()
    # db.pretty_print(temp)
    us.add_product_to_cart(user_1['id'], 2, 10)
    us.add_product_to_cart(user_1['id'], 3, 7)
    us.add_product_to_cart(user_1['id'], 7, 1)
    us.add_product_to_cart(user_1['id'], 15, 2)
    sp_cart = us.show_user_cart(user_1['id'])
    print(sp_cart)
    print(len(sp_cart))
    print("====================================")
    us.remove_prod_from_cart(user_1['id'], sp_cart[1])
    us.purchase(user_1['id'], us.show_user_cart(user_1['id']))
    status = us.order_refund(user_1['id'], 1)
    print(status)
    status = us.order_refund(user_1['id'], 2)
    print(status)
    status = us.order_refund(user_1['id'], 3)
    print(status)
    db.pretty_print(db.load_json())

def test_5():
    admin_1, user_1, user_2, user_3 = samp.generate_sample_db_1()
    temp = db.load_json()
    # db.pretty_print(temp)
    recommend = wb.prod_recommendation(user_1['id'])
    print(recommend)

if __name__ == "__main__":
    test_0()
    # test_1()
    # test_2()
    # test_3()
    # test_4()
    # test_5()