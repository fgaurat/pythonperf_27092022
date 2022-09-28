#!/usr/bin/env python
import sys
import os

from TodoDAO import TodoDAO


def main():
    dao = TodoDAO('./tp08/todos_db.sqlite')


    todos = dao.find_all()

    for todo in todos:
        print(todo)

if __name__ == '__main__':
    main()