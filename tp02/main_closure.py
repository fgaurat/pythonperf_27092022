#!/usr/bin/env python
import sys
import os


def say_hello(hello):

    a = "toto" 
    
    def to(name):
        b = "titi"
        return f"{hello} {name} {a} {b}"

    return to





def main():
    bonjour = say_hello('Bonjour')
    hello = say_hello('Hello')

    print(bonjour('fred'))
    print(hello('fred'))

    print(say_hello('Bonjour')("fred"))


if __name__ == '__main__':
    main()