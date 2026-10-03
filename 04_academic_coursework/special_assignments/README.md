# ⭐ Special Programming Assignments

Advanced coursework projects emphasizing 2D grid representations, coordinate geometry, matrix manipulation, and game state validation.

---

## 📌 Projects

### 1. `01_connect_game.py`
A 6x6 Connect-3 board game playable against a computer bot in the console terminal.
- Includes gravity simulation where pieces drop to the lowest vacant slot in a column.
- Dynamic winning checks across rows, columns, and positive/negative diagonals.
- Safe matrix boundary validations.

### 2. `02_bomb_proximity_grid.py`
A 2D spatial distance field simulation.
- Places bombs onto an $N \times N$ matrix.
- Calculates Chebyshev proximity distances ($\max(|x_1 - x_2|, |y_1 - y_2|)$) to visualize continuous distance gradients around multiple hazard points.
- Features interactive input and automated demo mode.
