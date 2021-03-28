'''
    This fill contains function related to admin
'''
'''
ADMIN_DB = {
    # format:
    '<id>':{                # type: string
        'id': 2             # type: int, serial
        'name': 'YYF'       # type: string
        'admin_token': '198ANFu72oDJ0827'
                            # type: string
    }
}
'''

import database as db

# class Admin:
#     def __init__(name, password, email):
#         self.id = None
#         self.name = name
#         self.password = password
#         self.email = email

# init

def new_admin(name, password, email):
    new_id = db.id_generator('admin')
    return {
        "id": new_id,
        "name": name,
        "password": password,
        "email": email
    }

def new_product(name, price, description, category, deli_days):
    '''
        create a new product,
        category should be a lst of int with length of
        TYPE_OF_PRODUCTS
    '''
    new_id = db.id_generator('product')
    assert db.check_interest_dim(category)
    return {
        "id": new_id,
        "name": name,
        "price": price,
        "description": description,
        "category": category, # [0] * temp['TYPE_OF_PRODUCTS']
        "delivery": deli_days,
        "ratings": [],
                    # [(u_id, rating), ...]
        "pic": None
    }


# editors

def edit_admin(admin_id, name, password, email):
    '''
        This function edits admin info with inputs above
        and returns the id of this admin
    '''
    temp = db.load_json()
    if str(admin_id) not in temp['ADMIN_DB']:
        raise KeyError()
    temp['ADMIN_DB'][str(admin_id)]["name"] = name
    temp['ADMIN_DB'][str(admin_id)]["password"] = password
    temp['ADMIN_DB'][str(admin_id)]["email"] = email
    return {
        'id': admin_id
    }

def edit_product(prod_id, prod_name, prod_category, prod_descrip):
    '''
        This function edits product info with inputs above
        and returns the id of this product
    '''
    temp = db.load_json()
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    temp['PRODUCT_DB'][str(prod_id)]["name"] = prod_name
    assert db.check_interest_dim(prod_category)
    temp['PRODUCT_DB'][str(prod_id)]["category"] = prod_category
    temp['PRODUCT_DB'][str(prod_id)]["description"] = prod_descrip
    return {
        'id': prod_id
    }

def delete_product(prod_id):
    '''
        This function deletes a product by id
        and returns the id of this product
    '''
    temp = db.load_json()
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    else:
        return temp['PRODUCT_DB'].pop(str(prod_id))

def edit_prod_category(prod_id, category_lst):
    '''
        This function can update the category vector of a product
    '''
    db.valid_id('product', prod_id)
    temp = db.load_json()
    if len(category_lst) != temp['TYPE_OF_PRODUCTS']:
        raise ValueError()
        return {}
    else:
        temp['PRODUCT_DB'][str(prod_id)]['category'] = category_lst
        db.to_json(temp)
    return {}

def change_order_state(order_id, new_state):
    '''
        Thi function changes the delivery state of an order
        # 0: just purchase
        # 1: delivering
        # 2: done
        # 3: cancelled
    '''
    assert new_state in [0,1,2,3]
    db.valid_id('order', order_id)
    temp = db.load_json()
    temp['ORDER_DB'][str(order_id)]['state'] = new_state
    db.to_json(temp)
    return {
        'id': order_id,
        'state': new_state
    }

def get_user_list():
    '''
        This functions returns all user's basic info for admin
    '''
    temp = db.load_json()
    rt = []
    for key in temp['USER_DB'].keys():
        rt.append({
            'user_id' :temp['USER_DB'][key]['id'],
            'account_name' :temp['USER_DB'][key]['name'],
            'first_name' :temp['USER_DB'][key]['fname'],
            'last_name' :temp['USER_DB'][key]['lname']
        })
    return rt

# def order_history():
#     '''
#         This function doen't have a purpose yet.
#     '''
#     return {}