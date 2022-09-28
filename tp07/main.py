#!/usr/bin/env python
import sys
import os
from Rectangle import Rectangle
from Cercle import Cercle


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
    r2 = Rectangle(1252, 4564563)

    c1 = Cercle(2)
    c2 = Cercle(2)
    print(hex(id(r1)))
    print(hex(id(r2)))
    print(r1) 
    print(r2) 
    r1.longueur = 10
    print(r1) 
    print(r2) 
    print(hex(id(c1)))
    print(hex(id(c2)))
    print(c1) 
    print(c2) 
    c1.rayon = 20 
    print(c1) 
    print(c2) 
if __name__ == '__main__':
    main()
