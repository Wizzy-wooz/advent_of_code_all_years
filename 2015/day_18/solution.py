from pathlib import Path


def simulate(lines: list[str], stuck_corners: bool = False, steps: int = 100) -> int:
    grid = [list(row.strip()) for row in lines if row.strip()]
    height, width = len(grid), len(grid[0])
    corners = {(0, 0), (0, width - 1), (height - 1, 0), (height - 1, width - 1)}

    def force_corners(board):
        for r, c in corners:
            board[r][c] = '#'

    if stuck_corners:
        force_corners(grid)
    for _ in range(steps):
        next_grid = [['.' for _ in range(width)] for _ in range(height)]
        for r in range(height):
            for c in range(width):
                neighbors = sum(0 <= r + dr < height and 0 <= c + dc < width
                                and grid[r + dr][c + dc] == '#'
                                for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                                if dr or dc)
                next_grid[r][c] = '#' if (grid[r][c] == '#' and neighbors in (2, 3)
                                           or grid[r][c] == '.' and neighbors == 3) else '.'
        grid = next_grid
        if stuck_corners:
            force_corners(grid)
    return sum(row.count('#') for row in grid)


def solve(lines: list[str]) -> tuple[int, int]:
    return simulate(lines), simulate(lines, stuck_corners=True)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
