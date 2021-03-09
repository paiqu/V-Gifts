import json
from user import User

class Database:
    def __init__(self):
        self.users = {}
        self.admins = {}
        self.products = {}
        self.orders = {}

    def to_json(self):
        """
        a function to transfer the User object to JSON format

        return: 
        """
        output = {
            "users": self.users,
            "admins": self.admins,
            "products": self.products,
            "orders": self.orders
        }

        return json.dumps(output)

    def load_json(self):
        '''
            This function loads database from json
            into Database class object
        '''
        return {}

    def add_user(self, user_object):
        """
        a function to add a user to the database

        @param user - type: User
        """
        self.users[str(user_object.get_id)] = user_object
        self.save_to_database()
        
    def get_user_by_id(self, user_id):
        """
        a function to locate a users in the database by its id

        @param: user_id  - type: int
        output: the User object or None (If not found) 
        """
        if str(user_id) not in self.user:
            raise KeyError("User id not exist")
        return self.user[str(user_id)]

    def add_fund_to_user(self, user_id, num):
        user = self.get_user_by_id(user_id)
        user.add_fund(num)

        # update the database
        save_to_database()


    def save_to_database(self):
        with open("data.txt", 'w') as f:
            f.write(self.to_json())
    
    def add_admin(self, admin_object):
        return {}

    def add_product(self, admin_object):
        return {}

    def add_order(self, admin_object):
        return {}
