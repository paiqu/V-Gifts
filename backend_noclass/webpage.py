'''
    This file contains webpage operations
    including:
        item sorting
        order sorting
        product recommendation
'''
import random as rd
import numpy as np
import database_pai as dbp

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

def prod_recommendation(user_id, num = 10):
    '''
        This function calculates the similarity between
        user_interest vector and
        product feature
        to rank products and recommend

        returns a list of product_id, sorted
    '''
    # item & value calculator
    lst = prod_picker(1.0)
    # return sorted result (descending)
    return sorting_merge(lst, 1)


def interest_calculator(v_1, v_2, key):
    '''
        for example
        u_interest = [1, 2, 3, 4, 5]
        it_feature = [6, 7, 8, 9, 10]
    '''
    return (key, angle_between(v_1, v_2))
    

def prod_picker(user_id, percent): # percent -> the chance of product is joining the recommendation
    # prod_lst = DB
    temp = dbp.Database()
    temp = temp.load_json()
    prod_lst = temp.export_product()
    user_lst = temp.export_user()
    # append to lst
    lst = []
    for item in prod_lst:
        rdd = rd.randint(0, 100)
        if rdd > 100 * percent:
            v_1 = prod_lst[item].e_feature()
            v_2 = user_lst[str(user_id)].e_interest()
            lst.append(interest_calculator(v_1, v_2, item))
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
