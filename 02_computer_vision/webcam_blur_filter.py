"""
Real-Time Webcam Gaussian Blur Filter
======================================
Captures live frames from a webcam, applies a 2D Gaussian convolution kernel,
and provides side-by-side or live filtered visualization.

Key Concepts:
- Video stream polling (`cv2.VideoCapture`)
- Gaussian spatial smoothing (`cv2.GaussianBlur`)
- Frame display and interactive keyboard input
"""

import sys
import cv2


def run_webcam_filter(camera_index: int = 0, kernel_size: int = 21):
    """Capture live video feed and display original vs blurred output."""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Could not access camera with index {camera_index}.")
        sys.exit(1)

    print("Webcam Blur Filter started. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Warning: Failed to receive frame from camera.")
            break

        # Apply 2D Gaussian Blur filter
        blurred_frame = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

        # Overlay text annotation
        cv2.putText(
            blurred_frame,
            f"Gaussian Blur (Kernel: {kernel_size}x{kernel_size})",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2,
            cv2.LINE_AA,
        )

        cv2.imshow("Webcam Filter - Original", frame)
        cv2.imshow("Webcam Filter - Blurred", blurred_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_webcam_filter()
