import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    # convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # detect red color (use red object as pointer)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 800:
            x,y,w,h = cv2.boundingRect(cnt)

            cx = x + w//2
            cy = y + h//2

            # draw pointer
            cv2.circle(frame, (cx, cy), 10, (0,255,0), -1)
            cv2.putText(frame, f"Pointer: {cx},{cy}", (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)

    cv2.imshow("Virtual Mouse Demo", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()