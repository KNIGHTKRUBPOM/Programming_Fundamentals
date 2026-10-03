"""
Bomb Proximity Distance Field Grid
==================================
Generates an N x N matrix containing bomb placements ('X') and computes Chebyshev
distance proximity fields around each bomb. Closer cells show lower distances,
simulating proximity / heat maps in 2D space.

Topics: 2D Arrays, Distance Metrics (Chebyshev Distance), Grid Modeling.
"""

from typing import List, Tuple


def create_grid(size: int) -> List[List[object]]:
    """Initialize empty N x N grid with zeros."""
    return [[0] * size for _ in range(size)]


def add_bombs_and_calculate_distances(
    grid: List[List[object]], bombs: List[Tuple[int, int]], size: int
):
    """Place bombs and compute Chebyshev distance fields across all cells."""
    for r, c in bombs:
        grid[r][c] = "X"
        for size_r in range(size):
            for size_c in range(size):
                dist_r = abs(r - size_r)
                dist_c = abs(c - size_c)
                dist = max(dist_r, dist_c)  # Chebyshev metric

                current_val = grid[size_r][size_c]
                if dist > 0:
                    if current_val == 0:
                        grid[size_r][size_c] = dist
                    elif isinstance(current_val, int) and current_val > dist:
                        grid[size_r][size_c] = dist


def print_grid(grid: List[List[object]]):
    """Render formatted grid output."""
    for row in grid:
        line = []
        for cell in row:
            if isinstance(cell, int) and cell > 0:
                line.append(f"{cell:2d}")
            elif cell == "X":
                line.append(" X")
            else:
                line.append(" .")
        print(" ".join(line))


def run_demo():
    """Run demonstration with preset bomb coordinates."""
    size = 10
    grid = create_grid(size)
    bombs = [(2, 2), (7, 7)]
    add_bombs_and_calculate_distances(grid, bombs, size)
    print("=== Demo 10x10 Distance Field with 2 Bombs ===")
    print_grid(grid)


def main():
    """Interactive CLI execution."""
    size = 10
    grid = create_grid(size)

    try:
        user_input = input("Enter number of bombs (1-5) or press Enter for Demo: ").strip()
        if not user_input:
            run_demo()
            return

        num_bombs = int(user_input)
        if not (1 <= num_bombs <= 5):
            print("Number of bombs must be between 1 and 5.")
            return

        bombs = []
        for i in range(num_bombs):
            r, c = map(
                int,
                input(f"Enter bomb #{i+1} position (Row 1-{size}, Col 1-{size}): ").split(),
            )
            if not (1 <= r <= size and 1 <= c <= size):
                print("Coordinates out of range.")
                return
            bombs.append((r - 1, c - 1))

        add_bombs_and_calculate_distances(grid, bombs, size)
        print("\nGenerated Distance Grid:")
        print_grid(grid)

    except (ValueError, EOFError):
        run_demo()


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv or not sys.stdin.isatty():
        run_demo()
    else:
        main()

