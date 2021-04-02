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
    # This TEST KEYWORD is used to analyse
    # user query, following has format of:
    #     'keywords': <position of catagory in catagoty list (product)
    #                            / interest in interest list (user)>

    # for men
    'men': 0,
    'husband': 0,
    # for women
    'wowen': 1,
    'wife': 1,
    # for kids
    'children': 2,
    'child': 2,
    'toy': 2,
    'toys': 2,
    # for pet
    # 'pet': 3,
    # 'cat': 3,
    # 'dog': 3,
    # descriptive:
    # not yet
}

NUM_CATA = 3

NEGATION_KEYWORDS = [
    'not',
    'don\'t',
    'doesn\'t',
    'dislike',
    'hate',
    'bad',
]

CONTRARY_KEYWORDS = [
    'but',
    'although',
    'though',
    'instead',
]

TEST_QRY = \
    'I want a toy for children, and my wife. But I don\'t like it for men.\
    My neighbor\'s husband doesn\'t like toy.'

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
            vec[kwds[wd]] += 1
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
            vec[kwds[wd]] += 1
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

def query_analysis_negation_included(qry):
    '''
        This function identifies negations inside query
        Including:[
            'not', 'don\'t', 'doesn\'t', 'dislike', etc.
        ]
    '''
    negation = False 
    lst = re.split("[,.; ]", qry)
    # print(lst)
    vec = [0] * NUM_CATA
    kwds = TEST_KEYWORDS
    for wd in lst:
        # dentify negation
        if wd in NEGATION_KEYWORDS:
            negation = True
    for wd in lst:
        # punishing/rewarding values
        if wd in kwds.keys() and negation == False:
            vec[kwds[wd]] += 1
        elif wd in kwds.keys() and negation == True:
            vec[kwds[wd]] -= 1
    return vec

def query_analysis_test3(qry):
    '''
        This function identifies negation in qry,
        and punishes the direction on value negated
    '''
    # print(lst)
    qrys = qry.split('.')
    vec = [0] * NUM_CATA
    for qryy in qrys:
        vec = adding_lsts(vec, 
                            query_analysis_negation_included(qryy))
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
