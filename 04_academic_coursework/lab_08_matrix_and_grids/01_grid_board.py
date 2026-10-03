"""
Lab 8 - Exercise 1: 6x6 Grid Board Marker (XO Game)
===================================================
A 6x6 numerical matrix board where players place markers on numbered cells (1 to 36).
Demonstrates 1D to 2D index flattening and grid rendering.
"""

from typing import List


def create_board() -> List[str]:
    """Create empty 6x6 grid represented as 36-element list."""
    return ["."] * 36


def format_board(board: List[str]) -> str:
    """Format the 36-element board into 6 rows of 6 items."""
    rows = []
    for i in range(0, 36, 6):
        rows.append(" ".join(f"{item:>2}" for item in board[i : i + 6]))
    return "\n".join(rows)


def place_marker(board: List[str], cell_number: int, marker: str = "X") -> bool:
    """Place marker in cell 1-36. Returns True if successfully marked."""
    if not (1 <= cell_number <= 36):
        return False
    index = cell_number - 1
    board[index] = marker
    return True


if __name__ == "__main__":
    board = create_board()
    assert place_marker(board, 1, "X") is True
    assert place_marker(board, 36, "O") is True
    assert place_marker(board, 0) is False
    assert place_marker(board, 37) is False

    print("Sample 6x6 Board State:")
    print(format_board(board))
    print("Grid Board Marker: All tests passed!")
