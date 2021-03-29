'''
    All tests in this file changes nothing to database.py
'''

import user as us

def test0():
    print(us.show_product_lst(1)) # id: 1, 2, 3
    print(us.show_product_lst(1,1)) # id: 2, 1, 3
    print(us.show_product_lst(2,1)) # empty


if __name__ == "__main__":
    test0()