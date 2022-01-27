import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()