__author__ = 'Judd'

from random import randint, choice
import constants

class Attack:
    def __init__(self, enemy_config):
        self.view_of_opponent = [[constants.UNKNOWN] * (6 if x < 6 else 12) for x in range(constants.BOARD_HEIGHT)]

        self.hits = 0
        self.misses = 0
        self.repeats = 0
        self.enemy_config = enemy_config

        #print (self.view_of_opponent)

        while self.hits < constants.TOTAL_HITS:
            i, j = self.random()

            if self.repeats >= 1000:
                break

            if self.view_of_opponent[i][j] != constants.UNKNOWN:
                self.repeats += 1
                continue

            self.attack_enemy(i, j)

    def attack_enemy(self, i, j):
        if self.enemy_config[i][j] == constants.OCCUPIED:
            self.hits += 1
            self.view_of_opponent[i][j] = constants.OCCUPIED
        else:
            self.misses += 1
            self.view_of_opponent[i][j] = constants.UNOCCUPIED

    def random(self):
        while True:
            i1 = randint(0, 11)

            if i1 < 6:
                i2 = randint(0, 5)
            else:
                i2 = randint(0, 11)

            return i1, i2