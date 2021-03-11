import json
from user import User

class Database:
    def __init__(self):
        self.users = {}
        self.admins = {}
        self.products = {}
        self.orders = {}
        self.u_id = 0
        self.p_id = 0
        self.a_id = 0
        self.o_id = 0

    def to_json(self):
        """
        a function to transfer the User object to JSON format
        remember to save ids (see __init__)
        return: 
        """

        # users - type: dict of {'id': User}
        output = {
            "users": {key: value.to_dict() for (key, value) in self.users.items()},
            "admins": {key: value.to_dict() for (key, value) in self.admins.items()},
            "products": {key: value.to_dict() for (key, value) in self.products.items()},
            "orders": {key: value.to_dict() for (key, value) in self.orders.items()}
        }

        return json.dumps(output)

    def load_json(self):
        '''
            This function loads database from json
            into Database class object

            remember to load ids (see __init__)
        '''
        return self # {}

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

    def export_product(self):
        '''
            extract product dict
        '''
        return self.products

    def export_user(self):
        '''
            extract user dict
        '''
        return self.user

    def id_generator(self, option):
        if option == 'user' or option == 'users':
            self.u_id += 1
            return self.u_id
        elif option == 'product' or option == 'products':
            self.p_id += 1
            return self.u_id
        elif option == 'admin' or option == 'admins':
            self.a_id += 1
            return self.u_id
        elif option == 'order' or option == 'orders':
            self.o_id += 1
            return self.u_id
        else:
            # Temporary
            raise KeyError()

# place holder for Database

DB_ALL = Database()