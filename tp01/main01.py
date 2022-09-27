import sys
import pck.lemodule as lm
import copy
from pck.lemodule import hello as hl


def main02():
    l = [10,20,30,40,50]
    l[0] = 1000
    s1 = l[2:4]
    s1[0] =1000
    
    print(l)
    print(s1)
    print(l[:3])
    print(l[3:])

    
    l1 = l[:]
    l1[0] = 10
    print(l)
    print(l1)

    print(50*'-')
    a = [10,20]
    b = [30,40]
    c = [50,60]
    l = [a,b,c]

    l1 = copy.deepcopy(l)
    l[1][1] = 12
    print(l)
    print(l1)


def main01():
    print(sys.getrefcount(2))
    a=2 # inférence de type
    b=2
    print(sys.getrefcount(2))
    print("a",hex(id(a)))
    print("b",hex(id(b)))
    a=3
    print(hex(id(a)))
    # hello = lemodule.hello("Fred")
    hello = lm.hello("Fred")
    print(hello)


if __name__ == '__main__':
    main01()