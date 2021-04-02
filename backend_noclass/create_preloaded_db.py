'''

'''

import json
import database as db
import admin as ad

def add_product_to_db_special(file_name = 'database_manual.json'):
    temp = db.init_db()
    # file_name = 'database_manual.json'
    db.to_json(temp, file_name)
    lst = [
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            # more to add
        }
    ]
    # load products into db
    for prod in lst:
        db.add_prod(ad.new_product(prod['name'], prod['price'], prod['description'],\
                            None, prod['delivery_days'], prod['pic_link']), file_name)
    # show db
    db.pretty_print(db.load_json(file_name))

if __name__ == "__main__":
    add_product_to_db_special()