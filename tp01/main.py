#!/usr/bin/env python
import sys
import os


def main():

    # Scolaire
    l=[]
    for i in range(10):
        l.append(i)
    print(l)

    # Dev
    l=list(map(lambda i:i,range(10)))
    print(l)

    # Comprehension de list
    l=[i for i in range(10) if i%2==0]
    print(l)



if __name__ == '__main__':
    main()