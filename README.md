# Motion Detection using OpenCV 🎥

This project demonstrates a basic motion detection system using the popular Python computer vision library — OpenCV.  
The program works by detecting differences between consecutive video frames and identifying areas of movement in real time.

---

## 🧠 Pipeline

Frame difference → Grayscale conversion → Noise reduction (Gaussian blur) → Thresholding (binary image) → Morphological dilation → Contour detection → Motion filtering → Result display

---

## 🚀 Features

- Real-time webcam video processing
- Motion detection using frame differencing
- Noise reduction with Gaussian blur
- Contour detection for moving objects
- Bounding boxes around detected motion
- Lightweight and fast algorithm

---

## 🧠 How It Works

The system detects motion using the following steps:

1. Capture two consecutive frames from the webcam  
2. Compute the absolute difference between frames  
3. Convert the result to grayscale  
4. Apply Gaussian blur to reduce noise  
5. Apply thresholding to create a binary image  
6. Dilate the image to strengthen motion regions  
7. Detect contours of moving objects  
8. Filter out small noise-based movements  
9. Draw bounding boxes around detected motion  

---

## 📦 Requirements

Install OpenCV:

```bash
pip install opencv-python
