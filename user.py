'''
    This file contains user side functions
'''

def edit_info_user(id):
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

def create_order(user_id, product_id):
    '''
        This function creates an order
        and generate an order id and store it in user

        This function adds order to ORDER_DB
    '''
    return {
        'order_id': 1               # order_id
    }

def buy_product_from_cart(user_id, product_id):
    '''
        This function buys a product if user has 
        enough fund, and create a corresponding
        order.
    '''
    # order_id = create_order(user_id, product_id)
    return {
        'user_id': user_id, 
        'product_id': product_id,
        'order_id': 1               # order_id
    }