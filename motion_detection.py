import cv2
cam = cv2.VideoCapture(0)
#frames to find the difference
ret, frame1 = cam.read()
ret, frame2 = cam.read()
while cam.isOpened():
    #difference between the frames
    diff = cv2.absdiff(frame1, frame2)
    # Convert to gray
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Threshold (black and white image)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # Enlarge motion areas
    dilated = cv2.dilate(thresh, None, iterations=3)
    # find the motion
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
    # ignore the little motion
      if cv2.contourArea(contour) < 1000:
            continue
      #show the window
      x, y, w, h = cv2.boundingRect(contour)
      cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
      # red text
      cv2.putText(frame1, "Movement detected", (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Motion Detection", frame1)

       
    frame1 = frame2
    ret, frame2 = cam.read()

      #press "ESP" to exit
    if cv2.waitKey(40) == 27:
        break

cam.release()
cv2.destroyAllWindows()

        
    


