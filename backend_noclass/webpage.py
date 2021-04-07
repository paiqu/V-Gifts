'''
    This file contains webpage operations
    including:
        item sorting
        order sorting
        product recommendation
'''
import random as rd
import numpy as np
import database as db
import user as us

def unit_vector(vector):
    '''
        Returns the unit vector of the vector.  
    '''
    # deal with [0, 0, 0, ..., 0]
    if_all_zero = sum(map(abs,vector))
    if if_all_zero == 0:
        return vector
    # regular calculation
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    ''' 
        Returns the angle in radians between vectors 'v1' and 'v2'
    '''
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def prod_recommendation(user_id, prod_lst = [], db_name = 'database.json', num = 100):
    '''
        This function calculates the similarity between
        user_interest vector and
        product category
        to rank products and recommend

        returns a list of product_id, sorted
    '''
    # item & value calculator
    lst = prod_picker(user_id, prod_lst, db_name)
    # return sorted result (descending)
    rt = sorting_merge(lst, 1)
    if len(rt) <= num:
        return rt
    else:
        return rt[:num]


def interest_calculator(v_1, v_2, key):
    '''
        for example
        u_interest = [1, 2, 3, 4, 5]
        it_category = [6, 7, 8, 9, 10]
    '''
    return (key, angle_between(v_1, v_2))
    

def prod_picker(user_id, prod_lst = [], db_name = 'database.json'): # percent -> the chance of product is joining the recommendation
    # prod_lst = DB
    temp = db.load_json(db_name)
    prod_lst = temp['PRODUCT_DB'].keys() if prod_lst == [] else prod_lst
    user_v = temp['USER_DB'][str(int(user_id))]['interest']
    # append to lst
    lst = []
    for item in prod_lst:
        v_1 = temp['PRODUCT_DB'][item]['category']
        lst.append(interest_calculator(v_1, user_v, item))
    return lst

def sorting_helper(lst1, lst2, posi, mode = 0):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    new = []
    while len(lst1) > 0 and len(lst2) > 0:
        l1 = lst1[0]
        l2 = lst2[0]
        if mode == 0: # ascending
            if l1[posi] <= l2[posi]:
                new.append(l1)
                lst1.pop(0)
            else: # l1[1] > l2[1]
                new.append(l2)
                lst2.pop(0)
        else: # mode != 0, descending
            if l1[posi] > l2[posi]:
                new.append(l1)
                l1 = lst1.pop(0)
            else: # l1[1] <= l2[1]
                new.append(l2)
                l2 = lst2.pop(0)

    # merge tails
    if len(lst1) == 0:
        new.extend(lst2)
    else: # len(lst2) == 0
        new.extend(lst1)

    return new

def sorting_merge(lst, posi = 1, mode = 0): # lst -> [(id, value), ....]
    '''
        This function sorts a list [(id, value), ...]
        depends on the aspect chosen
        mode == 0: ascending
        mode == 1: descending
        posi => position of the value being compared
    '''
    midd = int(len(lst)/2)
    if midd == 0:
        return lst
    left = sorting_merge(lst[:midd], posi, mode)
    right = sorting_merge(lst[midd:], posi, mode)
    new = sorting_helper(left, right, posi, mode)
    return new

def order_filter_sort(order_keys, option = None, mode = 1):
    '''
        This function is used to reorder order_list
        option => any key of order_db items
        mode = 1  -> decending
        mode = 0  -> ascending
    '''
    temp = db.load_json()
    order_keys = list(temp['ORDER_DB'].keys())
    rt = []
    temp_lst = [] # [[key, <option>], ...]
    for item in order_keys:
        temp_lst.append([item, temp['ORDER_DB'][item]['id']])
    # sort list for all options
    if option is None:
        return order_keys
    else:
        if option not in temp['ORDER_DB'][order_keys[0]]:
            raise KeyError()
        else:
            for item in temp_lst:
                item[1] = temp['ORDER_DB'][item[0]][option]
            temp_lst = sorting_merge(temp_lst, 1, mode)
    # turn into list of keys
    for item in temp_lst:
        rt.append(item[0])
    return rt

