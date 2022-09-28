import sqlite3
from typing import List
from Todo import Todo


class TodoDAO:

    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)

    
    def find_all(self):
        cur = self._con.cursor()
        res = cur.execute('SELECT * FROM todos_tbl')
        for id,title,completed in res.fetchall():
            t = Todo(id,title,completed)
            yield t


    def __del__(self):
        self._con.close()