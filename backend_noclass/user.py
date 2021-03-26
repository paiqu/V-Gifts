'''
    This file contains user side functions
'''
import database as db
import datetime as dt
import admin as ad
import login as lo

def new_user(aname, fname, lname, password, email, address, city, country):
    new_id = db.id_generator('user')
    temp = db.load_json()
    return {
        "id": new_id,
        "name": aname,
                # account name
        "fname": fname,
        "lname": lname,
        "password": password,
        "email": email,
        "address": address,
        "city": city,
        "country": country,
        "fund": 0,
        "shopping_cart": [],
                # [[product_id, amount], ...]
        "order": [],
                # [order_id, ...]
        "interest": [0] * temp['TYPE_OF_PRODUCTS']
    }

def new_order(user_id, product_id, datee, amount):
    '''
        create a new product,
        category should be a lst of int with length of
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
                                # 3: cancelled / refunded
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
    temp['USER_DB'][str(u_id)]['fund'] += num
    new_fund = temp['USER_DB'][str(u_id)]['fund']
    db.to_json(temp)
    return {
        'fund': new_fund
    }

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



# User forget password and reset
def forget_password(name, email):
    '''
    Check the email exist
    Send reset url to the email
    return new password
    '''
    return new_password

# Users change password
def change_password(token, old_password, new_password):
    '''
    Check the name and password match
    Reset the password
    '''
    
    if check_token_token(token) is not True:
        print('Invalid Token!')
        return False
    temp = db.load_json()
    for user_id, user_info in temp['USER_DB'].items():
        if user_info["password"] == lo.encrypt_password(old_password):
            user_info["password"] = lo.encrypt_password(new_password)
            db.to_json(temp)
            lo.logout_user(user_id)
            return True
    return False


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
    db.to_json(temp)
    return {
        'pid': product_id,
        'amount': amount
    }

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
    return {
        'pid': product_id
    }

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
        lst -> [[product_id, amount], ...]
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
            order_id = create_order(u_id, product_id, amount)
    return {
        'id': order_id
    }

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
    order_id = order['id']
    # 4 
    temp = db.load_json()
    cart_item_pair = [product_id, amount]
    temp['USER_DB'][str(user_id)]['shopping_cart'].remove(cart_item_pair)
    # 5 add order id to user
    temp['USER_DB'][str(user_id)]['order'].append(order['id'])
    # 6
    db.to_json(temp)
    return {
        'id': order_id
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
    if u_id != temp['ORDER_DB'][str(order_id)]['user_id']:
        raise KeyError()
    prod_id = temp['ORDER_DB'][str(order_id)]['product_id']
    temp['ORDER_DB'][str(order_id)]['rating'] = rating
    temp['PRODUCT_DB'][str(prod_id)]['ratings'].append([u_id, rating])
    db.to_json(temp)
    return {}

def edit_user_interest(u_id, interest_lst):
    '''
        This function is used to directly edit 
        user's interest vecetor
    '''
    db.valid_id('user', u_id)
    temp = db.load_json()
    if len(interest_lst) != temp['TYPE_OF_PRODUCTS']:
        raise ValueError()
        return {}
    else:
        temp['USER_DB'][str(u_id)]['interest'] = interest_lst
        db.to_json(temp)
    return {}

def show_user_cart(u_id):
    '''
        This function shows the shopping cart of a user
    '''
    db.valid_id('user', u_id)
    temp = db.load_json()
    return temp['USER_DB'][str(u_id)]['shopping_cart']

def show_product_detail(prod_id):
    '''
        This function shows the details of a product
    '''
    db.valid_id('product', prod_id)
    temp = db.load_json()
    return temp['PRODUCT_DB'][str(prod_id)]

def refund_helper(db, u_id, amount):
    '''
        This function adds amount to a user
        WITHOUT loading/saving from/to Database
    '''
    db['USER_DB'][str(u_id)]['fund'] += amount
    return db

def order_refund(u_id, order_id):
    '''
        This function refunds an order if 
        the order is not delivered yet (state = 0)
    '''
    db.valid_id('user', u_id)
    db.valid_id('order', order_id)
    temp = db.load_json()
    # if refund is applicable
    if temp['ORDER_DB'][str(order_id)]['state'] == 3:
        # print('Order already refunded')
        status = "Order already refunded"
    elif temp['ORDER_DB'][str(order_id)]['state'] == 0:
        if int(u_id) != temp['ORDER_DB'][str(order_id)]['user_id']:
            # print('Only user paid for this order can refund')
            status = "Only user paid for this order can refund"
        ad.change_order_state(order_id, 3)
        prod_id = temp['ORDER_DB'][str(order_id)]['product_id']
        price = temp['PRODUCT_DB'][str(prod_id)]['price']
        amount = temp['ORDER_DB'][str(order_id)]['amount']
        temp = refund_helper(temp, u_id, amount * price)
        db.to_json(temp)
        # print('Refund success')
        status = "Refund success"
    else:
        # print('Already on delivery, refund not applicable')
        status = "Already on delivery, refund not applicable"
    return status

def show_order_user(u_id):
    '''
        This functions shows order ids done by selected user
    '''
    db.valid_id('user', u_id)
    temp = db.load_json()
    return temp['USER_DB'][str(u_id)]['order']



# Check token is available
def check_token(iid):
    temp = db.load_json()
    for token_id, user_token in temp['TOKEN_DB'].items():
        if iid == token_id:
            return True
    return False

def check_token_token(token):
    temp = db.load_json()
    for token_id, user_token in temp['TOKEN_DB'].items():
        if token == user_token:
            return True
    return False
