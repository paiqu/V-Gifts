'''
    This file includes all database structure for 
    all databases, DO NOT make ANY CHANGE
    without notifying other members. Upon adding new
    attributes, PLEASE do pytest to remove any
    conflict changes.
'''
import json
# main content
# ID_DB = {
#     '''
#         This DB stores the next id should be used upon
#         creating new user/admin/product/order
#     '''
#     'USER_ID': 0,
#     'ADMIN_ID': 0,
#     'PRODUCT_ID': 0,
#     'ORDER_ID': 0,
#     'USER_DB': {},
#     'ADMIN_DB': {},
#     'PRODUCT_DB': {},
#     'ORDER_DB': {},
# }

# global
TYPE_OF_PRODUCTS = 3

def init_db():
    return {
    'TYPE_OF_PRODUCTS': TYPE_OF_PRODUCTS,   # dimension of interests
    'USER_ID': 0,
    'ADMIN_ID': 0,
    'PRODUCT_ID': 0,
    'ORDER_ID': 0,
    'USER_DB': {},
    'ADMIN_DB': {},
    'PRODUCT_DB': {},
    'ORDER_DB': {},
}

# check valid

def valid_id(option, idd):
    '''
        This func checks if an id exist in DB
    '''
    temp = load_json()
    if option == 'user' or option == 'users':
        if str(idd) in temp['USER_DB']:
            return True
    elif option == 'product' or option == 'products':
        if str(idd) in temp['PRODUCT_DB']:
            return True
    elif option == 'admin' or option == 'admins':
        if str(idd) in temp['ADMIN_DB']:
            return True
    elif option == 'order' or option == 'orders':
        if str(idd) in temp['ORDER_DB']:
            return True
    # Temporary
    # invalid id
    raise KeyError()

# read and write

def to_json(DB, filename = 'database.json'):
    '''
        Save DB to json file
    '''
    with open(filename, 'w') as fp:
        json.dump(DB, fp)
    return {}
    # return json.dumps(output)

def load_json(filename = 'database.json'):
    '''
        This function loads database from json
    '''
    # temp = {}
    with open(filename, 'r') as fp:
        temp = json.load(fp)
    return temp

def add_user(user):
    '''
        Add user to db
    '''
    temp = load_json()
    temp['USER_DB'][str(user['id'])] = user
    to_json(temp)
    return {}

def add_admin(admin):
    '''
        Add admin to db
    '''
    temp = load_json()
    temp['ADMIN_DB'][str(admin['id'])] = admin
    to_json(temp)
    return {}

def add_prod(prod):
    '''
        Add product to db
    '''
    temp = load_json()
    temp['PRODUCT_DB'][str(prod['id'])] = prod
    to_json(temp)
    return {}

def add_order(order):
    '''
        Add order to db
    '''
    temp = load_json()
    temp['ORDER_DB'][str(order['id'])] = order
    to_json(temp)
    return {}

def clear_db():
    to_json(init_db())
    return {}

def id_generator(option):
    temp = load_json()
    if option == 'user' or option == 'users':
        temp['USER_ID'] += 1
        to_json(temp)
        return temp['USER_ID']
    elif option == 'product' or option == 'products':
        temp['PRODUCT_ID'] += 1
        to_json(temp)
        return temp['PRODUCT_ID']
    elif option == 'admin' or option == 'admins':
        temp['ADMIN_ID'] += 1
        to_json(temp)
        return temp['ADMIN_ID']
    elif option == 'order' or option == 'orders':
        temp['ORDER_ID'] += 1
        to_json(temp)
        return temp['ORDER_ID']
    else:
        # Temporary
        raise KeyError()

def check_interest_dim(feature):
    temp = load_json()
    if len(feature) == temp['TYPE_OF_PRODUCTS']:
        return True
    else:
        return False

def add_product_type():
    temp = load_json()
    temp['TYPE_OF_PRODUCTS'] += 1
    for key in temp['PRODUCT_DB']:
        temp['PRODUCT_DB'][key]['feature'].append(0)
    for key in temp['USER_DB']:
        temp['USER_DB'][key]['interest'].append(0)
    to_json(temp)
    return temp['TYPE_OF_PRODUCTS']

# USER_DB = {
#     '''
#     format:
#         '<id>':                 # type: string
#                 <User class object>
#             contains:
#             {                
#             'id': 1             # type: int, serial
#             'name': 'Zard'      # type: string
#             'fund': 10          # type: int; unit: $
#             'address': 'Pacific Ocean'
#                                 # type: string
#             'cart': [list of product ID]
#                                 # type: list of int
#             'orders': [list of order ID]
#                                 # type: list of int
#             'interests': [('cheap', 1.0), ...]
#                                 # type: list of tuple, tuple of (feature, weight)
#                                 #                                string,  float
#         }
#     '''
# }

# ADMIN_DB = {
#     '''
#     format:
#         '<id>':{                 # type: string
#                 <Admin class object>
#             contains:
#             {     
#             'id': 2             # type: int, serial
#             'name': 'YYF'       # type: string
#             'admin_token': '198ANFu72oDJ0827'
#                                 # type: string
#         }
#     '''
# }

# PRODUCT_DB = {
#     '''
#     format:
#         '<id>':{                 # type: string
#                 <Product class object>
#             contains:
#             {     
#             'id': 3             # type: int, serial
#             'name': 'gift_1'    # type: string
#             'pic': ??????
#                                 # type: string, website or file name
#             'description': 'good'
#                                 # type: string
#             'feature': ['cheap', 'durable']
#                                 # type: list of string, adjective words
#             'delivery': datetime_object
#                                 # type: leng of time (mm/dd)
#         }
#     '''
# }

# ORDER_DB = {
#     '''
#     format:
#         '<id>':{                 # type: string
#                 <Order class object>
#             contains:
#             {      
#                                         e.g. '<id>' means: '3' for item with 'id': 3
#             'id': 4             # type: int, serial
#             'product_id': 3     # type: int
#             'user_id': 2        # type: int
#             'order_date': datetime_object
#                                 # type: datetime_object
#             'delivery_date': datetime_object
#                                 # type: datetime_object
#             'delivery_state': 0
#                                 # type: int, [0: not delivered,
#                                 #             1: on the way,
#                                 #             2: delivered,
#                                 #             3: cancelled]
#         }
#     '''
# }