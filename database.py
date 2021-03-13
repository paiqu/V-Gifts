'''
    This file includes all database structure for 
    all databases, DO NOT make ANY CHANGE
    without notifying other members. Upon adding new
    attributes, PLEASE do pytest to remove any
    conflict changes.
'''
# may create class objects instead later


# main content
    # '''
    #     This DB stores the next id should be used upon
    #     creating new user/admin/product/order
    # '''
ID_DB = {
    'USER_DB': 1,
    'ADMIN_DB': 1,
    'PRODUCT_DB': 0,
    'ORDER_DB': 0
    
}


USER_DB = {
    # '''
    # format:
    #     '<id>':                 # type: string
    #             <User class object>
    #         contains:
    #         {                
    #         'id': 1             # type: int, serial
    #         'name': 'Zard'      # type: string
    #         'email': '123@unsw' # type: string
    #         'fund': 10          # type: int; unit: $
    #         'address': 'Pacific Ocean'
    #                             # type: string
    #         'cart': [list of product ID]
    #                             # type: list of int
    #         'orders': [list of order ID]
    #                             # type: list of int
    #         'interests': [('cheap', 1.0), ...]
    #                             # type: list of tuple, tuple of (feature, weight)
    #                             #                                string,  float
    #     }
    # '''
    '1':  {
        'id':1,
        'name': 'Tim',
        'password':'12312313',
        'email': '123@unsw',
        'fund': 0,
        'address':'',
        'cart': [],
        'orders':[],
        'interests':[]
    }
    
}

ADMIN_DB = {
    # '''
    # format:
    #     '<id>':{                 # type: string
    #             <Admin class object>
    #         contains:
    #         {     
    #         'id': 2             # type: int, serial
    #         'name': 'YYF'       # type: string
    #         'admin_token': '198ANFu72oDJ0827'
    #                             # type: string
    #     }
    # '''
    '1':  {
        'id': 1,
        'name': 'Tim',
        'password': '123456'
    }
}

PRODUCT_DB = {
    '''
    format:
        '<id>':{                 # type: string
                <Product class object>
            contains:
            {     
            'id': 3             # type: int, serial
            'name': 'gift_1'    # type: string
            'pic': ??????
                                # type: string, website or file name
            'description': 'good'
                                # type: string
            'feature': ['cheap', 'durable']
                                # type: list of string, adjective words
            'delivery': datetime_object
                                # type: leng of time (mm/dd)
        }
    '''
}

ORDER_DB = {
    '''
    format:
        '<id>':{                 # type: string
                <Order class object>
            contains:
            {      
                                        e.g. '<id>' means: '3' for item with 'id': 3
            'id': 4             # type: int, serial
            'product_id': 3     # type: int
            'user_id': 2        # type: int
            'order_date': datetime_object
                                # type: datetime_object
            'delivery_date': datetime_object
                                # type: datetime_object
            'delivery_state': 0
                                # type: int, [0: not delivered,
                                #             1: on the way,
                                #             2: delivered,
                                #             3: cancelled]
        }
    '''
}

TOKEN_DB = {
    # '''
    # format:
    # {
    #     'Tim': 'token'          # type: string
    #     'Amy': '...'     
    # }

}