'''
    This file implements a chatbot AI based on provided keyword list
    It uses Information Retrieval technic to calculate the 
        interest vector in user's query and compare with that of 
        product description, to find the best match.
    Upon if the top match is pretty poor (??? w8 definition), 
        chatbot AI should (??? not decided yet)
'''
import re

TEST_KEYWORDS = {
    "men": [1], "man": [1], "dad": [1], "groom": [1], "bridegroom": [1], 
    "father's": [1], "men's": [1], "man's": [1], "family": [1, 2, 3, 5], 
    "women": [2], "woman": [2], "mom": [2], "bride": [2], "mother": [2], 
    "women's": [2], "woman's": [2], "mother's": [2], "lady": [2], "ladies": [2], 
    "lego": [3], "toy": [3], "piano": [3], "bag": [3, 4, 8], "teen": [3], 
    "kid": [3], "kids": [3], "girls": [3], "girl": [3], "boys": [3], 
    "boy": [3], "birthday": [3], "whiskey": [4], "cocktail": [4], 
    "music": [4, 10], "music box": [4], "bluetooth": [4], "friendship": [4], "friend": [4], "friends": [4], "grandma": [5], "grandmother": [5], "grandpa": [5], "grandfather": [5], "couple": [6], "love": [6], "candle": [6], "cooking": [7], "organic": [7], "grilling": [7], "grill": [7], "cook": [7], "pork": [7], "beef": [7], "snack": [7], "sweet": [7], "hot": [7], "spicy": [7], "protein": [7], "health": [7], "healthy": [7], "food": [7, 7], "chocolate": [7], "honey": [7], "wellness": [7], "gluten-free": [7], "vegetarianism": [7], "vegan": [7], 
    "foods": [7], "survival": [8], "gear": [8], "tool": [8], "tools": [8], "flash": [8], "necklace": [9], "earrings": [9], "jewelry": [9], "ring": [9], "gold": [9], "luxury": [9], "pendant": [9], "cloth": [10], "hoodies": [10], "hoody": [10], "travel": [10], 
    "outdoor": [10], "entertainment": [10], "office": [11], "pen": [11], "pens": [11], "professional": [11], "working": [11], "work": [11], "notebook": [11],
}

NUM_CATA = 11

# NEGATION_KEYWORDS = [
#     'not',
#     'don\'t',
#     'doesn\'t',
#     'dislike',
#     'hate',
#     'bad',
# ]

# CONTRARY_KEYWORDS = [
#     'but',
#     'although',
#     'though',
#     'instead',
# ]

TEST_QRY = \
    'I want a toy for children, and my wife. But I don\'t like it for men.\
    My neighbor\'s husband doesn\'t like toy.'

TEST_QRY_UPPER = \
    'I want a toy for children, and my wife. But I don\'t like it for men.\
    My neighbor\'s husband doesn\'t like toy.'.upper()

TEST_QRY_1 = \
    'I don\'t want cat toys nor dog toys'

def query_analysis_test0(qry):
    '''
        This function simply returns the frequency 
        of catagory of keywords
    '''
    lst = re.split("[,.; ]", qry)
    # print(lst)
    vec = [0] * NUM_CATA
    kwds = TEST_KEYWORDS
    for wd in lst:
        if wd in kwds.keys():
            for cate in kwds[wd]:
                vec[cate] += 1
    return vec

def deminishing_returns(num):
    '''
        This function returns a slightly larger number
        then input, with a reduced increasing rate
        for each recursive call.
        e.g. 0 --> 0, 1 --> 1, 2 --> 1.5
    '''
    if num == 0:
        return 0.0
    else:
        summ = 0
        if num > 0:
            while num > 0:
                summ += 1.0/num
                num -= 1
            return summ 
        else: # num < 0
            n = -1 * num 
            while n > 0:
                summ += 1.0/n
                n -= 1
            return -1 * summ

def query_analysis_test1(qry):
    '''
        This function returns the weighted
        frequency of catagory of keywords

        For high frequency words, the score increases slower
    '''
    lst = re.split("[,.; ]", qry)
    # print(lst)
    vec = [0] * NUM_CATA
    kwds = TEST_KEYWORDS
    for wd in lst:
        if wd in kwds.keys():
            for cate in kwds[wd]:
                vec[cate] += 1
    return list(map(deminishing_returns, vec))

def adding_lsts(lst1, lst2): # -> lst
    assert len(lst1) == len(lst2)
    new = []
    for i in range(len(lst1)):
        new.append(lst1[i] + lst2[i])
    return new

def query_analysis_test2(qry):
    '''
        This function returns the weighted score
        of word frequency, but qry is seperated into sections
    '''
    # print(lst)
    qrys = qry.split('.')
    vec = [0] * NUM_CATA
    for qryy in qrys:
        vec = adding_lsts(vec, 
                            query_analysis_test0(qryy))
    return list(map(deminishing_returns, vec))

# def query_analysis_negation_included(qry):
#     '''
#         This function identifies negations inside query
#         Including:[
#             'not', 'don\'t', 'doesn\'t', 'dislike', etc.
#         ]
#     '''
#     negation = False 
#     lst = re.split("[,.; ]", qry)
#     # print(lst)
#     vec = [0] * NUM_CATA
#     kwds = TEST_KEYWORDS
#     for wd in lst:
#         # dentify negation
#         if wd in NEGATION_KEYWORDS:
#             negation = True
#     for wd in lst:
#         # punishing/rewarding values
#         if wd in kwds.keys() and negation == False:
#             vec[kwds[wd]] += 1
#         elif wd in kwds.keys() and negation == True:
#             vec[kwds[wd]] -= 1
#     return vec

def query_analysis_test3(qry):
    '''
        This function identifies negation in qry,
        and punishes the direction on value negated

        <qry> should include product name if name mentions 
        important keywords
    '''
    # print(lst)
    qrys = qry.split('.')
    vec = [0] * NUM_CATA
    for qryy in qrys:
        vec = adding_lsts(vec, 
                            query_analysis_test1(qry.lower()))
    return list(map(deminishing_returns, vec))

def query_analysis_test4(qry):
    '''
        This function breaks small query sentencies
        into branch format to include negation, contrary,
        and, or and etc. relationships
        e.g. My wife likes toys, but not the ones for children or men.

        ==>                       but
                    wife + toy           not (children + men)
    '''
    pass

if __name__ == "__main__":
    print(TEST_QRY)
    print(query_analysis_test0(TEST_QRY))
    print(query_analysis_test1(TEST_QRY))
    print(query_analysis_test2(TEST_QRY))
    print(query_analysis_test3(TEST_QRY))
    print(query_analysis_test3(TEST_QRY_UPPER))
