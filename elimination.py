from transform import *

base = [[0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 2, 1], [0, 0, 1, 1, 2, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 2, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 2, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]]

matches = match_matrix([[0,0,0]], base)

for match in matches:
    print(match)