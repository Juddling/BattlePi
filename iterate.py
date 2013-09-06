__author__ = 'Judd'

import constants
from Attack import Attack
from game_logic import InitPlayerBoard, DeployFleet
from addition import add_jagged_list

enemy_debug = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

enemy_config1 = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 1],
    [1, 1, 2, 2, 2, 1],
    [1, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

enemy_config2 = [
    [2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1],
]

#average 79 down to 62.1
enemy_config3 = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

enemy_config4 = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
]

enemy_config5 = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 2],
    [1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1],
]

iterations = 1
csv = ""

# 1: 69.42 then 67.08 - after eliminating horizontal Ts

heat_map = InitPlayerBoard(0)

for i in range(iterations):
    # while True:
    #     config = InitPlayerBoard()
    #     try:
    #         DeployFleet(config, False)
    #     except RuntimeError:
    #         continue
    #
    #     break

    config = [[1, 5, 5, 5, 5, 5], [1, 5, 2, 2, 2, 5], [1, 5, 5, 5, 5, 5], [5, 5, 5, 5, 2, 5], [5, 2, 2, 2, 2, 5], [5, 5, 5, 5, 2, 5], [1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 1, 5, 2, 2, 2, 2, 5, 2, 1, 2, 5], [1, 1, 5, 5, 5, 5, 5, 5, 2, 2, 2, 5], [1, 5, 5, 5, 5, 1, 1, 5, 1, 2, 1, 5], [1, 5, 2, 2, 5, 1, 1, 5, 5, 5, 5, 5], [1, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1]]

    # for row in config:
    #     for index, item in enumerate(row):
    #         if item == 5:
    #             row[index] = 1
    #
    # heat_map = add_jagged_list(heat_map, config)

    attack = Attack(config)
    total = attack.hits + attack.misses
    csv += str(total) + "," + str(attack.search_misses) + "," + str(attack.misses - attack.search_misses) + "\n"

    #if i % 1000 == 0:
    #    print (i)

    print("Hits: ", attack.hits, ", Misses: ", attack.misses, ", Search Hits: ", attack.search_hits,
          ", Search Misses: ", attack.search_misses, "Other Misses: ", attack.misses - attack.search_misses)

with open("random_boards_lines_bubble.csv", 'w') as f:
    f.write("total shots,search misses,other misses\n" + csv)

# for row in heat_map:
#     print (row)