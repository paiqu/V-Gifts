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
import csv
import database as db
import datetime as dt
import user as usr
import chatbot as ct
import webpage as wbp
from numpy import ceil
import login

# class Admin:
#     def __init__(name, password, email):
#         self.id = None
#         self.name = name
#         self.password = password
#         self.email = email

# init

def new_preset_admin(name, password, email):
    return {
        "id": 1,
        "name": name,
        "password": password,
        "email": email
    }

def new_admin(name, password, email, db_name = 'database.json'):
    new_id = db.id_generator('admin', db_name)
    return {
        "id": new_id,
        "name": name,
        "password": password,
        "email": email
    }

def new_product(name, price, description, category, deli_days, pic_link, db_name = 'database.json'):
    '''
        create a new product,
        category should be a lst of int with length of
        TYPE_OF_PRODUCTS
    '''
    new_id = db.id_generator('product', db_name)
    # assert db.check_interest_dim(category)
    # catagory is now calculated by query_analysis
    category = None
    if description == "" or description is None:
        description = name
        category = ct.query_analysis_test3(name)
    else:
        category = ct.query_analysis_test3(name + '. ' + description)
    return {
        "id": new_id,
        "name": name,
        "price": price,
        "description": description,
        "category": category, # [0] * temp['TYPE_OF_PRODUCTS']
        "delivery": deli_days,
        "ratings": [],
                    # [(u_id, rating), ...]
        "pic": pic_link
    }


# editors

def edit_admin(admin_id, name, password, email, db_name = 'database.json'):
    '''
        This function edits admin info with inputs above
        and returns the id of this admin
    '''
    temp = db.load_json(db_name)
    if str(admin_id) not in temp['ADMIN_DB']:
        raise KeyError()
    temp['ADMIN_DB'][str(admin_id)]["name"] = name
    temp['ADMIN_DB'][str(admin_id)]["password"] = password
    temp['ADMIN_DB'][str(admin_id)]["email"] = email
    db.to_json(temp, db_name)
    return {
        'id': admin_id
    }

def temp_use():
    temp = db.load_json()
    passw = login.encrypt_password("admin")
    print(passw)
    temp['ADMIN_DB']["1"]["password"] = passw
    db.to_json(temp)

def edit_product(prod_id, prod_name, prod_descrip, prod_price, \
                prod_delivery, prod_pic, db_name = 'database.json'):
    '''
        This function edits product info with inputs above
        and returns the id of this product
    '''
    temp = db.load_json(db_name)
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    temp['PRODUCT_DB'][str(prod_id)]["name"] = prod_name
    # assert db.check_interest_dim(prod_category)
    prod_category = None
    if prod_descrip == "" or prod_descrip is None:
        prod_descrip = prod_name
        prod_category = ct.query_analysis_test3(prod_name)
    else:
        prod_category = ct.query_analysis_test3(prod_name + '. ' + prod_descrip)
    temp['PRODUCT_DB'][str(prod_id)]["category"] = prod_category
    temp['PRODUCT_DB'][str(prod_id)]["description"] = prod_descrip
    temp['PRODUCT_DB'][str(prod_id)]["price"] = prod_price
    temp['PRODUCT_DB'][str(prod_id)]["delivery"] = prod_delivery
    temp['PRODUCT_DB'][str(prod_id)]["pic"] = prod_pic
    db.to_json(temp, db_name)
    return {
        'id': prod_id
    }

def product_id_to_name(prod_id, db_name = 'database.json'):
    temp = db.load_json(db_name)
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    return temp['PRODUCT_DB'][str(prod_id)]["name"]

def delete_product(prod_id, db_name = 'database.json'):
    '''
        This function deletes a product by id
        and returns the id of this product
    '''
    temp = db.load_json(db_name)
    if str(prod_id) not in temp['PRODUCT_DB']:
        raise KeyError()
    else:
        rt = temp['PRODUCT_DB'].pop(str(prod_id))
        db.to_json(temp, db_name)
        return {
            'prod_info': rt
        }

