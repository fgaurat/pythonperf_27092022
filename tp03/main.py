#!/usr/bin/env python
import sys
import os

from Rectangle import Rectangle


def main():
    r = Rectangle(2,3)
    print(r.longueur)
    assert r.longueur == 2

    r.longueur = 12
    print(r.longueur)
    print(r.largeur)
    print(r._Rectangle__toto)

    
    print(r)

if __name__ == '__main__':
    main()