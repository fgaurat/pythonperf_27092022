#!/usr/bin/env python
import sys
import os


def fib(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b


def mult2(flux):

    for v in flux:
        yield v*2


def get_even(flux):

    for v in flux:
        if v %2 ==0:
            yield v


def main():
    # v = fib(1000)
    # print(next(v))
    # print(next(v))
    # print(next(v))
    


    # l = list(fib(1000))
    # print(l)
     
    # fib(1000) | get_even | mult2 
    for v in mult2(get_even(fib(1000))):
        print(v)

    v = (i for i in range(10))
    print(v)


if __name__ == '__main__':
    main()