from transform import *

test_pattern = [
    [2,2,2]
]

m = Matrix(test_pattern)

row_results = match_matrix(test_pattern, [
    # [1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [1, 2, 2, 1, 2, 1],
    [2, 2, 1, 1, 2, 1],
    [2, 2, 2, 1, 2, 1],
    [1, 1, 1, 2, 2, 2],
    [2, 2, 2, 2, 1, 1],
])

for r in matches_to_relative_position(row_results):
    print(r)