'''
    This file is used to test functions in
    webpage.py
'''
import webpage as wp

def test0():
    a = [(1, 123), (2, 41), (3, 6345), (4, 12), (5, 222), (6, 321)]

    b = [(1, 123), 
        (2, 41), 
        (3, 6345), 
        (4, 12), 
        (5, 222), 
        (6, 321),
        (7, 124), 
        (8, 2222), 
        (9, 329)]

    # print(wp.sorting_helper([(11, 329)], [(10, 32)], 0))
    # print(wp.sorting_helper([(11, 329)], [(10, 32)], 1))
    print(wp.sorting_merge(a, 0))
    print(wp.sorting_merge(a, 1))
    print(wp.sorting_merge(b, 0))
    print(wp.sorting_merge(b, 1))

def test1():
    a = [1, 1, 1]
    b = [1, 1, 1]
    d = [3, 4, 5]
    c = [0, 0, 0, 4]
    e = [8, 3, 1, 1]
    print(wp.angle_between(a, [0,0,0]))
    print(wp.angle_between(a, b))
    print(wp.angle_between(e, c))
    print(wp.angle_between(c, e))
    print(wp.angle_between(a, d))

def test2():
    a = {
        'a': 'aaa',
        'b': 'bbb'
    }
    for item in a:
        print(item)
        print(a[item])

if __name__ == '__main__':
    test0()
    test1()
    test2()