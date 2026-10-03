"""
Real-Time Hand Contour & Finger Detection
==========================================
Uses OpenCV and image processing techniques to detect hand contours,
compute the convex hull, and estimate finger counts from a live webcam feed.

Key Concepts:
- Grayscale conversion and Gaussian Blur filtering
- Binary inverse thresholding (Otsu / adaptive / fixed)
- Contour extraction (`cv2.findContours`)
- Convex Hull computation (`cv2.convexHull`)
"""

import sys
import cv2
import numpy as np


def run_finger_counter(camera_index: int = 0):
    """Run real-time finger detection loop from connected webcam."""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index}.")
        sys.exit(1)

    print("Finger Counter started. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Warning: Failed to grab frame.")
            break

        # Flip horizontally for natural mirror interaction
        frame = cv2.flip(frame, 1)

        # Preprocessing: Grayscale -> Gaussian Blur -> Binary Inversion
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        detected_count = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1200:  # Filter out small noise
                # Compute Convex Hull around hand/fingers
                hull = cv2.convexHull(contour)
                cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)
                detected_count += 1

        # Display HUD information
        cv2.putText(
            frame,
            f"Detected Features / Fingers: {detected_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        cv2.putText(
            frame,
            "Press 'q' to Exit",
            (20, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (200, 200, 200),
            1,
            cv2.LINE_AA,
        )

        cv2.imshow("Hand & Finger Detection - OpenCV", frame)
        cv2.imshow("Threshold Mask", thresh)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_finger_counter()
