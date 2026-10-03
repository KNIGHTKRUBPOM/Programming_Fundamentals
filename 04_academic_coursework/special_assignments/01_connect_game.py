"""
Connect-3 Console Game
======================
An interactive 6x6 connect-style game played against a computer opponent.
Players drop chips into columns, gravity pulls them down to the lowest
available slot, and the first to connect 3 tokens horizontally, vertically,
or diagonally wins.

Controls / Input:
- Enter column number (1 - 6)
"""

import random
from typing import List


def create_board() -> List[List[str]]:
    """Initialize empty 6x6 board."""
    return [["o|" for _ in range(6)] for _ in range(6)]


def display_board(board: List[List[str]]):
    """Print board state with gravity orientation (row 0 at bottom)."""
    print("\n  1   2   3   4   5   6")
    print("-------------------------")
    for row in reversed(board):
        print(" " + "".join(row))
    print("-------------------------\n")


def drop_piece(board: List[List[str]], col: int, token: str) -> bool:
    """Drop token into the lowest empty slot in the specified column."""
    if not (0 <= col < 6):
        return False
    for row in range(6):
        if board[row][col] == "o|":
            board[row][col] = token
            return True
    return False  # Column is full


def bot_move(board: List[List[str]]) -> bool:
    """Simulate bot move by randomly picking an available column."""
    available_cols = [c for c in range(6) if board[5][c] == "o|"]
    if not available_cols:
        return False
    col = random.choice(available_cols)
    return drop_piece(board, col, "w|")


def check_win(board: List[List[str]], player: str) -> bool:
    """Check if the given player token has 3 in a row in any direction."""
    # Horizontal
    for r in range(6):
        for c in range(4):
            if board[r][c] == board[r][c + 1] == board[r][c + 2] == player:
                return True

    # Vertical
    for c in range(6):
        for r in range(4):
            if board[r][c] == board[r + 1][c] == board[r + 2][c] == player:
                return True

    # Diagonal Up-Right
    for r in range(4):
        for c in range(4):
            if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == player:
                return True

    # Diagonal Down-Right
    for r in range(2, 6):
        for c in range(4):
            if board[r][c] == board[r - 1][c + 1] == board[r - 2][c + 2] == player:
                return True

    return False


def play_game():
    """Start interactive game session."""
    board = create_board()
    print("=== Welcome to Connect-3 Game ===")
    display_board(board)

    while True:
        try:
            choice = input("Enter column (1-6) or 'q' to quit: ").strip()
            if choice.lower() == "q":
                print("Game exited.")
                break

            col_idx = int(choice) - 1
            if not (0 <= col_idx < 6):
                print("Invalid column. Please enter a number between 1 and 6.")
                continue

            if not drop_piece(board, col_idx, "x|"):
                print("Column is full! Choose another column.")
                continue

            if check_win(board, "x|"):
                display_board(board)
                print("🎉 YOU WIN! Congratulations!")
                break

            # Computer move
            if bot_move(board):
                if check_win(board, "w|"):
                    display_board(board)
                    print("🤖 COMPUTER WINS! Better luck next time!")
                    break

            display_board(board)

        except (ValueError, EOFError):
            print("Session ended.")
            break


def run_unit_tests():
    """Verify core game logic."""
    b = create_board()
    assert drop_piece(b, 0, "x|") is True
    assert drop_piece(b, 0, "x|") is True
    assert drop_piece(b, 0, "x|") is True
    assert check_win(b, "x|") is True
    assert check_win(b, "w|") is False
    print("Connect-3 Game: All tests passed!")


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv or not sys.stdin.isatty():
        run_unit_tests()
    else:
        play_game()

