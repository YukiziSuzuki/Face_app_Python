# app.py

# ...（前のコード）

from insert_record import insert_record

# ...（後のコード）

while True:
    # ...（前のコード）

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
            if face_distances[best_match_index] > 0.6:
                name = "Unknown"
            else:
                name = known_names[best_match_index]

                # データベースに記録を挿入
                insert_record(name, "入室")  # ここでアクションを適切に設定

            # 照合が成功したらボタンを表示
            st_name.text(name)
            entry_clicked = entry_button
            leave_clicked = leave_button
            return_home_clicked = return_home_button

            if entry_clicked:
                st.text("入室しました")
                insert_record(name, "入室")
            elif leave_clicked:
                st.text("外出しました")
                insert_record(name, "外出")
            elif return_home_clicked:
                st.text("帰宅しました")
                insert_record(name, "帰宅")

# ...（後のコード）