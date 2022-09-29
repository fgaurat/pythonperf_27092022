#!/usr/bin/env python
import multiprocessing
import sys
import os
from multiprocessing import Pool

def f(x):
    return x*x

def main():
    with Pool(multiprocessing.cpu_count()) as p:
        print(p.map(f, [1, 2, 3]))

if __name__ == '__main__':
    main()