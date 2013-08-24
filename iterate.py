__author__ = 'Judd'

import constants
from Attack import Attack

enemy_config = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 1, 1],
    [2, 2, 1, 1, 1, 1],
    [1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

iterations = 10

for i in range(iterations):
    attack = Attack(enemy_config)

    print("Hits: ", attack.hits, ", Misses: ", attack.misses, ", Repeats: ", attack.repeats)