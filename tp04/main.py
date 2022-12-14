#!/usr/bin/env python
import sys
import os

from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo


class Toto:


    def get_surface(self):
        print("Toto get_surface")

def show_surface(o:ICalcGeo):
    print('show_surface',o,o.get_surface())


def main():
    r = Rectangle(2,3)
    c = Carre(2)
    ce = Cercle(2)
    t = Toto()
    
    print("surface Carre",c.get_surface())
    print("surface Cercle",ce.get_surface())
    
    # print(ce)
    # print(r)
    # print(c)
    # c.cote=10
    # print(c.get_surface())

    show_surface(r) # Rectangle
    show_surface(c) # Carre
    show_surface(ce) # Cercle
    show_surface(t) # Cercle
    r.hello()

if __name__ == '__main__':
    main()