'''
    This file contains user side functions
'''
import database as db
import datetime as dt

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
                # [(product_id, amount), ...]
        "order": [],
                # [order_id, ...]
        "interest": [0] * temp['TYPE_OF_PRODUCTS']
    }

def new_order(user_id, product_id, datee, amount):
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
                                # in format of timestamp:
                                # e.g. datee = 1545730073  ->  2018-12-25 09:27:53
        "amount": amount,
        "state": 0,             # 0: just purchase
                                # 1: delivering
                                # 2: done
                                # 3: cancelled
        "rating": 0
    }

####################################################################
########### Corrections for function below are required ############
####################################################################


def add_fund(u_id, num):
    '''
    This function adds fund to a user
    '''
    temp = db.load_json()
    db.valid_id('user',u_id)
    print(temp['USER_DB'][str(u_id)])
    temp['USER_DB'][str(u_id)]['fund'] += num
    db.to_json(temp)
    return {}

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


def add_product_to_cart(user_id, product_id, amount):
    '''
        This function adds a product into user's 
        shopping cart
    '''
    db.valid_id('user',user_id)
    db.valid_id('product',product_id)
    temp = db.load_json()
    item = [product_id, amount]
    # (product_id, amount)
    temp['USER_DB'][str(user_id)]['shopping_cart'].append(item)
    print(temp['USER_DB'][str(user_id)]['shopping_cart'])
    db.to_json(temp)
    return {}

def remove_prod_from_cart(user_id, cart_item_pair):
    '''
        cart_item_pair -> (product_id, amount)
        This function remvoes prod from cart
    '''
    product_id, amount = cart_item_pair
    db.valid_id('user',user_id)
    db.valid_id('product',product_id)
    temp = db.load_json()
    temp['USER_DB'][str(user_id)]['shopping_cart'].remove(cart_item_pair)
    db.to_json(temp)
    return {}

def individual_price(product_id, amount):
    temp = db.load_json()
    price = amount * temp['PRODUCT_DB'][str(product_id)]['price']
    return price

def total_price(lst):
    '''
        This function calculates the total price of item to purchase
    '''
    price = 0
    for cart_item_pair in lst:
        product_id, amount = cart_item_pair
        price += individual_price(product_id, amount)
    return price

def purchase(u_id, lst):
    '''
        This function makes payment
        lst -> [(product_id, amount), ...]
        1. check fund
        2. make payments
    '''
    # 1
    db.valid_id('user', u_id)
    total_cost = total_price(lst)
    temp = db.load_json()
    user_fund = temp['USER_DB'][str(u_id)]['fund']
    if user_fund < total_cost:
        # not enough fund
        print('Not enough fund')
        return {}
    else:
        # 2
        # enough fund
        temp['USER_DB'][str(u_id)]['fund'] -= total_cost
        db.to_json(temp)
        for cart_item_pair in lst:
            product_id, amount = cart_item_pair
            create_order(u_id, product_id, amount)
    return {}

def create_order(user_id, product_id, amount):
    '''
        This function creates an order
        and generate an order id and store it in user
        3. create order
        4. remove product from cart
        5. add order to user & order_db
        6. save to db

        This function adds order to ORDER_DB
    '''
    db.valid_id('user',user_id)
    db.valid_id('product',product_id)
    # 3
    datee = int(dt.datetime.timestamp(dt.datetime.now()))
    order = new_order(user_id, product_id, datee, amount)
    db.add_order(order)
    # 4 
    temp = db.load_json()
    cart_item_pair = [product_id, amount]
    temp['USER_DB'][str(user_id)]['shopping_cart'].remove(cart_item_pair)
    # 5 add order id to user
    temp['USER_DB'][str(user_id)]['order'].append(order['id'])
    # 6
    db.to_json(temp)
    return {
        'order_id': 1               # order_id
    }

def rate_order(u_id, order_id, rating):
    '''
        This function allows user to rate an order if order is completed
    '''
    db.valid_id('user', u_id)
    db.valid_id('order', order_id)
    if rating <= 0:
        rating = 0
    elif rating >= 5:
        rating = 5
    temp = db.load_json()
    if u_id != temp['ORDER_DB'][str(order_id)]['u_id']:
        raise KeyError()
        return {}
    prod_id = temp['ORDER_DB'][str(order_id)]['product_id']
    temp['ORDER_DB'][str(order_id)]['rating'] = rating
    temp['PRODUCT_DB'][str(prod_id)]['rating'].append([u_id, rating])
    return {}
