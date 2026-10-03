"""
OpenCV Falling Items Catcher Game
==================================
An interactive 2D arcade game built using OpenCV and NumPy.
Players move a catcher paddle horizontally to collect score points and power-ups
while avoiding falling bombs with increasing game difficulty.

Controls:
- [A]: Move Left
- [D]: Move Right
- [R]: Restart Game (when Game Over or Won)
- [ESC]: Exit
"""

import os
from pathlib import Path
import random
import sys
import time

import cv2
import numpy as np

# Play sound on Windows if winsound is available
try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False

# Paths & Assets
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
BG_IMAGE_PATH = ASSETS_DIR / "images" / "Background.png"
THEME_MUSIC_PATH = str(ASSETS_DIR / "sounds" / "theme.wav")
BOMB_SOUND_PATH = str(ASSETS_DIR / "sounds" / "bomb_sound.wav")

# Game Configuration
WIDTH, HEIGHT = 1920, 1080
FPS = 200
GAME_DURATION = 300  # 5 minutes in seconds

# Game State Variables
player_pos = WIDTH // 2
player_width = 60
player_height = 10
bombs = []
green_points = []
yellow_points = []
purple_points = []
score = 0
start_time = time.time()
game_over = False
win = False


def play_music():
    """Start background music loop if supported."""
    if HAS_WINSOUND and os.path.exists(THEME_MUSIC_PATH):
        try:
            winsound.PlaySound(THEME_MUSIC_PATH, winsound.SND_ASYNC | winsound.SND_LOOP)
        except Exception:
            pass


def play_sound_effect(sound_path: str):
    """Play a one-shot sound effect."""
    if HAS_WINSOUND and os.path.exists(sound_path):
        try:
            winsound.PlaySound(sound_path, winsound.SND_FILENAME)
        except Exception:
            pass


def stop_all_sounds():
    """Stop all sounds on exit or game transition."""
    if HAS_WINSOUND:
        try:
            winsound.PlaySound(None, winsound.SND_PURGE)
        except Exception:
            pass


def is_overlapping(x: int, y: int, width: int, height: int, points: list) -> bool:
    """Check whether a bounding box overlaps with any existing falling point."""
    for point in points:
        if (
            point[0] < x + width
            and point[0] + 30 > x
            and point[1] < y + height
            and point[1] + 30 > y
        ):
            return True
    return False


def create_bomb():
    """Spawn a bomb at a non-overlapping horizontal coordinate."""
    while True:
        x_pos = random.randint(0, WIDTH - 100)
        all_items = bombs + green_points + yellow_points + purple_points
        if not is_overlapping(x_pos, 0, 30, 30, all_items):
            bombs.append([x_pos, 0])
            break


def create_green_point():
    """Spawn a regular green score item (+1 score)."""
    while True:
        x_pos = random.randint(0, WIDTH - 100)
        all_items = bombs + green_points + yellow_points + purple_points
        if not is_overlapping(x_pos, 0, 30, 30, all_items):
            green_points.append([x_pos, 0])
            break


def create_yellow_point():
    """Spawn a yellow power-up item (+10 paddle width)."""
    while True:
        x_pos = random.randint(0, WIDTH - 100)
        all_items = bombs + green_points + yellow_points + purple_points
        if not is_overlapping(x_pos, 0, 30, 30, all_items):
            yellow_points.append([x_pos, 0])
            break


def create_purple_point():
    """Spawn a purple penalty item (-25 paddle width)."""
    while True:
        x_pos = random.randint(0, WIDTH - 100)
        all_items = bombs + green_points + yellow_points + purple_points
        if not is_overlapping(x_pos, 0, 30, 30, all_items):
            purple_points.append([x_pos, 0])
            break


# Load and prepare background image
if BG_IMAGE_PATH.exists():
    background_draw_game = cv2.imread(str(BG_IMAGE_PATH))
else:
    # Fallback to dark background if asset not found
    background_draw_game = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)


