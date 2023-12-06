# insert_record.py

import sqlite3

def insert_record(name, action):
    conn = sqlite3.connect("user_records.db")
    c = conn.cursor()

    c.execute('''
        INSERT INTO user_records (name, action)
        VALUES (?, ?)
    ''', (name, action))

    conn.commit()
    conn.close()