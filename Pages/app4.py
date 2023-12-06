# app.py

import streamlit as st
import cv2
import face_recognition
import numpy as np
import os

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

def main():
    st.title("顔認証アプリ")

    # カメラを開く
    video_capture = cv2.VideoCapture(0)

    # 事前に保存された顔の情報を読み込む
    known_faces, known_names = load_known_faces()

    # Streamlit上で表示する画像と名前を格納する変数
    st_image = st.empty()
    st_name = st.empty()

    # 入室、外出、帰宅のボタン
    entry_button = st.button("入室")
    leave_button = st.button("外出")
    return_home_button = st.button("帰宅")

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

                    # 照合が成功したらボタンを表示
                    st_name.text(name)
                    entry_clicked = entry_button
                    leave_clicked = leave_button
                    return_home_clicked = return_home_button

                    if entry_clicked:
                        st.text("入室しました")
                    elif leave_clicked:
                        st.text("外出しました")
                    elif return_home_clicked:
                        st.text("帰宅しました")

        # Streamlit上で画像を表示
        st_image.image(frame, channels="BGR", width=640)


if __name__ == "__main__":
    main()
