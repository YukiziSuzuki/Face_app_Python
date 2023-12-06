# app.py

import streamlit as st
import cv2
import face_recognition

def main():
    st.title("顔認証アプリ")

    # カメラを開く
    video_capture = cv2.VideoCapture(0)

    # Streamlit上で表示する画像を格納する変数
    st_image = st.empty()

    while True:
        # カメラからフレームを取得
        ret, frame = video_capture.read()

        # 顔認識の処理
        face_locations = face_recognition.face_locations(frame)

        # 画像に顔の枠を描画
        for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Streamlit上で画像を表示
        st_image.image(frame, channels="BGR", width=640)

        # Streamlitの表示を更新
        #st_image.pyplot()  # これにより画面が更新されます

if __name__ == "__main__":
    main()

