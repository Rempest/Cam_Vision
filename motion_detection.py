import cv2  # Import OpenCV library for computer vision (video, images, camera processing)

# Create a video capture object
# 0 means the default webcam (built-in camera)
cam = cv2.VideoCapture(0)

# Read the first two frames from the camera
# ret = True/False (whether frame was successfully read)
# frame1 and frame2 are image frames (NumPy arrays)
ret, frame1 = cam.read()
ret, frame2 = cam.read()

# Main loop: runs while the camera is successfully opened
while cam.isOpened():

    # =========================
    # 1. FRAME DIFFERENCE
    # =========================
    # Calculate absolute difference between two consecutive frames
    # This highlights pixels that changed → motion detection basis
    diff = cv2.absdiff(frame1, frame2)

    # =========================
    # 2. CONVERT TO GRAYSCALE
    # =========================
    # Convert image to grayscale (removes color information)
    # This simplifies processing and reduces computation cost
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # =========================
    # 3. GAUSSIAN BLUR (NOISE REDUCTION)
    # =========================
    # Apply Gaussian blur to remove small noise and camera shaking
    # (5,5) is kernel size; larger = more smoothing
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # =========================
    # 4. THRESHOLDING (BINARY IMAGE)
    # =========================
    # Convert image into black and white format:
    # pixels > 20 → white (255)
    # pixels <= 20 → black (0)
    # This isolates strong motion areas
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # =========================
    # 5. DILATION (EXPANDING MOTION AREAS)
    # =========================
    # Increase white regions to fill gaps and connect broken motion parts
    # Helps make detected movement regions more solid
    dilated = cv2.dilate(thresh, None, iterations=3)

    # =========================
    # 6. FIND CONTOURS (MOTION REGIONS)
    # =========================
    # Detect continuous boundaries (contours) of white areas
    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_TREE,          # retrieves all contours and hierarchy
        cv2.CHAIN_APPROX_SIMPLE # compresses contour points to save memory
    )

    # Loop through all detected contours
    for contour in contours:

        # =========================
        # 7. FILTER SMALL MOVEMENTS (NOISE REMOVAL)
        # =========================
        # Ignore small detected areas (likely noise or tiny movements)
        # Only keep meaningful motion
        if cv2.contourArea(contour) < 1000:
            continue

        # =========================
        # 8. DRAW BOUNDING BOX
        # =========================
        # Get rectangle coordinates around detected motion
        x, y, w, h = cv2.boundingRect(contour)

        # Draw green rectangle around moving object
        cv2.rectangle(
            frame1,
            (x, y),         # top-left corner
            (x + w, y + h), # bottom-right corner
            (0, 255, 0),    # green color in BGR format
            2               # thickness of rectangle border
        )

        # =========================
        # 9. DISPLAY TEXT LABEL
        # =========================
        # Add text label to show that motion was detected
        cv2.putText(
            frame1,
            "Movement detected",     # text to display
            (10, 20),                # position on screen
            cv2.FONT_HERSHEY_SIMPLEX,# font type
            1,                       # font scale
            (0, 0, 255),             # red color (BGR)
            2                        # thickness
        )

    # =========================
    # 10. SHOW OUTPUT WINDOW
    # =========================
    # Display the processed video frame with rectangles and text
    cv2.imshow("Motion Detection", frame1)

    # =========================
    # 11. FRAME UPDATE
    # =========================
    # Shift frames:
    # previous frame becomes frame1
    # new frame is captured into frame2
    frame1 = frame2
    ret, frame2 = cam.read()

    # =========================
    # 12. EXIT CONDITION
    # =========================
    # If ESC key (ASCII 27) is pressed → exit loop
    if cv2.waitKey(40) == 27:
        break

# =========================
# CLEANUP (RELEASE RESOURCES)
# =========================
# Release camera resource
cam.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
