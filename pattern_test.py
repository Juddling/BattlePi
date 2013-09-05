from transform import *

test_pattern = [
    [1],
    [2],
    [2],
    [1]
]

# m = Matrix(test_pattern)
# all = m.all_transformations()
#
# for pattern in all:

row_results = match_matrix(test_pattern, Ships.Hovercraft)

for r in matches_to_relative_position(row_results):
    print(r)