__author__ = 'Judd'

from random import randint, shuffle
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
                raise RuntimeError('Too many repeats!')

            if self.repeat_check(i, j):
                continue

            self.attack_enemy(i, j)

        pass

    def repeat_check(self, i, j):
        if self.view_of_opponent[i][j] != constants.UNKNOWN:
            self.repeats += 1
            return True

        return False

    def legal_position(self, i, j):
        if i < 0 or j < 0:
            return False

        if i >= constants.BOARD_HEIGHT:
            return False

        if j >= len(self.view_of_opponent[i]):
            return False

        return True

    def eliminated(self, i, j):
        """can square be eliminated because all neighbours are known"""

        neighbours = [
            [i - 1, j],
            [i + 1, j],
            [i, j - 1],
            [i, j + 1]
        ]

        count = 0

        for square in neighbours:
            if not self.legal_position(square[0], square[1]) or self.known_square(square[0], square[1]):
                count += 1
            else:
                return False

        if count == 4:
            return True

        return False

    def known_square(self, i, j):
        square = self.view_of_opponent[i][j]

        if square == constants.OCCUPIED or square == constants.UNOCCUPIED:
            return True

        return False

    def attack_enemy(self, i, j):
        if self.hits >= constants.TOTAL_HITS:
            return

        if not self.legal_position(i, j):
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
            i = randint(0, 11)

            if i < 6:
                j = randint(0, 5)
            else:
                j = randint(0, 11)

            if i % 2 == 0 and j % 2 == 1:
                continue

            if i % 2 == 1 and j % 2 == 0:
                continue

            if self.eliminated(i, j):
                continue

            return i, j

    def markers(self):
        """center of each 3x3 sudoku square"""

        if not hasattr(self, 'marker_count'):
            self.marker_count = 0
        else:
            self.marker_count += 1

        if not hasattr(self, 'twelve'):
            self.twelve = [
                [1, 1],
                [1, 4],
                [4, 1],
                [4, 4],
                [7, 1],
                [7, 4],
                [10, 1],
                [10, 4],
                [7, 7],
                [7, 10],
                [10, 7],
                [10, 10]
            ]

            thirty_six = [
                [0, 0],
                [0, 3],
                [2, 2],
                [2, 5],
                [3, 0],
                [3, 3],
                [5, 2],
                [5, 5],
                [6, 0],
                [6, 3],
                [8, 2],
                [8, 5],
                [9, 0],
                [9, 3],
                [11, 2],
                [11, 5],
                [6, 6],
                [6, 9],
                [8, 8],
                [8, 11],
                [9, 6],
                [9, 10],
                [11, 9],
                [11, 11]
            ]

            shuffle(self.twelve)
            shuffle(thirty_six)

        if self.marker_count >= 12:
            raise RuntimeError('Got too big!')

        return self.twelve[self.marker_count][0], self.twelve[self.marker_count][1]

    def is_hit(self, i, j):
        return self.view_of_opponent[i][j] == constants.OCCUPIED

    def hunt(self, i, j):
        """Surrounds a hit to try and sink a ship"""

        self.attack_enemy(i, j - 1) # left
        self.attack_enemy(i, j + 1) # right
        self.attack_enemy(i + 1, j) # up
        self.attack_enemy(i - 1, j) # down