def edit_prod_category(prod_id, category_lst):
    '''
        *** NO LONGER USED ***
        This function can update the category vector of a product
    '''
    db.valid_id('product', prod_id)
    temp = db.load_json()
    if len(category_lst) != temp['TYPE_OF_PRODUCTS']:
        raise ValueError()
        return {}
    else:
        temp['PRODUCT_DB'][str(prod_id)]['category'] = category_lst
        db.to_json(temp)
    return {}

def change_order_state(order_id, new_state):
    '''
        Thi function changes the delivery state of an order
        # 0: just purchase
        # 1: delivering
        # 2: done
        # 3: cancelled
    '''
    assert new_state in [0,1,2,3]
    db.valid_id('order', order_id)
    temp = db.load_json()
    temp['ORDER_DB'][str(order_id)]['state'] = new_state
    db.to_json(temp)
    return {
        'id': order_id,
        'state': new_state
    }

def get_user_list():
    '''
        This functions returns all user's basic info for admin
    '''
    temp = db.load_json()
    rt = []
    for key in temp['USER_DB'].keys():
        rt.append({
            'user_id': temp['USER_DB'][key]['id'],
            'account_name': temp['USER_DB'][key]['name'],
            'first_name': temp['USER_DB'][key]['fname'],
            'last_name': temp['USER_DB'][key]['lname'],
            'email': temp['USER_DB'][key]['email'],
            'address': temp['USER_DB'][key]['address'],
            'city': temp['USER_DB'][key]['city'],
            'country': temp['USER_DB'][key]['country']
        })
    return rt

def show_profile(aid):
    db.valid_id("admin", aid)
    temp = db.load_json()
    return {
        "username": temp["ADMIN_DB"][str(aid)]["name"],
        "email": temp["ADMIN_DB"][str(aid)]["email"]
    }

def get_all_order():
    temp = db.load_json()
    lst = []
    for key in temp["ORDER_DB"].keys():
        uid = temp["ORDER_DB"][key]["user_id"]
        pid = temp["ORDER_DB"][key]["product_id"]
        amount = temp["ORDER_DB"][key]["amount"]
        datte = temp["ORDER_DB"][key]["purchase_date"]
        state_in_code = temp["ORDER_DB"][key]["state"]
        if state_in_code == 0:
            state_in_text = "Just purchase"
        elif state_in_code == 1:
            state_in_text = "Delivering"
        elif state_in_code == 2:
            state_in_text = "Done"
        elif state_in_code == 3:
            state_in_text = "Cancelled / Refunded"
        else:
            state_in_text = "Invalid state"
        lst.append({
            "order_id": key,
            "user_id": uid,
            "product_id": pid,
            "product_name": product_id_to_name(pid),
            "amount": amount,
            "pic_link": temp["PRODUCT_DB"][str(pid)]["pic"],
            "cost": usr.individual_price(pid, amount),
            "purchase_date": int(datte),
            "state_in_code": state_in_code,
            "state_in_text": state_in_text,
            "rating": temp["ORDER_DB"][key]["rating"]
        })
    return lst

def get_all_admin():
    temp = db.load_json()
    lst = []
    for key in temp["ADMIN_DB"].keys():
        lst.append({
            "admin_id": key,
            "username": temp["ADMIN_DB"][key]["name"],
            "email": temp["ADMIN_DB"][key]["email"]
        })
    return lst

def add_prod_from_csv(filename, db_name = 'database.json'):
    '''
        This function allows admin to import prod data from
        csv file
    '''
    if filename[-4:] != '.csv':
        # print(filename[-4:-1])
        return 'File format is not accepted'
    else:
        csvf = open(filename, 'r')
        csvfr = csv.reader(csvf)
        n_prod = []
        row_n = 0
        for rows in csvfr:
            row_n += 1
            print(rows)
            # 6 inputs for new_product()
            if len(rows) == 6:
                name, price, description, category, \
                        deli_days, pic_link = rows
                n_prod.append(new_product(name, int(price), description, category, \
                        int(deli_days), pic_link, db_name))
            elif len(rows) == 0:
                continue
            else:
                csvf.close()
                return 'Error information in provided csv file, row {}, \
                            roll back database'.format(row_n)
        # if all fows are good
        for prod in n_prod:
            db.add_prod(prod, db_name)
        csvf.close()
        return 'Success, {} products imported'.format(row_n)

