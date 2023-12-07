# insert_record.py
#データベースを更新するプログラム

import sqlite3
from datetime import datetime

def insert_record(name, action):
    conn = sqlite3.connect("user_records.db")
    c = conn.cursor()

    c.execute('''
        INSERT INTO user_records (name, action)
        VALUES (?, ?)
    ''', (name, action))

    conn.commit()
    conn.close()


#入室状態へと変更する関数
def update_leaving_room_and_timestamp(cursor, name, new_leaving_room):
    update_query = "UPDATE user_records SET Leaving_The_Room = ?, timestamp = ? WHERE name = ?"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (new_leaving_room, timestamp, name)

    try:
        cursor.execute(update_query, data)
        print("データが更新されました。")
    except sqlite3.Error as e:
        print(f"エラー: {e}")



#退室状態へと変更する関数
def update_leaving_room_and_timestamp(cursor, name, new_out_of_room):
    update_query = "UPDATE user_records SET Out_Of_The_Room = ?, timestamp = ? WHERE name = ?"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (new_out_of_room, timestamp, name)

    try:
        cursor.execute(update_query, data)
        print("データが更新されました。")
    except sqlite3.Error as e:
        print(f"エラー: {e}")


#帰宅状態へと変更する関数
def update_leaving_room_and_timestamp(cursor, name, new_going_home):
    update_query = "UPDATE user_records SET Going_home = ?, timestamp = ? WHERE name = ?"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (new_going_home, timestamp, name)

    try:
        cursor.execute(update_query, data)
        print("データが更新されました。")
    except sqlite3.Error as e:
        print(f"エラー: {e}")