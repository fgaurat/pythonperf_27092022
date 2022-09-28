#!/usr/bin/env python
import sys
import os
from Rectangle import Rectangle


class Test:

    def __new__(cls):
        print("__new__")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("__init__")

    def __call__(cls) -> None:
        print("__call__",cls)


def main():
    r1 = Rectangle(2, 3)
    r2 = Rectangle(2, 3)

    # r = Rectangle.build_from_str("2,3")
    # print(r)
    # t = Test()
    # t()
    print(hex(id(r1)))
    print(hex(id(r2)))
    r1.longueur =1000
    print(r1) 
    print(r2) 

if __name__ == '__main__':
    main()
