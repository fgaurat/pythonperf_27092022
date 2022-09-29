#!/usr/bin/env python
from ctypes.util import find_library
import sys
import os
import traceback
import logging

# logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s',filename='example.log', encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch2 = logging.FileHandler(filename='example.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(processName)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
ch2.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(ch2)
logger.setLevel(logging.INFO)

def division(a,b):
    return a/b

def call_division(a,b):
    print(20*'-',"avant",20*'-')
    r=0
    try:
        r = division(a,b)
    finally:
        print(20*'-',"après",20*'-')
    return r

def main():
    logger.warning('Watch out!')
    logger.info('info')
    try:
        a=2
        b=0
        c = call_division(a,b)

        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError Erreur !")
        print(e)
        traceback.print_exc()
        logger.error('error !'+str(e))
    except TypeError as e:
        print("TypeError Erreur !")
        print(e)
        traceback.print_exc()
    except Exception as e:
        print("Exception Erreur !")
        print(e)
        traceback.print_exc()
        logger.error('error !'+str(e))
    else:
        print("pas d'erreurs")
    finally:
        print("finally")

    print("après")

if __name__ == '__main__':
    main()