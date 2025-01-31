#!/usr/bin/python3
"""
Module for calculating the perimeter of an island represented in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.

    Args:
        grid (List[List[int]]): A 2D list where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.

    Raises:
        ValueError: If the grid is not rectangular.
    """
    if not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Grid is not rectangular")

    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:  # If the cell is land
                perimeter += 4  # Add 4 for the cell's edges

                if row > 0 and grid[row - 1][col] == 1:  # Check top neighbor
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check left neighbor
                    perimeter -= 2

    return perimeter
