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
from login import encrypt_password

# Global values

TYPE_OF_PRODUCTS_INIT = 11


# Main fuctions

def init_db():
    """
        This fuction initialize the database 
        with no values but a pre-set admin for further use
    """
    db = {
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
    admin = adm.new_preset_admin("admin", encrypt_password("admin"), "VictimsCOMP3900@gmail.com")
    db["ADMIN_DB"][str(admin["id"])] = admin
    return db

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

def valid_id(option, idd, db_name = "database.json"):
    """
        This func checks if an id exist in database
        options in user/product/admin/order
    """
    db = load_json(db_name)
    if option == "user" or option == "users":
        if str(idd) in db["USER_DB"]:
            return True
    elif option == "product" or option == "products":
        if str(idd) in db["PRODUCT_DB"]:
            return True
    elif option == "admin" or option == "admins":
        if str(idd) in db["ADMIN_DB"]:
            return True
    elif option == "order" or option == "orders":
        if str(idd) in db["ORDER_DB"]:
            return True

    # raise key error if id not found
    raise KeyError()

def to_json(db, filename = "database.json"):
    """
        This fuction save database to json file
    """
    with open(filename, "w") as fp:
        json.dump(db, fp)
    return {}

def load_json(filename = "database.json"):
    """
        This function loads database from json file
    """
    with open(filename, "r") as fp:
        db = json.load(fp)
    return db

def add_user(user, db_name = "database.json"):
    """
        This fuction add user to database
    """
    db = load_json(db_name)
    db["USER_DB"][str(user["id"])] = user
    to_json(db, db_name)
    return {}

def add_admin(admin, db_name = "database.json"):
    """
        This fuction add admin to database
    """
    db = load_json(db_name)
    db["ADMIN_DB"][str(admin["id"])] = admin
    to_json(db, db_name)
    return {}

def add_prod(prod, db_name = "database.json"):
    """
        This fuction add product to db
    """
    db = load_json(db_name)
    db["PRODUCT_DB"][str(prod["id"])] = prod
    to_json(db, db_name)
    return {}

def add_order(order, db_name = "database.json"):
    """
        This fuction add order to db
    """
    db = load_json(db_name)
    db["ORDER_DB"][str(order["id"])] = order
    to_json(db, db_name)
    return {}

def clear_db(db_name = "database.json"):
    """
        This fuction reset all value in database to its initial value
    """
    to_json(init_db(), db_name)
    return {}

def id_generator(option, db_name = "database.json"):
    """
        This fuction generate id of objects
        options in user/product/admin/order
    """
    db = load_json(db_name)
    if option == "user" or option == "users":
        db["USER_ID"] += 1
        to_json(db, db_name)
        return db["USER_ID"]
    elif option == "product" or option == "products":
        db["PRODUCT_ID"] += 1
        to_json(db, db_name)
        return db["PRODUCT_ID"]
    elif option == "admin" or option == "admins":
        db["ADMIN_ID"] += 1
        to_json(db, db_name)
        return db["ADMIN_ID"]
    elif option == "order" or option == "orders":
        db["ORDER_ID"] += 1
        to_json(db, db_name)
        return db["ORDER_ID"]
    else:
        # raise key error if option not in range
        raise KeyError()

def check_interest_dim(category, db_name = "database.json"):
    """
        This fuction check user interest dimension
    """
    db = load_json(db_name)
    if len(category) == db["TYPE_OF_PRODUCTS"]:
        return True
    else:
        return False

def add_product_type(db_name = "database.json"):
    """
        This fuction add more product type
    """
    db = load_json(db_name)
    db["TYPE_OF_PRODUCTS"] += 1
    for key in db["PRODUCT_DB"]:
        db["PRODUCT_DB"][key]["category"].append(0)
    for key in db["USER_DB"]:
        db["USER_DB"][key]["interest"].append(0)
    to_json(db, db_name)
    return db["TYPE_OF_PRODUCTS"]

def prod_rating_calculator(prod_id, db_name = "database.json"):
    """
        This function is used to obtain total 
        rating for a product from individual 
        user ratings
    """
    valid_id("product", prod_id)
    db = load_json(db_name)
    rating_lst = db["PRODUCT_DB"][str(prod_id)]["rating"]
    if len(rating_lst) == 0:
        return 0
    summ = 0
    for rating in rating_lst:
        summ += rating[1]
    return summ / len(rating_lst)

def edit_user_interest(u_id, interest_lst, db_name = "database.json"):
    """
        This function is used to directly edit 
        user"s interest vecetor
    """
    valid_id("user", u_id, db_name)
    db = load_json(db_name)
    # 11 product types
    interest_vector = [0] * 11
    for ctgry in interest_lst:
        interest_vector[TEST_KEYWORDS[ctgry]] += 1
    db["USER_DB"][str(u_id)]["interest"] = interest_vector
    to_json(db, db_name)
    return {}

def get_interest_lst():
    """
        This functions returns all keywords as options to user
        to set up user"s interest
    """
    return list(TEST_KEYWORDS.keys())
