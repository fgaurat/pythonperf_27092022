#!/usr/bin/env python
import sys
import os

def do_log(func):

    def wrapper(*values):
        print("log avant",*values)
        func(*values)
        print("log après")
    
    return wrapper



@do_log
def say_hello(name):
    print("Hello",name)

def main():
    say_hello("fred")

if __name__ == '__main__':
    main()



