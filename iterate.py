__author__ = 'Judd'

import constants
from Attack import Attack, HuntType
from game_logic import InitPlayerBoard, DeployFleet
from addition import add_jagged_list
from GameManager import *

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

enemy_config3 = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1],
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
    [1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1],
    [1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

enemy_config6 = [
    [1, 1, 1, 2, 2, 2],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 1],
    [1, 1, 2, 2, 1, 1],
    [1, 1, 1, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    [2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1],
]

enemy_config7 = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

enemy_config8 = [
    [1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1],
    [1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2],
]

enemy_config9 = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 2, 1, 1],
    [1, 2, 1, 2, 1, 1],
    [1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1],
    [1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
]

enemy_config10 = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1],
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

ant_config = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 1, 1],
    [1, 1, 1, 2, 2, 1],
    [2, 2, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
]

# boards = [
#     enemy_config1,
#     enemy_config2,
#     enemy_config3,
#     enemy_config4,
#     enemy_config5,
#     enemy_config6,
#     enemy_config7,
#     enemy_config8,
#     enemy_config9,
#     enemy_config10
# ]
#
# i = 1
# iterations = 1000
#
# for board in boards:
#     csv = ""
#
#     for bla in range(iterations):
#         manager = IterateGameManager(enemy_config9)
#
#         attack = manager.attacker
#         total = attack.hits + attack.misses
#         csv += str(total) + "," + str(attack.search_misses) + "," + str(attack.misses - attack.search_misses) + "\n"
#
#     file_name = "lines" + str(i) + ".csv"
#
#     with open(file_name, 'w') as f:
#         f.write("total shots,search misses,other misses\n" + csv)
#         print("wrote to ", file_name)
#
#     i += 1


iterations = 1000
csv = ""
#heat_map = InitPlayerBoard(0)

for i in range(iterations):
    while True:
        config = InitPlayerBoard()
        try:
            DeployFleet(config, False)
        except RuntimeError:
            continue

        break

    # for row in config:
    #     for index, item in enumerate(row):
    #         if item == 5:
    #             row[index] = 1
    #
    # heat_map = add_jagged_list(heat_map, config)

    manager = IterateGameManager(enemy_config4)

    attack = manager.attacker
    total = attack.hits + attack.misses
    csv += str(total) + "," + str(attack.search_misses) + "," + str(attack.misses - attack.search_misses) + "\n"

    unique = set(attack.eliminated_points)

    print("Hits: ", attack.hits, ", Misses: ", attack.misses, ", Search Hits: ", attack.search_hits,
          ", Search Misses: ", attack.search_misses, "Other Misses: ", attack.misses - attack.search_misses,
          " Elim: ", len(unique), " 36 search: ", attack.thirty_six_search)

with open("lines4.csv", 'w') as f:
    f.write("total shots,search misses,other misses\n" + csv)