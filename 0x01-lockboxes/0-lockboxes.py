#!/usr/bin/python3
"""Module for task 0
"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened
    Returns 
        boolean: True if all boxes can be unlocked, by using all the keys
        available 
    """
    # Initialize set of visited boxes, starting with the first box
    visited = {0}
    # Initialize queue with the first box
    queue = [boxes[0]]
    # While there are boxes in the queue
    # print("boxes type is {}".format(type(boxes)))
    while queue:
        # Take the first box from the queue
        box = queue.pop(0)
        # Iterate through the keys in the box
        for key in box:
            # If the key corresponds to a locked box that has not been
            if key not in visited and key < len(boxes):
                # Mark the box as visited
                visited.add(key)
                # Add the box to the queue to explore its keys
                queue.append(boxes[key])
    # Return whether all boxes have been visited
    return len(visited) == len(boxes)