def draw_game() -> np.ndarray:
    """Render the game board, player paddle, items, and UI overlay."""
    background_resized = cv2.resize(background_draw_game, (WIDTH, HEIGHT))
    frame = background_resized.copy()

    # Draw player paddle
    cv2.rectangle(
        frame,
        (player_pos, HEIGHT - player_height),
        (player_pos + player_width, HEIGHT),
        (255, 255, 255),
        -1,
    )

    # Draw falling bombs (Red)
    for bomb in bombs:
        cv2.circle(frame, (bomb[0] + 15, bomb[1]), 15, (0, 0, 255), -1)

    # Draw regular score points (Green)
    for point in green_points:
        cv2.circle(frame, (point[0] + 15, point[1]), 15, (0, 255, 0), -1)

    # Draw size expand points (Yellow)
    for yellow_point in yellow_points:
        cv2.circle(frame, (yellow_point[0] + 15, yellow_point[1]), 15, (0, 255, 255), -1)

    # Draw size shrink points (Purple)
    for purple_point in purple_points:
        cv2.circle(frame, (purple_point[0] + 15, purple_point[1]), 15, (255, 0, 255), -1)

    # Render score HUD
    cv2.putText(frame, f"Score : {score}", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 15)
    cv2.putText(frame, f"Score : {score}", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    # Render remaining time HUD
    remaining_time = max(0, int(GAME_DURATION - (time.time() - start_time)))
    cv2.putText(frame, f"Time : {remaining_time}", (WIDTH - 400, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 15)
    cv2.putText(frame, f"Time : {remaining_time}", (WIDTH - 400, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    return frame


def check_collision() -> bool:
    """Check if player paddle collides with any bomb."""
    for bomb in bombs:
        if (
            bomb[1] >= HEIGHT - player_height
            and player_pos < bomb[0] + 30
            and player_pos + player_width > bomb[0]
        ):
            play_sound_effect(BOMB_SOUND_PATH)
            return True
    return False


def check_point_collection():
    """Detect item collection and update score or paddle width."""
    global score, player_width

    # Green point: +1 score
    for point in green_points[:]:
        if (
            point[1] >= HEIGHT - player_height
            and player_pos < point[0] + 30
            and player_pos + player_width > point[0]
        ):
            score += 1
            green_points.remove(point)

    # Yellow point: expand paddle size (+10 px)
    for yellow_point in yellow_points[:]:
        if (
            yellow_point[1] >= HEIGHT - player_height
            and player_pos < yellow_point[0] + 30
            and player_pos + player_width > yellow_point[0]
        ):
            player_width += 10
            yellow_points.remove(yellow_point)

    # Purple point: shrink paddle size (-25 px, min width 10)
    for purple_point in purple_points[:]:
        if (
            purple_point[1] >= HEIGHT - player_height
            and player_pos < purple_point[0] + 30
            and player_pos + player_width > purple_point[0]
        ):
            player_width = max(10, player_width - 25)
            purple_points.remove(purple_point)


def create_points_in_intervals():
    """Spawn items and scale falling speeds as game time progresses."""
    global bombs, green_points, yellow_points, purple_points
    elapsed_time = time.time() - start_time
    speed_multiplier = 1

    if elapsed_time < 60:
        speed_multiplier = 1
        if random.randint(1, 50) == 1:
            create_green_point()
            create_bomb()
    elif 60 <= elapsed_time < 66:
        create_yellow_point()
        create_bomb()
    elif elapsed_time < 120:
        speed_multiplier = 1
        if random.randint(1, 42) == 1:
            create_green_point()
            if random.randint(1, 10) == 1:
                create_yellow_point()
            create_bomb()
    elif 120 <= elapsed_time < 126:
        create_purple_point()
        create_bomb()
    elif elapsed_time < 180:
        speed_multiplier = 1
        if random.randint(1, 30) == 1:
            create_green_point()
            if random.randint(1, 10) == 1:
                create_yellow_point()
            if random.randint(1, 10) == 1:
                create_purple_point()
            create_bomb()
    elif elapsed_time < 240:
        speed_multiplier = 2
        if random.randint(1, 30) == 1:
            create_green_point()
            if random.randint(1, 10) == 1:
                create_yellow_point()
            if random.randint(1, 10) == 1:
                create_purple_point()
            create_bomb()
    elif elapsed_time < 295:
        speed_multiplier = 3
        if random.randint(1, 10) == 1:
            create_green_point()
            if random.randint(1, 10) == 1:
                create_yellow_point()
            if random.randint(1, 10) == 1:
                create_purple_point()
            create_bomb()
    else:
        speed_multiplier = 3

    # Update positions by multiplier
    for bomb in bombs:
        bomb[1] += 2 * speed_multiplier
    for point in green_points:
        point[1] += 2 * speed_multiplier
    for yellow_point in yellow_points:
        yellow_point[1] += 2 * speed_multiplier
    for purple_point in purple_points:
        purple_point[1] += 2 * speed_multiplier

    # Remove items that have fallen off-screen
    bombs = [b for b in bombs if b[1] < HEIGHT]
    green_points = [p for p in green_points if p[1] < HEIGHT]
    yellow_points = [yp for yp in yellow_points if yp[1] < HEIGHT]
    purple_points = [pp for pp in purple_points if pp[1] < HEIGHT]


def show_end_screen(message: str) -> np.ndarray:
    """Render the game end / victory summary screen."""
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    cv2.putText(frame, message, (WIDTH // 2 - 140, HEIGHT // 2 - 40), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 255, 255), 3)
    cv2.putText(frame, f"Final Score : {score}", (WIDTH // 2 - 140, HEIGHT // 2 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)
    cv2.putText(frame, "Press 'R' to Play Again", (WIDTH // 2 - 160, HEIGHT // 2 + 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)
    cv2.putText(frame, "Press 'ESC' to Exit", (WIDTH // 2 - 140, HEIGHT // 2 + 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)
    return frame


def reset_game():
    """Reset all state variables for a new round."""
    global player_pos, player_width, bombs, green_points, yellow_points, purple_points, score, start_time, game_over, win
    player_pos = WIDTH // 2
    player_width = 60
    bombs = []
    green_points = []
    yellow_points = []
    purple_points = []
    score = 0
    start_time = time.time()
    game_over = False
    win = False
    play_music()


def main():
    """Main game execution loop."""
    global player_pos, game_over, win

    window_name = "Catcher Game - OpenCV"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1280, 720)

    play_music()

    while True:
        elapsed_time = time.time() - start_time

        # Check win condition (survived full game duration)
        if elapsed_time >= GAME_DURATION and not win:
            win = True
            stop_all_sounds()
            end_frame = show_end_screen("You Win!")
            cv2.imshow(window_name, end_frame)
            key = cv2.waitKey(0) & 0xFF
            if key == ord("r"):
                reset_game()
                continue
            elif key == 27:
                break

        if not game_over:
            key = cv2.waitKey(int(1000 / FPS)) & 0xFF
            if (key == ord("a") or key == ord("A")) and player_pos > 0:
                player_pos -= 40
            if (key == ord("d") or key == ord("D")) and player_pos < WIDTH - player_width:
                player_pos += 40
            if key == 27:  # ESC key
                break

            create_points_in_intervals()

            if check_collision():
                game_over = True
                end_frame = show_end_screen("Game Over!")
                cv2.imshow(window_name, end_frame)
                key = cv2.waitKey(0) & 0xFF
                if key == ord("r"):
                    reset_game()
                    continue
                elif key == 27:
                    break

            check_point_collection()
            frame = draw_game()
            cv2.imshow(window_name, frame)

        else:
            end_frame = show_end_screen("Game Over!")
            cv2.imshow(window_name, end_frame)
            key = cv2.waitKey(0) & 0xFF
            if key == ord("r"):
                reset_game()
                continue
            elif key == 27:
                break

    stop_all_sounds()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
