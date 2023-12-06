#######データベースに登録されている内容の表示#######



import sqlite3

def display_records(cursor):
    select_query = "SELECT * FROM user_records"
    cursor.execute(select_query)
    records = cursor.fetchall()

    if not records:
        print("データベースにはまだレコードがありません。")
    else:
        print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<20}".format("Name", "Year", "Leaving", "Out of Room", "Going Home", "Timestamp"))
        print("-" * 90)
        for record in records:
            print("{:<15} {:<10} {:<15} {:<15} {:<15} {:<20}".format(record[0], record[1], record[2], record[3], record[4], record[5]))

def main():
    conn = sqlite3.connect('your_database_name.db')
    cursor = conn.cursor()

    display_records(cursor)

    conn.close()

if __name__ == "__main__":
    main()