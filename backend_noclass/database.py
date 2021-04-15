"""
    This file includes all database structure for 
    all databases, DO NOT make ANY CHANGE
    without notifying other members. Upon adding new
    attributes, PLEASE do pytest to remove any
    conflict changes.
"""
import json
import admin as adm
from chatbot import TEST_KEYWORDS
# main content
# ID_DB = {
#     """
#         This DB stores the next id should be used upon
#         creating new user/admin/product/order
#     """
#     "USER_ID": 0,
#     "ADMIN_ID": 0,
#     "PRODUCT_ID": 0,
#     "ORDER_ID": 0,
#     "USER_DB": {},
#     "ADMIN_DB": {},
#     "PRODUCT_DB": {},
#     "ORDER_DB": {},
# }

# global
TYPE_OF_PRODUCTS_INIT = 11

def init_db_withoutadm():
    return {
        "TYPE_OF_PRODUCTS": TYPE_OF_PRODUCTS_INIT,   # dimension of interests
        "PROD_CATAGORY":["for men", 
                        "for women", 
                        "for children", 
                        "for friends", 
                        "for elder",
                        "for relationship", 
                        "foods", 
                        "tools", 
                        "luxuries",
                        "entertainment", 
                        "working",
                        ],
        "USER_ID": 0,
        "ADMIN_ID": 1,
        "PRODUCT_ID": 0,
        "ORDER_ID": 0,
        "USER_DB": {},
        "ADMIN_DB": {},
        "PRODUCT_DB": {},
        "ORDER_DB": {},
        "TOKEN_DB":{}
    }

def init_db():
    temp = init_db_withoutadm()
    admin = adm.new_preset_admin("admin", "admin", "VictimsCOMP3900@gmail.com")
    temp["ADMIN_DB"][str(admin["id"])] = admin
    return temp

def pretty_print(dct, level = 0, strr = "    "):
    for key in dct.keys():
        for i in range(level):
            print(strr, end = "")
        print(key, ":")
        if isinstance(dct[key], dict):
            pretty_print(dct[key], level+1)
        else:
            for i in range(level+1):
                print(strr, end = "")
            print(dct[key])
    return {}

# check valid

def valid_id(option, idd, db_name = "database.json"):
    """
        This func checks if an id exist in DB
    """
    temp = load_json(db_name)
    if option == "user" or option == "users":
        if str(idd) in temp["USER_DB"]:
            return True
    elif option == "product" or option == "products":
        if str(idd) in temp["PRODUCT_DB"]:
            return True
    elif option == "admin" or option == "admins":
        if str(idd) in temp["ADMIN_DB"]:
            return True
    elif option == "order" or option == "orders":
        if str(idd) in temp["ORDER_DB"]:
            return True
    # Temporary
    # invalid id
    raise KeyError()

# read and write

def to_json(DB, filename = "database.json"):
    """
        Save DB to json file
    """
    with open(filename, "w") as fp:
        json.dump(DB, fp)
    return {}
    # return json.dumps(output)

def load_json(filename = "database.json"):
    """
        This function loads database from json
    """
    # temp = {}
    with open(filename, "r") as fp:
        temp = json.load(fp)
    return temp

def add_user(user, db_name = "database.json"):
    """
        Add user to db
    """
    temp = load_json(db_name)
    temp["USER_DB"][str(user["id"])] = user
    to_json(temp, db_name)
    return {}

def add_admin(admin, db_name = "database.json"):
    """
        Add admin to db
    """
    temp = load_json(db_name)
    temp["ADMIN_DB"][str(admin["id"])] = admin
    to_json(temp, db_name)
    return {}

def add_prod(prod, db_name = "database.json"):
    """
        Add product to db
    """
    temp = load_json(db_name)
    temp["PRODUCT_DB"][str(prod["id"])] = prod
    to_json(temp, db_name)
    return {}

def add_order(order, db_name = "database.json"):
    """
        Add order to db
    """
    temp = load_json(db_name)
    # add to order db
    temp["ORDER_DB"][str(order["id"])] = order
    to_json(temp, db_name)
    return {}

def clear_db(db_name = "database.json"):
    to_json(init_db(), db_name)
    return {}

