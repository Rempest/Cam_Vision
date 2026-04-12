import cv2
cam = cv2.VideoCapture(0)
#frames to find the difference
frame1, rem1 = cam.read()
frame2, rem2 = cam.read()
while cam.isOpen():
    #difference between the frames
    diff = cv2.absdiff(frame1, frame2)
    # Convert to gray
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Threshold (black and white image)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # Enlarge motion areas


