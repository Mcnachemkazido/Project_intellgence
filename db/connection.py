import sqlite3

db_connection = "C:/Users/kazido/Projects/week_6/Project_intellgence/db/example.db"

def get_connection():
    conn = sqlite3.connect(db_connection)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