def order_filter_switch(order_keys, option, minn = None, maxx = None):
    '''
        This function filters order based on
        option and the value of the option

        Only allows option with values in range 
        to be returned
    '''
    temp = db.load_json()
    # order_keys = list(temp['ORDER_DB'].keys())
    rt = []
    # sort list for all options
    temp_lst = []
    if option not in temp['ORDER_DB'][order_keys[0]]:
        raise KeyError()
    else:
        for key in order_keys:
            # must have min and max at the same time
            if minn != None and maxx != None \
                and temp['ORDER_DB'][key][option] >= minn \
                and temp['ORDER_DB'][key][option] <= maxx:
                temp_lst.append([key, temp['ORDER_DB'][key][option]])
            else:
                temp_lst.append([key, temp['ORDER_DB'][key][option]])
    # turn into list of keys
    for item in temp_lst:
        rt.append(item[0])
    return rt

def order_filter(option_lst, mode = 1, permission = 'admin', u_id = -1):
    '''
        option_lst => [[option, min, max], ...]
        A combination of
        order_filter_switch
        and
        order_filter_sort
    '''
    temp = db.load_json()
    if permission == 'admin':
        order_keys = list(temp['ORDER_DB'].keys())
    elif permission == 'user':
        order_keys = temp['USER_DB'][str(u_id)]['order']
    else:
        raise ValueError() 
    
    for options in option_lst:
        option, minn, maxx = options
        order_keys = order_filter_sort(order_keys, option)
        order_keys = order_filter_switch(order_keys, option, minn, maxx)
    
    return order_keys

def prod_filter(option_lst, mode = 1):
    '''
        This function is used to filter/reorder product_list
        option_lst => [[option, min, max], ...]
        product:{
            "id": new_id,
            "name": name,
            "price": price,
            "description": description,
            "category": category, # [0] * temp['TYPE_OF_PRODUCTS']
            "delivery": deli_days,
            "ratings": [],
                        # [(u_id, rating), ...]
            "pic": None
        }
    '''
    temp = db.load_json()
    prod_keys = list(temp['PRODUCT_DB'].keys())
    for options in option_lst:
        option, minn, maxx = options
        prod_keys = prod_filter_sort(prod_keys, option, mode)
        prod_keys = prod_filter_switch(prod_keys, option, minn, maxx)
    
    return prod_keys


def prod_filter_switch(prod_keys, option, minn = None, maxx = None):
    '''
        This function filters order based on
        option and the value of the option (['price', 'delivery'])

        Only allows option with values in range 
        to be returned

        usually apply to:
            1. price
            2. delivery days
    '''
    temp = db.load_json()
    # order_keys = list(temp['ORDER_DB'].keys())
    rt = []
    # sort list for all options
    temp_lst = []
    if option not in temp['PRODUCT_DB'][prod_keys[0]]:
        raise KeyError()
    else:
        for key in prod_keys:
            # must have min and max at the same time
            if minn != None and maxx != None \
                and temp['PRODUCT_DB'][key][option] >= minn \
                and temp['PRODUCT_DB'][key][option] <= maxx:
                temp_lst.append([key, temp['PRODUCT_DB'][key][option]])
    # turn into list of keys
    for item in temp_lst:
        rt.append(item[0])
    return rt

def prod_filter_sort(prod_keys, option = None, mode = 1):
    '''
        This function is used to reorder order_list
        mode = 1  -> decending
        mode = 0  -> ascending
    '''
    temp = db.load_json()
    rt = []
    temp_lst = [] # [[key, <option>], ...]
    for item in prod_keys:
        temp_lst.append([item, temp['PRODUCT_DB'][item]['id']])
    # sort list for all options
    if option is None:
        return prod_keys
    else:
        if option not in temp['PRODUCT_DB'][prod_keys[0]]:
            raise KeyError()
        else:
            for item in temp_lst:
                item[1] = temp['PRODUCT_DB'][item[0]][option]
            temp_lst = sorting_merge(temp_lst, 1, mode)
    # turn into list of keys
    for item in temp_lst:
        rt.append(item[0])
    return rt

