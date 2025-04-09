import cv2
import mediapipe as mp
import pyautogui as pyagi

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)

pyagi.PAUSE = 0
screen_width, screen_height = pyagi.size()
mouse_x, mouse_y = pyagi.position()

fingertips = [8, 12, 16, 20]
pip_joints = [6, 10, 14, 18]

dragging = False

while True:
    sucess, frame = cap.read()
    if not sucess:
        continue

    rbg_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rbg_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[8]
            x, y = int(index_tip.x * frame_width), int(index_tip.y * frame_height)

            # if distance between thumb and index finger is less then 0.03 cm, left click
            thumb_tip = hand_landmarks.landmark[4]
            distance = ((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)**0.5
            if distance < 0.03:
                pyagi.click()

            # if distance between middle finger and thumb is less then 0.03 cm, right click
            middle_tip = hand_landmarks.landmark[12]
            distance = ((middle_tip.x - thumb_tip.x)**2 + (middle_tip.y - thumb_tip.y)**2)**0.5
            if distance < 0.03:
                pyagi.rightClick()

            # if distance between middle and index finger is less then 0.03 cm, use the mouse drag
            curr_x, curr_y = mouse_x, mouse_y
            distance = ((middle_tip.x - index_tip.x)**2 + (middle_tip.y - index_tip.y)**2)**0.5
            if distance<0.03:
                pyagi.mouseDown()
                pyagi.moveTo(x * screen_width // frame_width, y * screen_height // frame_height)
                dragging = True
            else:
                pyagi.mouseUp()
                dragging = False
    
    cv2.imshow("Hand mouse", frame)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()