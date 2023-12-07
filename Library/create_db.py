#データベースの作成及び、データの追加を行うプログラム
import sqlite3
from datetime import datetime

def create_table(cursor):
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS user_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year TEXT NOT NULL,
            Leaving_The_Room TEXT NOT NULL,
            Out_Of_The_Room TEXT NOT NULL,
            Going_home TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    '''
    cursor.execute(create_table_query)

def insert_data(cursor, name, year, leaving, out_of_room, going_home):
    insert_query = '''
        INSERT INTO user_records (name, year, Leaving_The_Room, Out_Of_The_Room, Going_home)
        VALUES (?, ?, ?, ?, ?)
    '''
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (name, year, leaving, out_of_room, going_home)

    try:
        cursor.execute(insert_query, data)
        print("データが挿入されました。")
    except sqlite3.IntegrityError:
        print("エラー: 主キーが重複しています。")

def main():
    conn = sqlite3.connect('Lab_menber.db')
    cursor = conn.cursor()

    create_table(cursor)

    name = input("名前: ")
    year = input("年: ")
    leaving = input("Leaving The Room: ")
    out_of_room = input("Out Of The Room: ")
    going_home = input("Going Home: ")

    insert_data(cursor, name, year, leaving, out_of_room, going_home)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()