#!/usr/bin/env python
import sys
import os


class A:
    def __init__(self, valA):
        self.valA = valA
        print(f"A def __init__(self, {valA}):")

    def the_method(self):
        print(self)
        print("the_method A",self.valA)

class B(A):
    def __init__(self, valB):
        super().__init__(valB)
        print(f"B def __init__(self, {valB}):")

    def the_method(self):
        print("the_method B",self.valA)

class C(B):
    def other_method(self):
        print("other_method")
        # print(C.__mro__)
        # super(B).the_method()
        print(super())
        print(super(A))
        print(super(B,self))
        print(super(B,self).the_method())
        # print(super(A).the_method())
        

def main():
    a = A(1)
    print(50*'-')
    b = B(2)
    print(50*'-')
    c = C(3)
    c.other_method()

if __name__ == '__main__':
    main()