def rating_calc(prod_id):
    temp = db.load_json()
    ratings = temp['PRODUCT_DB'][str(prod_id)]["ratings"]
    if len(ratings) == 0:
        return 0
    else:
        rt_lst = []
        for item in ratings:
            rt_lst.append(item[1])
        return sum(rt_lst) / len(rt_lst)

def prod_filter_type(prod_lst = [], ctgry = [], \
        price_rg = [0, 99999999], db_name = 'database.json'):
    '''
        This function filters product by category
        and price range
    '''
    temp = db.load_json(db_name)
    all_prod = prod_lst if prod_lst != [] else list(temp["PRODUCT_DB"].keys())
    # filter catagory
    rt1 = []
    rt2 = []
    # if category is chosen
    if ctgry != [] or ctgry != None:
        for prod in all_prod:
            prod_summ = 1
            # for all choson category, product has a positive direction on that category
            for i in range(len(ctgry)):
                if ctgry[i] > 0:
                    prod_summ *= ctgry[i] * temp["PRODUCT_DB"][prod]['category'][i]
            if prod_summ > 0:
                rt1.append(prod)
    else:
        rt1 = all_prod
    # filter price
    rt2 = []
    for prod in rt1:
        if temp["PRODUCT_DB"][prod]['price'] >= price_rg[0] \
            and temp["PRODUCT_DB"][prod]['price'] <= price_rg[-1]:
            rt2.append(prod)
    return rt2

def keyword_searcher(keyword = "", db_name = 'database.json'):
    temp = db.load_json(db_name)
    if keyword == "":
        return list(temp["PRODUCT_DB"].keys())
    else:
        rt = []
        keyword = keyword.lower()
        for prod in list(temp["PRODUCT_DB"].keys()):
            if keyword in temp["PRODUCT_DB"][prod]['name'].lower() \
                or keyword in temp["PRODUCT_DB"][prod]['description'].lower():
                rt.append(prod)
    return rt

def search_filter_recommendation(keyword = "", ctgry = [], \
            price_rg = [0, 99999999], user_id = -1, page = -1, db_name = 'database.json'):
    '''
        This function searches with a keyword, filter with selection,
        and rank product based on recommendation
        keyword_searcher(keyword = "", db_name = 'database.json') -> list
        prod_filter_type(prod_lst = [], ctgry = [], \
            price_rg = [0, 99999999], db_name = 'database.json') -> list
        prod_recommendation(user_id, prod_lst = [], db_name = \
            'database.json', num = 100) -> list
    '''
    rt0 = keyword_searcher(keyword, db_name)
    if len(rt0) == 0:
        rt0 = []
    rt1 = prod_filter_type(rt0, ctgry, price_rg, db_name)
    if user_id != -1:
        rt2 = prod_recommendation(user_id, rt1, db_name)
        rt3 = []
        for item in rt2:
            rt3.append(item[0])
    else:
        rt3 = rt1
    # deal with page number
    if page != -1:
        rt4 = []
        for i in range(len(rt3)):
            if i >= (page-1)*9 and i < page*9:
                # e.g. page 1 => item 0~8
                rt4.append(rt3[i])
    else: # return all prods
        rt4 = rt3
    return {
        "product_lst": rt4,
        "total_pages": us.ceil((len(rt3)/9))
    }



if __name__ == "__main__":
    # print(prod_filter_type(ctgry = [], price_rg = [0, 99999999], \
    #     db_name = 'database_manual.json'))
    # print(prod_filter_type(ctgry = [1, 0, 0], price_rg = [0, 99999999], \
    #     db_name = 'database_manual.json'))
    # print(prod_filter_type(ctgry = [], price_rg = [50, 999999], \
    #     db_name = 'database_manual.json'))
    print(search_filter_recommendation("mother", ctgry = [], \
            price_rg = [0, 99999999], user_id = -1, page = -1, db_name = 'database.json'))