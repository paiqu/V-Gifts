durian = {
    '1': {
        'user': 'Chenkai',
        'age': 12
    },
    '2': {
        'user': 'BoA',
        'age': 18
    }
}



for user, user_info in durian.items():
    print(user)
    print(user_info)
    
for user_id, user_info in durian.items():
        if user_info['user'] is 'Chenkai':
                print('success')

print('Do not find')