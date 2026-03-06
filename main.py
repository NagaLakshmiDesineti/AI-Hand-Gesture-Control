import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize Camera
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img) # Find hands

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand) # Count fingers up
        
        # Simple Gesture Logic
        if fingers == [1, 1, 1, 1, 1]:
            cv2.putText(img, "ALL FINGERS UP", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        elif fingers == [0, 1, 0, 0, 0]:
            cv2.putText(img, "INDEX FINGER - LIGHT ON", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
