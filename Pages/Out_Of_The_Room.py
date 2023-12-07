# 顔認識を行い、外出処理を行うページ

import streamlit as st
import cv2
import face_recognition
import numpy as np
import os
import sqlite3
from datetime import datetime

def load_known_faces(directory="known_faces"):
    known_faces = []
    known_names = []

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(os.path.splitext(filename)[0])

    return known_faces, known_names

def update_out_of_the_room_and_timestamp(cursor, name, new_leaving_room):
    # ユーザーのデータを取得
    select_query = "SELECT Out_Of_The_Room FROM user_records WHERE name = ?"
    cursor.execute(select_query, (name,))
    current_leaving_room = cursor.fetchone()

    # ユーザーが存在しない場合は処理を終了
    if current_leaving_room is None:
        print("指定されたユーザーが見つかりません。")
        return

    # Leaving_The_Room が "O" の場合は処理を行わずに関数を終了
    if current_leaving_room[0] == "O":
        print("Out_Of_The_Room が 'O' です。処理をスキップします。")
        return

    # 更新クエリの実行
    update_query = "UPDATE user_records SET Leaving_The_Room = 'X', Out_Of_The_Room = 'O', Going_home= 'X', timestamp = ? WHERE name = ?"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (timestamp, name)

    try:
        cursor.execute(update_query, data)
        st.write(name, "データが更新されました。")
    except sqlite3.Error as e:
        print(f"エラー: {e}")


def get_all_records(cursor):
    select_all_query = "SELECT * FROM user_records"
    cursor.execute(select_all_query)
    records = cursor.fetchall()
    return records

def display_all_records(records, st_db_info):

    # データベースのレコードを表示
    for i in range(len(records)):
        st_element[i].text(records[i])





def main():
    st.title("外出")

    conn = sqlite3.connect("Lab_menber.db")
    c = conn.cursor()





    # カメラを開く
    video_capture = cv2.VideoCapture(0)

    # 事前に保存された顔の情報を読み込む
    known_faces, known_names = load_known_faces()

    # Streamlit上で表示する画像と名前を格納する変数
    st_image = st.empty()
    st_name = st.empty()

    # データベースのカラム名を取得
    st.write("ID, 　　名前, 　学年, 　入室, 　退室, 　帰宅, 　　timestamp")

    st_db_info = []
    for i in range(10):
        st_db_info.append(st.empty())


    while True:
        # カメラからフレームを取得
        ret, frame = video_capture.read()

        # 顔認識の処理
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # 画像に顔の枠を描画
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # 保存された顔との照合を行う
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"

            # 照合が成功した場合、名前を取得
            face_distances = face_recognition.face_distance(known_faces, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                # 近似度が一定以下の場合、"Unknown"を表示
                if face_distances[best_match_index] > 0.4:
                    name = "Unknown"
                    st_name.text(name)
                else:
                    name = known_names[best_match_index]

                    # 照合が成功したら名前を表示
                    st_name.text(name)

                    
                    update_out_of_the_room_and_timestamp(c, name, "O")
                        
        # Streamlit上で画像を表示
        st_image.image(frame, channels="BGR", width=640)

        # 常時データベースの内容を取得して表示
        records = get_all_records(c)
        display_all_records(records, st_db_info)

if __name__ == "__main__":
    main()
