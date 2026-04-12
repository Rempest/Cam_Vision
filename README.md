This project demonstrates a basic motion detection system using the popular Python computer vision library — OpenCV.

The program works by detecting differences between video frames and identifying areas of movement.

### Pipeline:
Frame difference → Grayscale conversion → Noise reduction (blur) → Thresholding (binary image) → Morphological dilation → Contour detection → Motion filtering → Result display

---

## How it works:

1. The camera captures two consecutive frames (frame1 and frame2).
2. While the camera is running, the program calculates the difference between these two frames.
3. The difference is converted to a grayscale image.
4. A Gaussian blur is applied to reduce noise and improve detection accuracy.
5. Thresholding converts the image into a binary (black and white) format.
6. Dilation is applied to enlarge detected motion areas.
7. Contours are extracted to find the coordinates of moving objects.
8. Small movements (area < 1000) are ignored as noise.
9. Significant movements are highlighted with bounding boxes and displayed on the screen.
