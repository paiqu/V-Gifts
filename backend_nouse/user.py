'''
    This file contains user side functions
'''
from database_pai import Database

# global variable
TYPE_OF_PRODUCTS = 10   # dimension of interests
class User:
    def __init__(self, name, password, email):
        # used to generate id from database
        temp = Database()
        temp = temp.load_json()
        self.id = temp.id_generator('user')
        self.name = name
        self.password = password
        self.email = email
        self.address = ""
        self.fund = 0
        self.cart = []
        self.orders = []
        self.interests = [0] * TYPE_OF_PRODUCTS

    # Implement getters and setters later
    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email 

    def set_address(self, address):
        self.address = address

    def get_adress(self):
        return self.address
    

    def get_id(self):
        return self.id

    def add_fund(self, num):
        '''
        This function adds fund to a user
        '''
        self.fund += num
    
    def buy_product_from_cart(self, product):
        '''
        This function buys a product if user has 
        enough fund, and create a corresponding
        ordr

        :param product: the product to be purchased
        '''
    
    def to_dict(self):
        '''
        This function will transfer the User object to a dict
        Will be used in JSON later
        '''
        return self.__dict__

    def e_interest(self):
        return self.interests

    def add_interest(self, num):
        '''
            Prevent overflow
        '''
        self.interests[num % TYPE_OF_PRODUCTS] += 1

####################################################################
########### Corrections for function below are required ############
####################################################################

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


# # Users manage profile
# def manage_profile(name, cart, address, ):
#     '''
#     Users could manage their name, cart, address at their will
#     This function change users' information
#     '''
#     return {
#         ...
#     }
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

