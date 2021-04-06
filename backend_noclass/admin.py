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
import chatbot as ct

# class Admin:
#     def __init__(name, password, email):
#         self.id = None
#         self.name = name
#         self.password = password
#         self.email = email

# init

def new_preset_admin(name, password, email):
    return {
        "id": 1,
        "name": name,
        "password": password,
        "email": email
    }

def new_admin(name, password, email, db_name = 'database.json'):
    new_id = db.id_generator('admin', db_name)
    return {
        "id": new_id,
        "name": name,
        "password": password,
        "email": email
    }

def new_product(name, price, description, category, deli_days, pic_link, db_name = 'database.json'):
    '''
        create a new product,
        category should be a lst of int with length of
        TYPE_OF_PRODUCTS
    '''
    new_id = db.id_generator('product', db_name)
    # assert db.check_interest_dim(category)
    # catagory is now calculated by query_analysis
    category = None
    if description == "" or description is None:
        description = name
        category = ct.query_analysis_test3(name)
    else:
        category = ct.query_analysis_test3(name + '. ' + description)
    return {
        "id": new_id,
        "name": name,
        "price": price,
        "description": description,
        "category": category, # [0] * temp['TYPE_OF_PRODUCTS']
        "delivery": deli_days,
        "ratings": [],
                    # [(u_id, rating), ...]
        "pic": pic_link
    }


# editors

def edit_admin(admin_id, name, password, email, db_name = 'database.json'):
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
    db.to_json(temp, db_name)
    return {
        'id': admin_id
    }

def edit_product(prod_id, prod_name, prod_category, prod_descrip, db_name = 'database.json'):
    '''
        This function edits product info with inputs above
        and returns the id of this product
    '''
    temp = db.load_json(db_name)
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    temp['PRODUCT_DB'][str(prod_id)]["name"] = prod_name
    # assert db.check_interest_dim(prod_category)
    temp['PRODUCT_DB'][str(prod_id)]["category"] = prod_category
    temp['PRODUCT_DB'][str(prod_id)]["description"] = prod_descrip
    db.to_json(temp, db_name)
    return {
        'id': prod_id
    }

def product_id_to_name(prod_id):
    temp = db.load_json()
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    return temp['PRODUCT_DB'][str(prod_id)]["name"]

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
            'user_id': temp['USER_DB'][key]['id'],
            'account_name': temp['USER_DB'][key]['name'],
            'first_name': temp['USER_DB'][key]['fname'],
            'last_name': temp['USER_DB'][key]['lname'],
            'email': temp['USER_DB'][key]['email'],
            'address': temp['USER_DB'][key]['address'],
            'city': temp['USER_DB'][key]['city'],
            'country': temp['USER_DB'][key]['country']
        })
    return rt

# def order_history():
#     '''
#         This function doen't have a purpose yet.
#     '''
#     return {}