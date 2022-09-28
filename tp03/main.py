#!/usr/bin/env python
import sys
import os

from Rectangle import Rectangle


def main():
    r = Rectangle(2,3)
    print(r.get_longueur())
    assert r.get_longueur() == 2

    r.set_longueur(12)
    print(r.get_longueur())


    print(r)    

if __name__ == '__main__':
    main()