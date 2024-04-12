import sqlite3
from sqlite3 import Error, Connection


@staticmethod
def create_connection() -> Connection:

    try:
        conn = sqlite3.connect("instance/Database.db")
        conn.row_factory = sqlite3.Row
    except Error as e:
        print(e)

    return conn
