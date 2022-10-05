import numba as nb
import sys
import functools
import time
sys.setrecursionlimit(100000)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        if i in fibonacci_cache:
            return fibonacci_cache[i]
        a, b = b%(10**9+7), (a + b)%(10**9+7)
        fibonacci_cache[n] = a%(10**9+7)
    return a

def fibonacci_cache_func(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1 or n == 0:
        fibonacci_cache[n] = n
        return n
    fibonacci_cache[n] = (fibonacci_cache_func(n-1) + fibonacci_cache_func(n-2))%(10**9+7)
    return fibonacci_cache[n]

@functools.lru_cache(None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n-1)%(10**9+7) + fib_cache(n-2)%(10**9+7)

@nb.jit(nopython=True, fastmath=True)
def fib(term_num,counter,n0,n1):
    if term_num == 0:
        print(0)
    elif term_num == 1 | term_num == 2:
        print(1)
    else:
        while counter < term_num:
            largest_term = n0 + n1
            n0 = n1
            n1 = largest_term
            counter += 1
    return n0    

def fib_fast(n):
    m = 10**9+7
    if n == 0:
        return n
    v1, v2, v3 = 1, 1, 0    
    for rec in bin(n)[3:]:  
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = (v1+v2)%m, v1%m, v2%m
    return v2%m

def fib_short(n):
    a, b = 1, 0
    m = 10**9+7
    for i in bin(n):
        a, b = a*a+b*b, b*(a+a+b)
        if i == "1":
            a, b = b, a + b
        a %= m
        b %= m
    return b

'''
term_num = int(input())
n0,n1 = 0,1
counter = 0
print(fib(term_num,counter,n0,n1) %(10**9+7))
print(10**9+7)
'''
def benchmark(n, *args):
    print("-" * 80)
    for func in args:
        print(func.__name__)
        start = time.time()
        try:
            if func.__name__ == 'fib':
                n0,n1 = 0,1
                counter = 0
                ret = func(n,counter,n0,n1)
            else:
                ret = func(n)
            #print("Result:", ret)
        except RuntimeError as e:
            print("Error:", e)
        end = time.time()
        print("Time:", "{:.8f}".format(end - start))
        print()

fibonacci_cache = {}
n = int(input())
#benchmark(1000, fib, fib_cache, fib_fast, fibonacci, fibonacci_cache_func, fib_short)
print(fib_short(n))
benchmark(n, fib_short)
