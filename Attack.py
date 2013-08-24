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

            if self.repeat_check(i, j):
                continue

            self.attack_enemy(i, j)

    def repeat_check(self, i, j):
        if self.view_of_opponent[i][j] != constants.UNKNOWN:
            self.repeats += 1
            return True

        return False

    def attack_enemy(self, i, j):
        if i < 0 or j < 0:
            return

        if i > constants.BOARD_HEIGHT:
            return

        if j >= len(self.view_of_opponent[i]):
            return

        if self.repeat_check(i, j):
            return

        if self.enemy_config[i][j] == constants.OCCUPIED:
            self.hits += 1
            self.view_of_opponent[i][j] = constants.OCCUPIED

            self.hunt(i, j)
        else:
            self.misses += 1
            self.view_of_opponent[i][j] = constants.UNOCCUPIED

    def random(self):
        """Searches for ships across the whole domain"""

        while True:
            i1 = randint(0, 11)

            if i1 < 6:
                i2 = randint(0, 5)
            else:
                i2 = randint(0, 11)

            return i1, i2

    def hunt(self, i, j):
        """Surrounds a hit to try and sink a ship"""

        self.attack_enemy(i, j-1) # left
        self.attack_enemy(i, j+1) # right
        self.attack_enemy(i+1, j) # up
        self.attack_enemy(i-1, j) # down