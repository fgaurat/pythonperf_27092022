#!/usr/bin/env python
import sys
import os
from dataclasses import dataclass


@dataclass
class Rectangle:
    longueur:int=0
    largeur:int=0

    def surface(self):
        return self.longueur*self.largeur

def main():
    r = Rectangle(10,2)
    print(r)
    print(r.surface())

if __name__ == '__main__':
    main()