"""
“Rocks” game with two piles of rocks, say ten in each. In each
turn, one player may take either one rock (from either pile) or two rocks
(one from each pile). Once the rocks are taken, they are removed from
play. The player that takes the last rock wins the game. You make the first
move. We encourage you to play this game using our interactive puzzle.
"""
import numpy as np


def TwoRock(n, m):
    n += 1
    m += 1
    table = np.zeros((n, m), dtype="int8")
    table[0, 0] = 0
    for i in range(1, n):
        table[i, 0] = 0 if table[i-1, 0] == 1 else 1
    for i in range(1, m):
        table[0, i] = 0 if table[0, i-1] == 1 else 1
    for i in range(1, n):
        for j in range(1, m):
            table[i, j] = 0 if table[i-1, j-1] == 1 and \
                table[i, j-1] == 1 and table[i-1, j] == 1 else 1
    return table

# player can move up to three rocks at a time from the piles


def ThreeRock(n, m):
    n += 1
    m += 1
    table = np.zeros((n, m), dtype="int8")
    table[0, 0] = 0
    for i in range(1, n):
        table[i, 0] = 1 if i % 4 else 0
    for i in range(1, m):
        table[0, i] = 1 if i % 4 else 0
    for i in range(1, n):
        for j in range(1, m):
            table[i, j] = 1 if (i+j) % 4 else 0
    return table


ThreeRock(10, 10)
