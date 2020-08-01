import sqlite3

from PyQt5.QtSql import *

class DB(QSqlDatabase):
    def __init__(self):
        super(DB, self).__init__()
        self = self.addDatabase("QSQLITE")
        self.setDatabaseName("todolist.db")
        self.open()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()



def load(finish_state):
    conn = sqlite3.connect("todolist.db")
    cursor = conn.cursor()

    cursor.execute("select * from todolist;")
    return cursor.fetchall(), cursor.rowcount



def init_model():
    conn = sqlite3.connect("todolist.db")
    cursor = conn.cursor()

    with open("schema.sql") as f:
        for sql in f.read().split(";"):
            cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_model()