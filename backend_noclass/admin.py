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

def new_product(name, description, feature):
    '''
        create a new product,
        feature should be a lst of int with length of
        TYPE_OF_PRODUCTS
    '''
    new_id = db.id_generator('product')
    assert db.check_interest_dim(feature)
    return {
        "id": new_id,
        "name": name,
        "description": description,
        "feature": feature,
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
    temp['ADMIN_DB'][str(prod_id)]["name"] = name
    temp['ADMIN_DB'][str(prod_id)]["password"] = password
    temp['ADMIN_DB'][str(prod_id)]["email"] = email
    return {
        'id': admin_id
    }

def edit_product(prod_id, prod_name, prod_feature, prod_descrip):
    '''
        This function edits product info with inputs above
        and returns the id of this product
    '''
    temp = db.load_json()
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    temp['PRODUCT_DB'][str(prod_id)]["name"] = prod_name
    assert db.check_interest_dim(prod_feature)
    temp['PRODUCT_DB'][str(prod_id)]["feature"] = prod_feature
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

# def order_history():
#     '''
#         This function doen't have a purpose yet.
#     '''
#     return {}