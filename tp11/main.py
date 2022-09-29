#!/usr/bin/env python
import sys
import os

from TodoDAO import TodoDAO


def main():
    # f = open('workfile', 'w', encoding="utf-8")
    # print("open")
    # with open('workfile', 'w', encoding="utf-8") as f:
    #     print("opened")
    #     print("work")
    # print(f.closed)

    with TodoDAO('./tp11/todos_db.sqlite') as dao:
        print("ok")
if __name__ == '__main__':
    main()