'''
    This file is used to test functions in
    webpage.py
'''
import database as db
import user as us
import admin as ad
import webpage as wb

def test0():
    a = [(1, 123), (2, 41), (3, 6345), (4, 12), (5, 222), (6, 321)]

    b = [(1, 123), 
        (2, 41), 
        (3, 6345), 
        (4, 12), 
        (5, 222), 
        (6, 321),
        (7, 124), 
        (8, 2222), 
        (9, 329)]

    # print(wb.sorting_helper([(11, 329)], [(10, 32)], 0))
    # print(wb.sorting_helper([(11, 329)], [(10, 32)], 1))
    print(wb.sorting_merge(a, 0))
    print(wb.sorting_merge(a, 1))
    print(wb.sorting_merge(b, 0))
    print(wb.sorting_merge(b, 1))

def test1():
    a = [1, 1, 1]
    b = [1, 1, 1]
    d = [3, 4, 5]
    c = [0, 0, 0, 4]
    e = [8, 3, 1, 1]
    print(wb.angle_between(a, [0,0,0]))
    print(wb.angle_between(a, b))
    print(wb.angle_between(e, c))
    print(wb.angle_between(c, e))
    print(wb.angle_between(a, d))

def test2():
    a = {
        'a': 'aaa',
        'b': 'bbb'
    }
    for item in a:
        print(item)
        print(a[item])

def test3():
    db.clear_db()
    temp = db.init_db()
    db.to_json(temp)
    # add some product/user/admin
    admin_1 = ad.new_admin('admin','123456','123@unsw')
    prod_1 = ad.new_product('prod_1', 50, 'test_use', [1, 0, 0], 5)
    prod_2 = ad.new_product('prod_2', 100, 'test_use', [1, 1, 0], 20)
    user_1 = us.new_user('user_1', 'user_1', 'user_1', '123', '123@unsw', 'address', 'city', 'country')
    db.add_admin(admin_1)
    db.add_prod(prod_1)
    db.add_prod(prod_2)
    db.add_user(user_1)
    us.add_fund(user_1['id'], 500)
    us.add_product_to_cart(user_1['id'], prod_1['id'], 3)
    us.add_product_to_cart(user_1['id'], prod_1['id'], 4)
    us.add_product_to_cart(user_1['id'], prod_1['id'], 2)
    us.purchase(user_1['id'], [[prod_1['id'],3], [prod_1['id'],4], [prod_1['id'],2]])
    # testing
    temp_2 = db.load_json()
    assert temp_2['USER_DB'][str(user_1['id'])]['fund'] == (500 - (3+4+2)*50)
    print(wb.order_filter_sort(['1','2','3']))
    us.rate_order(user_1['id'], 2, 10)
    us.rate_order(user_1['id'], 1, -5)
    us.rate_order(user_1['id'], 3, 3)
    print(wb.order_filter_sort(['1','2','3'], 'rating'))
    print(wb.order_filter_sort(['1','2','3'], 'amount'))
    ad.change_order_state(1, 2)
    ad.change_order_state(2, 1)
    ad.change_order_state(3, 3)
    print(wb.order_filter_switch(['1','2','3'], 'state', 2, 2))
    print(wb.order_filter([['rating', 3, 5]]))
    # print(db.load_json())
    print(wb.prod_filter([['price', 40, 60]]))

if __name__ == '__main__':
    # test0()
    # test1()
    # test2()
    test3()