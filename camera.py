import cv2
import mediapipe as mp
import time
import os

def start_camera():
    if not os.path.exists("images"):
        os.makedirs("images")

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    captured = False

    while True:
        success, frame = cap.read()
        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame, hand, mp_hands.HAND_CONNECTIONS
                )

                lm = hand.landmark

                # ✊ Fist detection (all fingers closed)
                fingers = []
                tips = [8, 12, 16, 20]
                for tip in tips:
                    fingers.append(lm[tip].y > lm[tip - 2].y)

                if all(fingers) and not captured:
                    cv2.imwrite("images/captured.jpg", frame)
                    print("📸 Photo Captured!")
                    captured = True
                    time.sleep(1)
                    cap.release()
                    cv2.destroyAllWindows()
                    return

        cv2.imshow("Gesture Camera (Make Fist to Capture)", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()