#!/usr/bin/python3
"""
function def pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing Pascal triangle of n

    Args:
        n (integer): number of rows
Returns:
        list: integers representing Pascal's triangle.
    """
    # if n is less or 0 return an empty list
    if n <= 0:
        return []

    else:
        # Initialize a variable called triangle with a list containing 
        triangle = [[1]]

        for i in range(1, n):
           # On every generation of the loop, a brand new listing is created and
            # appended to the triangle variable. This listing begins off evolved with a
            # single detail, 1, which represents the primary detail of the
            # new row.
            triangle.append([1])

            # The feature then enters a nested loop that iterates over the
            # factors withinside the preceding row (the row with an index of i-1) and
            # calculates the price of every detail withinside the new row (the row
            # preceding row which are at once above and to the left and right
            # of the modern detail.

            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])

             # have been calculated, at which point a final 1 is appended to
            # the end of the row to complete it.

            triangle[i].append(1)
        return triangle

