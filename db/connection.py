import sqlite3

db_connection = "C:/Users/kazido/Projects/week_6/Project_intellgence/db/example.db"

def get_connection():
    return sqlite3.connect(db_connection)


