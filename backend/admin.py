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

from user import TYPE_OF_PRODUCTS
from database_pai import Database

class Admin:
    def __init__(name, password, email):
        self.id = None
        self.name = name
        self.password = password
        self.email = email

    # getters and setters
    def get_id(self):
        return self.id 
    
    def set_password(self, password):
        self.password = password

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name 

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email 

class product:
    def __init__(self, names, descriptions):
        temp = Database()
        temp = temp.load_json()
        self.id = temp.id_generator('product')
        self.name = names
        self.description = descriptions
        self.features = [0] * TYPE_OF_PRODUCTS
        self.pic = None


def add_product(prod_name, prod_feature, prod_descrip, prod_pic):
    '''
        This function creates a product with inputs above
        and returns the id generated for this product
    '''
    return {
        'id': 123
    }

def edit_product(prod_id, prod_name, prod_feature, prod_descrip, prod_pic):
    '''
        This function edits product info with inputs above
        and returns the id of this product
    '''
    return {
        'id': prod_id
    }

def delete_product(prod_id):
    '''
        This function deletes a product by id
        and returns the id of this product
    '''
    return {
        'id': prod_id
    }

def order_history():
    '''
        This function doen't have a purpose yet.
    '''
    return {}