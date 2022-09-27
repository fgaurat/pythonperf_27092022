#!/usr/bin/env python
import sys
import os


def add(l1,l2,*values):
    print(values)
    result = 0
    for v in values:
        result+=v

    return result





def main01():

    l = [10,20,30,40]
    print(l)
    s = add(10,20,30,40)
    print(s)
    s = add(*l)
    print(s)

    a,b = [10,20,30,40]


def hello(**kwargs):
    print(kwargs.values())
    print("Hello",*kwargs.values())


# def hello01(pos1,pos2,/,pos_kws1,pos_kws2,*,kw1,kw2):
# def hello01(name,firstName,/):
def hello01(*,name,firstName):
    print("Hello",name,firstName)

def main():
    # hello(firstName="Fred",name="Gaurat",age=46)
    d = {'firstName': 'Fred', 'name': 'Gaurat', 'age': 46}

    # s = "Hello {name} {firstName} {age}".format(name=d['name'],firstName=d['firstName'],age=d['age'])
    s = "Hello {name} {firstName} {age}".format(**d)
    print(s)
    hello01("Gaurat","Fred")
    hello01(name="Gaurat",firstName="Fred")



if __name__ == '__main__':
    main()