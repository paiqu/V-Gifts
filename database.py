'''
    This file includes all database structure for 
    all databases, DO NOT make ANY CHANGE
    without notifying other members. Upon adding new
    attributes, PLEASE do pytest to remove any
    conflict changes.
'''

ID_DB = {
    '''
        This DB stores the next id should be used upon
        creating new user/admin/product/order
    '''
    'USER_DB': 0,
    'ADMIN_DB': 0,
    'PRODUCT_DB': 0,
    'ORDER_DB': 0
}


USER_DB = {
    '''
    format:
        '<id>':{                # type: string
            'id': 1             # type: int, serial
            'name': 'Zard'      # type: string
            'fund': 10          # type: int; unit: $
            'address': 'Pacific Ocean'
                                # type: string
            'cart': [list of product ID]
                                # type: list of int
            'orders': [list of order ID]
                                # type: list of int
            'interests': [('cheap', 1.0), ...]
                                # type: list of tuple, tuple of (feature, weight)
                                #                                string,  float
        }
    '''
}

ADMIN_DB = {
    '''
    format:
        '<id>':{                # type: string
            'id': 2             # type: int, serial
            'name': 'YYF'       # type: string
            'admin_token': '198ANFu72oDJ0827'
                                # type: string
        }
    '''
}

PRODUCT_DB = {
    '''
    format:
        '<id>':{                # type: string
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
        '<id>':{                # type: string, 
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