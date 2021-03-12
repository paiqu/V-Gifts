'''
    This file contains user side functions
'''
import database as db

def new_user(name, password, email, address):
    new_id = db.id_generator('user')
    temp = db.load_json()
    return {
        "id": new_id,
        "name": name,
        "password": password,
        "email": email,
        "address": address,
        "fund": 0,
        "shopping_cart": [],
        "orders": [],
        "interest": [0] * temp['TYPE_OF_PRODUCTS']
    }

def new_order(user_id, product_id, datee):
    '''
        create a new product,
        feature should be a lst of int with length of
        TYPE_OF_PRODUCTS
    '''
    new_id = db.id_generator('order')
    return {
        "id": new_id,
        "user_id": user_id,
        "product_id": product_id,
        "purchase_date": datee,
        "state": 0,             # 0: just purchase
                                # 1: delivering
                                # 2: done
                                # 3: cancelled
    }

####################################################################
########### Corrections for function below are required ############
####################################################################


def add_fund(u_id, num):
    '''
    This function adds fund to a user
    '''
    temp = db.load_json
    db.valid_id('user',u_id)
    temp['USER_DB'][str(u_id)]['fund'] += num
    db.to_json(temp)
    return temp['USER_DB'][str(u_id)]['fund']

def buy_product_from_cart(self, product):
    '''
    This function buys a product if user has 
    enough fund, and create a corresponding
    ordr

    :param product: the product to be purchased
    '''


def add_interest(u_id, posi, num):
    '''
        This function updates user's interest
        Prevent overflow
    '''
    temp = db.load_json
    db.valid_id('user',u_id)
    temp['USER_DB'][str(u_id)]['interest'][posi % temp['TYPE_OF_PRODUCTS']] \
             += num
    return temp['USER_DB'][str(u_id)]['interest']


def encrypt_password(password):
    '''
    Encrypt the password with sha256 and store in database
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    '''
    return sha_signature

# User forget password and reset
def forget_password(name, email):
    '''
    Check the email exist
    Send reset url to the email
    return new password
    '''
    return new_password

# Users change password
def change_password(name,old_password):
    '''
    Check the name and password match
    Reset the password
    '''
    return new_password


def edit_info_user(u_id):
    '''
        This function edits user info
    '''
    return {
    }

def add_fund_user(id, fund):
    '''
        This function adds fund to a user
    '''
    return {
        "current_fund": fund
    }

def add_product_to_cart(user_id, product_id):
    '''
        This function adds a product into user's 
        shopping cart
    '''
    return {
        'user_id': user_id, 
        'product_id': product_id
    }

def create_order(user_id, product_id, datee):
    '''
        This function creates an order
        and generate an order id and store it in user
        1. check fund
        2. make payments
        3. create order
        4. remove product from cart
        5. add order to user & order_db
        6. save to db

        This function adds order to ORDER_DB
    '''
    order = new_order(user_id, product_id, datee)
    db.valid_id('user', user_id)
    temp = db.load_json()

    db.to_json(temp)
    return {
        'order_id': 1               # order_id
    }

def remove_prod_from_cart(user_id, product_id):
    '''
        This function remvoes prod from cart
    '''
    # order_id = create_order(user_id, product_id)
    return {}