def id_generator(option, db_name = "database.json"):
    temp = load_json(db_name)
    if option == "user" or option == "users":
        temp["USER_ID"] += 1
        to_json(temp, db_name)
        return temp["USER_ID"]
    elif option == "product" or option == "products":
        temp["PRODUCT_ID"] += 1
        to_json(temp, db_name)
        return temp["PRODUCT_ID"]
    elif option == "admin" or option == "admins":
        temp["ADMIN_ID"] += 1
        to_json(temp, db_name)
        return temp["ADMIN_ID"]
    elif option == "order" or option == "orders":
        temp["ORDER_ID"] += 1
        to_json(temp, db_name)
        return temp["ORDER_ID"]
    else:
        # Temporary
        raise KeyError()

def check_interest_dim(category, db_name = "database.json"):
    temp = load_json(db_name)
    if len(category) == temp["TYPE_OF_PRODUCTS"]:
        return True
    else:
        return False

def add_product_type(db_name = "database.json"):
    temp = load_json(db_name)
    temp["TYPE_OF_PRODUCTS"] += 1
    for key in temp["PRODUCT_DB"]:
        temp["PRODUCT_DB"][key]["category"].append(0)
    for key in temp["USER_DB"]:
        temp["USER_DB"][key]["interest"].append(0)
    to_json(temp, db_name)
    return temp["TYPE_OF_PRODUCTS"]

def prod_rating_calculator(prod_id, db_name = "database.json"):
    """
        This function is used to obtain total 
        rating for a product from individual 
        user ratings
    """
    valid_id("product", prod_id)
    temp = load_json(db_name)
    rating_lst = temp["PRODUCT_DB"][str(prod_id)]["rating"]
    if len(rating_lst) == 0:
        return 0
    summ = 0
    for rating in rating_lst:
        summ += rating[1]
    return summ / len(rating_lst)

def edit_user_interest(u_id, interest_lst, db_name = 'database.json'):
    """
        This function is used to directly edit 
        user"s interest vecetor
    """
    valid_id("user", u_id, db_name)
    temp = load_json(db_name)
    # 11 product types
    interest_vector = [0] * 11
    for ctgry in interest_lst:
        interest_vector[TEST_KEYWORDS[ctgry]] += 1
    temp["USER_DB"][str(u_id)]["interest"] = interest_vector
    to_json(temp, db_name)
    return {}

def get_interest_lst():
    '''
        This functions returns all keywords as options to user
        to set up user's interest
    '''
    return list(TEST_KEYWORDS.keys())

# USER_DB = {
#     """
#     format:
#         "<id>":                 # type: string
#                 <User class object>
#             contains:
#             {                
#             "id": 1             # type: int, serial
#             "name": "Zard"      # type: string
#             "fund": 10          # type: int; unit: $
#             "address": "Pacific Ocean"
#                                 # type: string
#             "cart": [list of product ID]
#                                 # type: list of int
#             "orders": [list of order ID]
#                                 # type: list of int
#             "interests": [("cheap", 1.0), ...]
#                                 # type: list of tuple, tuple of (category, weight)
#                                 #                                string,  float
#         }
#     """
# }

# ADMIN_DB = {
#     """
#     format:
#         "<id>":{                 # type: string
#                 <Admin class object>
#             contains:
#             {     
#             "id": 2             # type: int, serial
#             "name": "YYF"       # type: string
#             "admin_token": "198ANFu72oDJ0827"
#                                 # type: string
#         }
#     """
# }

# PRODUCT_DB = {
#     """
#     format:
#         "<id>":{                 # type: string
#                 <Product class object>
#             contains:
#             {     
#             "id": 3             # type: int, serial
#             "name": "gift_1"    # type: string
#             "pic": ??????
#                                 # type: string, website or file name
#             "description": "good"
#                                 # type: string
#             "category": ["cheap", "durable"]
#                                 # type: list of string, adjective words
#             "delivery": datetime_object
#                                 # type: leng of time (mm/dd)
#         }
#     """
# }

# ORDER_DB = {
#     """
#     format:
#         "<id>":{                 # type: string
#                 <Order class object>
#             contains:
#             {      
#                                         e.g. "<id>" means: "3" for item with "id": 3
#             "id": 4             # type: int, serial
#             "product_id": 3     # type: int
#             "user_id": 2        # type: int
#             "order_date": datetime_object
#                                 # type: datetime_object
#             "delivery_date": datetime_object
#                                 # type: datetime_object
#             "delivery_state": 0
#                                 # type: int, [0: not delivered,
#                                 #             1: on the way,
#                                 #             2: delivered,
#                                 #             3: cancelled]
#         }
#     """
# }