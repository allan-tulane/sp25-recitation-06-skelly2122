def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1  # track how many times we try to compute F(n) 
    if n == 0:  # base case: F(0) is 0 
        return 0
    elif n == 1:  # base case: F(1) is 1 
        return 1
    else:
        # classic recursion: split into two smaller problems and pray for no stack overflow
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

def fib_top_down(n, fibs):
    if fibs[n] != -1:  
        return fibs[n]
    if n == 0:  # F(0) is still 0
        fibs[n] = 0
    elif n == 1:  # F(1) is still 1
        fibs[n] = 1
    else:
        # compute F(n) by asking its parents and store it so we don't have to do this again
        fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
    return fibs[n]  # straight from cache


def fib_bottom_up(n):
    if n == 0:  # edge case: F(0) is 0, no work needed
        return 0
    fibs = [0] * (n + 1)  # create a list to store all F(i) from 0 to n
    fibs[0] = 0  # F(0) is 0
    if n >= 1:  # set F(1) if n is at least 1
        fibs[1] = 1
    for i in range(2, n + 1):  # start from 2 and build up 
        fibs[i] = fibs[i-1] + fibs[i-2]  # F(i) = F(i-1) + F(i-2)
    return fibs[n]  # return the last one
