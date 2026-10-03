# 👁️ Computer Vision & Image Processing

Practical real-time computer vision applications utilizing **OpenCV (`cv2`)** and **NumPy** for live video analysis, image filtering, and hand gesture recognition.

---

## 📁 Modules

### 1. `hand_finger_counter.py`
Real-time hand contour and finger feature extraction from a webcam feed.
- **Techniques Used:**
  - Grayscale conversion and Gaussian noise reduction.
  - Binary inverse thresholding.
  - Contour finding (`cv2.findContours`).
  - Convex Hull calculation (`cv2.convexHull`) for gesture and finger point estimation.
- **Run:**
  ```bash
  python hand_finger_counter.py
  ```

---

### 2. `webcam_blur_filter.py`
Real-time spatial filtering and smoothing using 2D Gaussian kernels.
- **Techniques Used:**
  - Video stream polling (`cv2.VideoCapture`).
  - Gaussian convolution smoothing (`cv2.GaussianBlur`).
  - Real-time side-by-side stream comparison.
- **Run:**
  ```bash
  python webcam_blur_filter.py
  ```

---

## 🛠️ Prerequisites

```bash
pip install opencv-python numpy
```
*Note: A functional webcam is required to run live video capture.*