def show_product_lst(page = -1, user_id = -1, num_each_page = 9, rec_num = 6, db_name = "database.json"):
    """
        This function shows a lst of product
    """
    dbs = db.load_json(db_name)
    proc_lst = []
    for key in dbs["PRODUCT_DB"].keys():
        rtt = round(wbp.rating_calc(dbs["PRODUCT_DB"][key]["id"]),2)
        proc_lst.append({
            "product_id": dbs["PRODUCT_DB"][key]["id"],
            "name": dbs["PRODUCT_DB"][key]["name"],
            "price": dbs["PRODUCT_DB"][key]["price"],
            "rating": rtt,
            "pic_link": dbs["PRODUCT_DB"][key]["pic"]
        })
    proc_rt = []
    if page != -1:
        for i in range(len(proc_lst)):
            if i >= (page-1)*num_each_page and i < page*num_each_page:
                # e.g. page 1 => item 0~8
                proc_rt.append(proc_lst[i])
    else: # return all prods
        proc_rt = proc_lst
    if user_id == -1:
        rec_rt = []
    else:
        # if a user presist, execute recommendation algo
        # technically fetchs all product
        rec_lst = wbp.search_filter_recommendation(user_id = user_id)["product_lst"]
        rec_pid = []
        for item in rec_lst:
            rec_pid.append(item["product_id"])
        rec_rt = []
        if rec_num >= len(rec_lst):
            rec_num = len(rec_lst)
        for i in range(rec_num):
            prod_id = rec_pid[i]
            rtt = round(wbp.rating_calc(prod_id),2)
            rec_rt.append({
                "product_id": prod_id,
                "name": dbs["PRODUCT_DB"][str(prod_id)]["name"],
                "price": dbs["PRODUCT_DB"][str(prod_id)]["price"],
                "rating": rtt,
                "pic_link": dbs["PRODUCT_DB"][str(prod_id)]["pic"]
            })
    return {
        "recommendation_list": rec_rt,
        "product_lst": proc_rt,
        "total_pages": ceil((len(proc_lst)/num_each_page))
    }

def show_product_detail(prod_id, db_name = "database.json"):
    """
        This function shows the details of a product
    """
    db.valid_id("product", prod_id)
    dbs = db.load_json()
    rt = round(wbp.rating_calc(prod_id), 2)
    return {
        "id": dbs["PRODUCT_DB"][str(prod_id)]["id"],
        "name": dbs["PRODUCT_DB"][str(prod_id)]["name"],
        "price": dbs["PRODUCT_DB"][str(prod_id)]["price"],
        "description": dbs["PRODUCT_DB"][str(prod_id)]["description"],
        "delivery": dbs["PRODUCT_DB"][str(prod_id)]["delivery"],
        "rating": rt,
        "pic_link": dbs["PRODUCT_DB"][str(prod_id)]["pic"],
    }

def add_prod_to_csv(filename, db_name = 'database.json'):
    '''
        This function allows admin to import prod data from
        csv file
    '''
    if filename[-4:] != '.csv':
        # print(filename[-4:-1])
        return 'File format is not accepted (not *.csv)'
    else:
        temp = db.load_json(db_name)
        csvf = open(filename, 'w', newline='')
        csvfw = csv.writer(csvf)
        row_n = 0
        for prod_key in temp['PRODUCT_DB'].keys():
            row_n += 1
            csvfw.writerow([
                temp['PRODUCT_DB'][prod_key]['name'],
                temp['PRODUCT_DB'][prod_key]['price'],
                temp['PRODUCT_DB'][prod_key]['description'],
                temp['PRODUCT_DB'][prod_key]['category'],
                temp['PRODUCT_DB'][prod_key]['delivery'],
                temp['PRODUCT_DB'][prod_key]['pic']
            ])
        csvf.close()
        return "{} rows of products saved into {}".format(row_n, filename)


# def order_history():
#     '''
#         This function doen't have a purpose yet.
#     '''
#     return {}

if __name__ == "__main__":
    # temp_use()
    # print(add_prod_from_csv("prod.csv", db_name = 'database.json'))
    print(add_prod_to_csv('prod.csv', db_name = 'database.json'))
    pass