'''
    Testing database read and write
'''
import database as db
# import user as us
import admin as ad

# test 0
def test_0():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    temp_2 = db.load_json()
    assert temp_2['USER_ID'] == 0
    assert temp_2['ADMIN_ID'] == 0
    assert temp_2['ORDER_ID'] == 0
    assert temp_2['PRODUCT_ID'] == 0
    assert len(temp_2['USER_DB']) == 0
    assert len(temp_2['ADMIN_DB']) == 0
    assert len(temp_2['ORDER_DB']) == 0
    assert len(temp_2['PRODUCT_DB']) == 0

def test_1():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    # add some product/user/admin
    admin_1 = ad.new_admin('admin','123456','123@unsw')
    prod_1 = ad.new_product('prod_1', 50, 'test_use', [1, 0, 0], 5)
    db.add_admin(admin_1)
    db.add_prod(prod_1)
    # testing
    temp_2 = db.load_json()
    assert temp_2['USER_ID'] == 0
    assert temp_2['ADMIN_ID'] == 1
    assert temp_2['ORDER_ID'] == 0
    assert temp_2['PRODUCT_ID'] == 1
    assert len(temp_2['USER_DB']) == 0
    assert len(temp_2['ADMIN_DB']) == 1
    assert len(temp_2['ORDER_DB']) == 0
    assert len(temp_2['PRODUCT_DB']) == 1
    print(temp_2)

if __name__ == "__main__":
    test_0()
    test_1()