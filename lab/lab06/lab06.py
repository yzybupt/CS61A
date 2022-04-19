this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    c = -1
    def f(b):
        nonlocal c
        c = c + 1
        return a + b + c
    return f



def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    l_last = 0 
    last = 0
    n = -1
    def f():
        nonlocal n
        nonlocal l_last
        nonlocal last
        n = n + 1
        if n == 0:
            return 0
        
        if n == 1:
            l_last = 0
            last = 1
            return 1
        
        temp = l_last
        l_last = last
        last = temp + last
        return last
    return f



def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    """Actually, this is still a recurvisive probelm, but we need to use nonlocal to keep a global variable"""
    indexes = []
    flag = -1
    for i in range(len(lst)):
        if lst[i] == entry:
            flag = flag + 1
            indexes = indexes + [i + 1 + flag]
    

    def f():
        nonlocal lst
        nonlocal indexes

        if len(indexes) == 0:
            return 
        
        lst.append(elem)
        lst[indexes[0] + 1:] = lst[indexes[0]: len(lst) - 1]
        lst[indexes[0]] = elem
        indexes = indexes[1:]
        f()
        return
    
    f()
    return lst


    


    
    


