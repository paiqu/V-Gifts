'''
    All tests in this file changes nothing to database.py
'''

import user as us
import database as db

def test0():
    print(us.show_product_lst(1)) # id: 1, 2, 3
    print(us.show_product_lst(1,1)) # id: 2, 1, 3
    print(us.show_product_lst(2,1)) # empty

def test1():
    # us.remove_prod_from_cart(1, us.show_user_cart(1)[0])
    print(us.show_all_cart(1))
    us.add_product_to_cart(1, 1, 1)
    print(us.show_all_cart(1))
    us.add_product_to_cart(1, 1, 1)
    print(us.show_all_cart(1))
    us.change_cart_amount(1, 0, 3)
    print(us.show_all_cart(1))
    us.change_cart_amount(1, 0, 0)
    print(us.show_all_cart(1))

def test2():
    print(us.show_all_order(1, 1))


if __name__ == "__main__":
    # test0()
    test1()
    # test2()
    # print("===============================")
    # temp = db.load_json()
    # db.pretty_print(temp)