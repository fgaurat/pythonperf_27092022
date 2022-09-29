#!/usr/bin/env python
import sys
import os
import httpx

from TodoDAO import TodoDAO
from Todo import Todo



def main():
    dao = TodoDAO('./todos_db.sqlite')

    url = "https://jsonplaceholder.typicode.com/todos"
    response = httpx.get(url)
    todos = response.json()

    for todo in todos:
        # del todo['id']
        # del todo['userId']
        t = Todo(**todo)
        # Todo(title="Une autre todo",completed=True)
        dao.save(t)

    todos = dao.find_all()
    for todo in todos:
        print(todo)



def main_test_dao():
    dao = TodoDAO('./todos_db.sqlite')

    t = Todo(title="Une autre todo",completed=True)

    dao.save(t)
    todos = dao.find_all()

    for todo in todos:
        print(todo)

if __name__ == '__main__':
    main()