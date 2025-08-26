import cv2
cam = cv2.VideoCapture(1)
while True:
    rem, frame = cam.read()
    print("The camera reads 1 frame")
    if not rem:
        break
    color_cam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("The picture", color_cam)
    if cv2.waitKey(1) & 0xFF == ord("p"):
       break
cam.release()
cv2.destroyAllWindows()

