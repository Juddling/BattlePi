__author__ = 'Judd'

import constants
from Attack import Attack, HuntType
from game_logic import InitPlayerBoard, DeployFleet
from addition import add_jagged_list
from GameManager import *
import boards

boards = [
    boards.enemy_config1,
    boards.enemy_config2,
    boards.enemy_config3,
    boards.enemy_config4,
    boards.enemy_config5,
    boards.enemy_config6,
    boards.enemy_config7,
    boards.enemy_config8,
    boards.enemy_config9,
    boards.enemy_config10
]

def run_board_csv(iterations, csv):
    for bla in range(iterations):
        manager = IterateGameManager(board)

        attack = manager.attacker
        total = attack.hits + attack.misses
        csv += str(total) + "," + str(attack.search_misses) + "," + str(attack.misses - attack.search_misses) + "\n"

i = 1
iterations = 1000

for board in boards:
    csv = ""

    run_board_csv(iterations, csv)

    file_name = "lines" + str(i) + ".csv"

    with open(file_name, 'w') as f:
        f.write("total shots,search misses,other misses\n" + csv)
        print("wrote to", file_name)

    i += 1

quit()

iterations = 1000
csv = ""
#heat_map = InitPlayerBoard(0)

for i in range(iterations):

    # use this to deploy a random board
    while True:
        config = InitPlayerBoard()
        try:
            DeployFleet(config, False)
        except RuntimeError:
            continue

        break


    # # use this for generating a heat map from random boards
    # for row in config:
    #     for index, item in enumerate(row):
    #         if item == 5:
    #             row[index] = 1
    #
    # heat_map = add_jagged_list(heat_map, config)
    # # end heat map

    manager = IterateGameManager(boards.enemy_config2)

    attack = manager.attacker
    total = attack.hits + attack.misses
    csv += str(total) + "," + str(attack.search_misses) + "," + str(attack.misses - attack.search_misses) + "\n"

    if attack.misses - attack.search_misses >= 20:
        pass

    unique = set(attack.eliminated_points)

    print("Hits: ", attack.hits, ", Misses: ", attack.misses, ", Search Hits: ", attack.search_hits,
          ", Search Misses: ", attack.search_misses, "Other Misses: ", attack.misses - attack.search_misses,
          " Elim: ", len(unique), " 36 search: ", attack.thirty_six_search)

with open("lines2.csv", 'w') as f:
    f.write("total shots,search misses,other misses\n" + csv)