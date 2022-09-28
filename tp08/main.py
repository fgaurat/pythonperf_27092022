#!/usr/bin/env python
import sys
import os


def main():
    dao = TodoDAO('./todos_db.sqlite')


    todos = dao.findAll()

    for todo in todos:
        print(todo.title)

if __name__ == '__main__':
    main()