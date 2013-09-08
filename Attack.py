__author__ = 'Judd'

from random import randint, shuffle
import constants


class HuntType:
    LINES = 1
    RECURSIVE = 2
    SEARCH = 3
    SINGLE_LINE = 4
    INTELLIGENT = 5


class Attack:
    def __init__(self, enemy_config, attack_type):
        self.view_of_opponent = [[constants.UNKNOWN] * (6 if x < 6 else 12) for x in range(constants.BOARD_HEIGHT)]

        self.default_attack_type = attack_type
        self.hits = 0
        self.misses = 0
        self.repeats = 0
        self.enemy_config = enemy_config
        self.search_hits = 0
        self.search_misses = 0
        self.true_random = False
        self.neighbours_hunted = []
        self.sunk_carrier = False
        self.sunk_hovercraft = False
        self.sunk_two_boat = False

        #print (self.view_of_opponent)

        while self.hits < constants.TOTAL_HITS:
            i, j = self.random()

            # if self.repeats >= 500:
            #     raise RuntimeError('Reverted to random shooting')
            #     # TODO: get rid of this, revert to shooting neighbours of existing hits
            #     self.true_random = True

            if self.repeats >= 5000:
                #defintely a fuck up
                raise RuntimeError('Too many repeats!')

            if self.repeat_check(i, j):
                continue

            self.attack_enemy(i, j, HuntType.SEARCH)

            if self.hits == 15:
                pass

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
            if self.legal_position(square[0], square[1]) and self.is_hit(square[0], square[1]):
                return False

            if not self.legal_position(square[0], square[1]) or self.is_empty(square[0], square[1]):
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

    def attack_enemy(self, i, j, attack_type):
        if i == 10 and j == 10:
            pass

        if self.hits >= constants.TOTAL_HITS:
            return

        if not self.legal_position(i, j):
            return

        if self.repeat_check(i, j):
            if self.is_hit(i, j):
                if attack_type == HuntType.RECURSIVE:
                    self.hunt(i, j)
                    return

                return True

            return

        if self.enemy_config[i][j] == constants.OCCUPIED:
            self.hits += 1
            self.view_of_opponent[i][j] = constants.OCCUPIED

            if attack_type == HuntType.SEARCH:
                self.search_hits += 1

                if self.default_attack_type == HuntType.LINES:
                    self.shoot_lines(i, j)
                else:
                    self.hunt(i, j)

            if attack_type == HuntType.RECURSIVE:
                self.hunt(i, j)

            return True
        else:
            if attack_type == HuntType.SEARCH:
                self.search_misses += 1

            self.misses += 1
            self.view_of_opponent[i][j] = constants.UNOCCUPIED

            return False

    def random(self):
        """Searches for ships across the whole domain"""

        while True:
            i = randint(0, 11)

            if i < 6:
                j = randint(0, 5)
            else:
                j = randint(0, 11)

            if not self.true_random:
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

    def is_empty(self, i, j):
        return self.view_of_opponent[i][j] == constants.UNOCCUPIED

    def attack_above_and_below(self, i, j):
        if self.attack_enemy(i + 1, j, HuntType.LINES):
            if self.attack_enemy(i - 1, j, HuntType.LINES):
                return True
            else:
                # four in a row, then one was a hit and the other side wasn't... must be touching shapes... hunt!
                self.hunt(i + 1, j)

        return False

    def attack_left_and_right(self, i, j):
        if self.attack_enemy(i, j + 1, HuntType.LINES):
            if self.attack_enemy(i, j - 1, HuntType.LINES):
                return True
            else:
                # four in a row, then one was a hit and the other side wasn't... must be touching shapes... hunt!
                self.hunt(i, j + 1)

        return False

    def shoot_lines(self, i, j):
        line = 1
        i_direction = -1
        j_direction = 0
        hits = 0

        while True:
            current_i = i + (line * i_direction)
            current_j = j + (line * j_direction)

            if self.legal_position(current_i, current_j) and self.is_hit(current_i, current_j):
                # if where you plan to shoot is already a hit, it's touching ships as the strategy now eliminates
                # ships as it finds them

                self.hunt(i, j)
                return

            attack_result = self.attack_enemy(current_i, current_j, HuntType.LINES)

            if attack_result:
                hits += 1

                if hits == 3:
                    # four in a row, now lets eliminate the T shape

                    if self.sunk_carrier:
                        return

                    if j_direction != 0:
                        #horizontal four
                        if not self.attack_above_and_below(current_i, current_j):
                            if self.attack_above_and_below(current_i, current_j - (j_direction * 3)):
                                self.sunk_carrier = True
                                return

                    if i_direction != 0:
                        #vertical four
                        if not self.attack_left_and_right(current_i, current_j):
                            if self.attack_left_and_right(current_i - (i_direction * 3), current_j):
                                self.sunk_carrier = True
                                return

                    # stopping the miss after taking out the four boat
                    return

                line += 1
                continue
            else:
                if j_direction == -1:
                    if hits == 1:
                        if not self.sunk_hovercraft:
                            self.handle_two_horizontal(current_i, current_j+1)
                        else:
                            if not self.sunk_two_boat:
                                self.sunk_two_boat = True
                            else:
                                # already sunk the two boat, something's wrong...
                                self.hunt(current_i, current_j+1)

                        return

                    if hits == 2:
                        self.handle_three_horizontal(current_i, current_j+2)

                    # here should be hunting for 2 boats
                    return

                if j_direction == 1:
                    j_direction = -1

                if i_direction == 1:
                    # from down to right

                    if hits == 2:
                        self.handle_three_vertical(current_i-2, current_j)

                    if hits == 1:
                        if not self.sunk_hovercraft:
                            self.handle_two_vertical(current_i-2, current_j)
                        else:
                            if not self.sunk_two_boat:
                                self.sunk_two_boat = True
                            else:
                                # already sunk the two boat, something's wrong...
                                self.hunt(current_i, current_j-2)

                    if hits > 0:
                        return

                    i_direction = 0
                    j_direction = 1

                if i_direction == -1:
                    i_direction = 1

                line = 1
                continue

    def handle_three_vertical(self, i, j):

        if not self.sunk_carrier or not self.sunk_hovercraft:
            hits_on_t = self.shoot_line(i, j-1, 0, -1)

            if hits_on_t == 1:
                if self.attack_enemy(i + 1, j + 1, HuntType.INTELLIGENT) and self.attack_enemy(i - 1, j + 1, HuntType.INTELLIGENT):
                    self.sunk_hovercraft = True
                    return

            elif hits_on_t == 0:
                # then shoot the other side!

                hits_on_t_other = self.shoot_line(i, j+1, 0, 1)

                if hits_on_t_other == 1:
                    if self.attack_enemy(i + 1, j - 1, HuntType.INTELLIGENT) and self.attack_enemy(i - 1, j - 1, HuntType.INTELLIGENT):
                        self.sunk_hovercraft = True
                        return
                elif hits_on_t_other == 3:
                    self.sunk_carrier = True
                    return

            elif hits_on_t == 3:
                self.sunk_carrier = True
                return

    def handle_three_horizontal(self, i, j):
        """ i, j relative to middle of the three"""

        #   X   <- shooting here
        # 2 2 2

        if not self.sunk_carrier or not self.sunk_hovercraft:
            hits_on_t = self.shoot_line(i-1, j, -1, 0)

            if hits_on_t == 1:
                if self.attack_enemy(i + 1, j - 1, HuntType.INTELLIGENT) and self.attack_enemy(i + 1, j + 1, HuntType.INTELLIGENT):
                    self.sunk_hovercraft = True
                    return

            elif hits_on_t == 0:
                # then shoot the other side!

                hits_on_t_other = self.shoot_line(i+1, j, 1, 0)

                if hits_on_t_other == 1:
                    if self.attack_enemy(i - 1, j + 1, HuntType.INTELLIGENT) and self.attack_enemy(i - 1, j - 1, HuntType.INTELLIGENT):
                        self.sunk_hovercraft = True
                        return
                elif hits_on_t_other == 3:
                    self.sunk_carrier = True
                    return

            elif hits_on_t == 3:
                self.sunk_carrier = True
                return

    def handle_two_vertical(self, i, j):
        top_left = self.attack_enemy(i, j-1, HuntType.INTELLIGENT)
        top_right = self.attack_enemy(i, j+1, HuntType.INTELLIGENT)

        if top_left and top_right:
            self.destroy_hovercraft_vertical(i, j, False)
            return
        elif top_left and not top_right:
            self.destroy_hovercraft_vertical(i, j-1, True)
            return
        elif not top_left and top_right:
            self.destroy_hovercraft_vertical(i, j+1, True)
            return
        else:
            bottom_left = self.attack_enemy(i+1, j-1, HuntType.INTELLIGENT)
            bottom_right = self.attack_enemy(i+1, j+1, HuntType.INTELLIGENT)

            if bottom_left and bottom_right:
                self.destroy_hovercraft_vertical(i+1, j, True)
                return
            elif bottom_left and not bottom_right:
                self.destroy_hovercraft_vertical(i+1, j-1, False)
                return
            elif not bottom_left and bottom_right:
                self.destroy_hovercraft_vertical(i+1, j+1, False)
                return

    def handle_two_horizontal(self, i, j):
        """ i, j should be the left of the horizontal"""

        top_left = self.attack_enemy(i-1, j, HuntType.INTELLIGENT)
        bottom_left = self.attack_enemy(i+1, j, HuntType.INTELLIGENT)

        if top_left and bottom_left:
            self.destroy_hovercraft_horizontal(i, j, False)
            return
        elif top_left and not bottom_left:
            self.destroy_hovercraft_horizontal(i-1, j, True)
            return
        elif not top_left and bottom_left:
            self.destroy_hovercraft_horizontal(i+1, j, True)
            return
        else:
            top_right = self.attack_enemy(i-1, j+1, HuntType.INTELLIGENT)
            bottom_right = self.attack_enemy(i+1, j+1, HuntType.INTELLIGENT)

            if top_right and bottom_right:
                self.destroy_hovercraft_horizontal(i, j+1, True)
                return
            elif top_right and not bottom_right:
                self.destroy_hovercraft_horizontal(i-1, j+1, False)
                return
            elif not top_right and bottom_right:
                self.destroy_hovercraft_horizontal(i+1, j+1, False)
                return

    def destroy_hovercraft_vertical(self, i, j, facing_up):
        """ i,j should be the middle of the three """

        co_ords = []

        if facing_up:
            co_ords.append((i-1, j))
            co_ords.append((i, j+1))
            co_ords.append((i, j-1))
            co_ords.append((i+1, j+1))
            co_ords.append((i+1, j-1))
        else:
            co_ords.append((i+1, j))
            co_ords.append((i, j+1))
            co_ords.append((i, j-1))
            co_ords.append((i-1, j+1))
            co_ords.append((i-1, j-1))

        self.destroy_hovercraft(co_ords)

    def destroy_hovercraft_horizontal(self, i, j, facing_left):
        """ i,j should be the middle of the three """
        co_ords = []

        if facing_left:
            co_ords.append((i-1, j))
            co_ords.append((i+1, j))
            co_ords.append((i, j-1))
            co_ords.append((i-1, j+1))
            co_ords.append((i+1, j+1))
        else:
            co_ords.append((i-1, j))
            co_ords.append((i+1, j))
            co_ords.append((i, j+1))
            co_ords.append((i-1, j-1))
            co_ords.append((i+1, j-1))

        self.destroy_hovercraft(co_ords)

    def destroy_hovercraft(self, co_ords):
        for i,j in co_ords:
            if not self.attack_enemy(i, j, HuntType.INTELLIGENT):
                return

        self.sunk_hovercraft = True

    def hunt(self, i, j):
        """Surrounds a hit to try and sink a ship"""

        if (i, j) in self.neighbours_hunted:
            return

        self.neighbours_hunted.append((i,j))

        self.attack_enemy(i, j - 1, HuntType.RECURSIVE) # left
        self.attack_enemy(i, j + 1, HuntType.RECURSIVE) # right
        self.attack_enemy(i + 1, j, HuntType.RECURSIVE) # up
        self.attack_enemy(i - 1, j, HuntType.RECURSIVE) # down

    def shoot_line(self, i, j, i_direction, j_direction):
        dist = 0
        hits = 0

        while True:
            if hits == 3:
                break

            current_i = i + (i_direction * dist)
            current_j = j + (j_direction * dist)

            if not self.legal_position(current_i, current_j):
                return hits

            attack_result = self.attack_enemy(current_i, current_j, HuntType.SINGLE_LINE)

            if not attack_result:
                # None / False
                return hits

            if self.is_hit(current_i, current_j):
                hits += 1

            dist += 1

        return hits