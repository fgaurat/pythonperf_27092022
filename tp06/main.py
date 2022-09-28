#!/usr/bin/env python
import sys
import os

from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeoProtocol import ICalcGeoProtocol


class Toto:
    def surface(self):
        print("Toto get_surface")

def show_surface(o:ICalcGeoProtocol):
    print('show_surface',o,o.get_surface())


def main():
    r = Rectangle(2,3)
    c = Carre(2)
    ce = Cercle(2)
    t = Toto()
    print("surface Carre",c.get_surface())
    print("surface Cercle",ce.get_surface())

    show_surface(r) # Rectangle
    show_surface(c) # Carre
    show_surface(ce) # Cercle
    show_surface(t) # Cercle

if __name__ == '__main__':
    main()