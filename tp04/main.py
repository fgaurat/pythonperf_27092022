#!/usr/bin/env python
import sys
import os

from Rectangle import Rectangle
from Carre import Carre


def main():
    # r = Rectangle(2,3)
    # print(r)
    c = Carre(2)
    print(c.get_surface())

    print(c)
    c.cote=10
    print(c.get_surface())
if __name__ == '__main__':
    main()