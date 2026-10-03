"""
Lab 8 - Exercise 2: Grid Word Search & Matrix Scanning
======================================================
Scans a 2D character matrix to locate character coordinates and verify
whether a target word's letters exist within the matrix.
"""

from typing import Dict, List, Tuple


def find_letter_coordinates(
    grid: List[str], target_word: str
) -> Dict[str, List[Tuple[int, int]]]:
    """Find all (row, col) coordinates for each character of target_word in the grid."""
    coords: Dict[str, List[Tuple[int, int]]] = {char: [] for char in target_word}

    for r_idx, row in enumerate(grid):
        for c_idx, char in enumerate(row):
            if char in coords:
                coords[char].append((r_idx, c_idx))

    return coords


def contains_all_characters(grid: List[str], target_word: str) -> bool:
    """Return True if all distinct characters of target_word are present in grid."""
    grid_chars = set("".join(grid))
    return set(target_word).issubset(grid_chars)


if __name__ == "__main__":
    matrix = [
        "*****",
        "*MM**",
        "*KIK*",
        "*IT**",
        "**L**",
    ]

    target = "KMITL"
    found = contains_all_characters(matrix, target)
    letter_positions = find_letter_coordinates(matrix, target)

    print(f"Target: '{target}' found in matrix: {found}")
    for letter, positions in letter_positions.items():
        print(f"  Letter '{letter}' at coordinates: {positions}")

    assert found is True
    assert (2, 1) in letter_positions["K"]
    assert (3, 2) in letter_positions["T"]
    assert (4, 2) in letter_positions["L"]

    assert contains_all_characters(matrix, "PYTHON") is False
    print("Grid Word Search: All tests passed!")
