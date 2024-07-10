#!/usr/bin/python3
"""Module For Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): the grid representing the island

    Returns:
        int: the perimeter of the island
    """
    # Determine the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the perimeter variable to 0
    perimeter = 0

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the bottom edge
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right edge
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    # Return the total perimeter
    return perimeter
