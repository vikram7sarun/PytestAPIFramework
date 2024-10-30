# utils/db_helper.py
import sqlite3

def connect_to_database(db_name):
    return sqlite3.connect(db_name)

def verify_user_in_database(conn, user_id, expected_name):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
    return cursor.fetchone()[0] == expected_name
