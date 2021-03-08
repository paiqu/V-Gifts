import json

class Database:
    def __init__(self):
        self.users = []
        self.admins = []
        self.products = []
        self.orders = []

    def to_json(self):
        output = {
            "users": self.users,
            "admins": self.admins,
            "products": self.products,
            "orders": self.orders
        }

        return json.dumps(output)

    def add_user(self, user):
        """
        a function to add a user to the database

        @param user - type: User
        """
        self.users.append(user)
        self.save_to_database()
        
    def get_user_by_id(self, user_id):
        """
        a function to locate a users in the database by its id

        @param: user_id  - type: int
        output: the User object or None (If not found) 
        """
        for user in self.users:
            if user.id == user_id:
                return user
        
        return None

    def save_to_database(self)
        with open("data.txt", 'w') as f:
            f.write(self.to_json())