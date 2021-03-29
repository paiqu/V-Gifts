'''
    This file implements a chatbot AI based on provided keyword list
    It uses Information Retrieval technic to calculate the 
        interest vector in user's query and compare with that of 
        product description, to find the best match.
    Upon if the top match is pretty poor (??? w8 definition), 
        chatbot AI should (??? not decided yet)
'''

def query_analysis(qry):
    if len(qry) == 0:
        return {}
