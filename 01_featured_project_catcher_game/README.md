# 🎮 Falling Items Catcher Game (OpenCV 2D Arcade)

An interactive real-time 2D arcade game built entirely using **OpenCV (`cv2`)** and **NumPy**, featuring dynamic difficulty scaling, sound effects, item collision mechanics, and state management.

---

## 🌟 Features

- **Real-Time Graphics & Rendering:** Built on OpenCV's graphic primitives and matrix operations (`cv2.rectangle`, `cv2.circle`, `cv2.putText`, `cv2.resize`).
- **Dynamic Difficulty Curve:** Falling speed and spawn rates increase proportionally across stages as survival time increases (1x -> 2x -> 3x speed multiplier).
- **Collision Detection & Scoring Engine:** Pixel-level bounding box overlap calculations for accurate item collection and bomb collision.
- **Audio Feedback:** Background music playback and collision sound effects integrated using Python's `winsound`.
- **Power-Ups & Penalties:**
  - 🟢 **Green Points:** Standard score bonus (+1 Score).
  - 🟡 **Yellow Points:** Paddle expansion (+10px paddle width power-up).
  - 🟣 **Purple Points:** Paddle shrinkage (-25px paddle width penalty).
  - 🔴 **Red Bombs:** Instant Game Over upon collision.

---

## 🕹️ Controls

| Key | Action |
|:---:|:---|
| <kbd>A</kbd> | Move Paddle Left |
| <kbd>D</kbd> | Move Paddle Right |
| <kbd>R</kbd> | Restart Game (on Game Over or Victory) |
| <kbd>ESC</kbd> | Exit Game |

---

## ⚙️ How to Run

1. Ensure requirements are installed:
   ```bash
   pip install opencv-python numpy
   ```

2. Run the game from this directory:
   ```bash
   python main.py
   ```

---

## 📁 Directory Structure

```
01_featured_project_catcher_game/
├── README.md
├── main.py
└── assets/
    ├── images/
    │   ├── Background.png
    │   └── Background Reserve.png
    └── sounds/
        ├── bomb_sound.wav
        └── theme.wav
```
