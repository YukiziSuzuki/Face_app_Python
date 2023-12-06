# app.py

import streamlit as st
import cv2
import numpy as np
import face_recognition

def main():
    st.title("顔認証アプリ")

    uploaded_file = st.file_uploader("画像ファイルをアップロードしてください", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # アップロードされた画像を読み込む
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

        # 顔認識の処理
        face_locations = face_recognition.face_locations(image)

        # 画像に顔の枠を描画
        for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

        # Streamlit上で画像を表示
        st.image(image, channels="BGR")

if __name__ == "__main__":
    main()
