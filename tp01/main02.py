#!/usr/bin/env python
from collections import deque
import sys
import os



# HelloWorld => UpperCamelCase / PascalCase 
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => train-case, spin-case, kebab-case => web : background-color => backgroundColor

def add(l1,l2,*values):
    """
    function add values
    """
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
# def hello01(*,name,firstName,/):
    print("Hello",name,firstName)

def main02():
    # hello(firstName="Fred",name="Gaurat",age=46)
    d = {'firstName': 'Fred', 'name': 'Gaurat', 'age': 46}

    # s = "Hello {name} {firstName} {age}".format(name=d['name'],firstName=d['firstName'],age=d['age'])
    s = "Hello {name} {firstName} {age}".format(**d)
    print(s)
    hello01("Gaurat","Fred")
    hello01(name="Gaurat",firstName="Fred")



def main():
    
    l = [20,30,40,50]
    print(l)
    l.append(60)
    print(l)
    i = l.pop()
    print(l)
    print(i)
    l.pop(0)
    print(l)
    l.insert(0,10)
    print(l)

    
    d = deque(l)



    print(d)
    d.pop()
    print(d)
    d.popleft()
    print(d)
    d.appendleft(20)
    print(d)
    print(d[2])
    d[2] = 1000
    print(d)




if __name__ == '__main__':
    main()