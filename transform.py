import constants
import random

from collections import Counter

class NoRecommendationError(RuntimeError):
    pass

class ShapeAndCoOrds():
    def __init__(self, shape, co_ords):
        self.shape = shape
        self.co_ords = co_ords

    def all_transformations(self):
        """
        returns tuple (rotated, list of relative co ords)
        """
        i = 0

        for i in range(4):
            m = Matrix(self.shape)
            yield (m.rotate_n(i), [x for x in self.transform_co_ords(i)])

    def transform_co_ords(self, i):
        height = len(self.shape)

        if i == 0:
            # not sure why i can't just return the list in this situation
            for tup in self.co_ords:
                yield tup
        if i == 1:
            for tup in self.co_ords:
                yield (tup[1], tup[0])
        if i == 2:
            for tup in self.co_ords:
                yield (height - 1 - tup[0], tup[1])
        if i == 3:
            for tup in self.co_ords:
                yield (tup[1], height - 1 - tup[0])


class Recommendation():
    four_boat = {
        "shape": [[0, 0, 0, 0]],
        "points": [(0, 0), (0, 1), (0, 2), (0, 3)]
    }
    three_boat = {
        "shape": [[0, 0, 0]],
        "points": [(0, 0), (0, 1), (0, 2)]
    }
    two_boat = {
        "shape": [[0, 0]],
        "points": [(0, 0), (0, 1)]
    }
    carrier = {
        "shape": [
            [0,0,0],
            [5,0,5],
            [5,0,5],
            [5,0,5]
        ],
        "points": [
            (0,0),
            (0,1),
            (0,2),
            (1,1),
            (2,1),
            (3,1)
        ]
    }
    hovercraft = {
        "shape": [
            [5,0,5],
            [0,0,0],
            [0,5,0]
        ],
        "points": [
            (0,1),
            (1,0),
            (2,0),
            (1,1),
            (1,2),
            (2,2)
        ]
    }

    @staticmethod
    def point_from_remaining(board, remaining_boats):
        """
        determines all possible locations on the board that unsunk boats can be (in all transformations) and adds
        them to allowed_points, then returns the most probable location
        """
        allowed_points = []

        for boat in remaining_boats:
            bla = ShapeAndCoOrds(boat['shape'], boat['points'])

            for result in bla.all_transformations():
                matches = match_matrix(result[0], Recommendation.pad_out_board(board[:]))

                for j, i in matches: # reversed on purpose
                    for relative_tuple in result[1]:
                        allowed_points.append((i + relative_tuple[0], j + relative_tuple[1]))

        if len(allowed_points) == 0:
            raise NoRecommendationError('no recommendations for the boat, yet seems to be last remaining')

        lst = Counter(allowed_points).most_common()
        highest_count = max([i[1] for i in lst])
        values = [i[0] for i in lst if i[1] == highest_count]
        random.shuffle(values)
        return values[0]

    @staticmethod
    def point(board, shape, co_ords):
        """
        DEPRECATED - returns the most probable location to shoot given a single boat / shape
        """
        bla = ShapeAndCoOrds(shape, co_ords)

        allowed_points = []

        for result in bla.all_transformations():
            matches = match_matrix(result[0], Recommendation.pad_out_board(board[:]))

            for j, i in matches: # reversed on purpose
                for relative_tuple in result[1]:
                    allowed_points.append((i + relative_tuple[0], j + relative_tuple[1]))

        d = {x: allowed_points.count(x) for x in allowed_points}

        for w in sorted(d, key=d.get, reverse=True):
            return w

        raise RuntimeError('no recommendations for the boat, yet seems to be last remaining')

    @staticmethod
    def pad_out_board(board):
        """
        fills in the missing top right corner with misses to make the board a square
        """
        for i, row in enumerate(board):
            if len(row) == 6:
                for bla in range(6):
                    board[i].append(1)

        return board


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotate_n(self, n):
        if n == 4 or n == 0:
            # four / zero rotations = identity
            return self.matrix
        if n == 3:
            return self.rotate(self.rotate(self.rotate(self.matrix)))
        if n == 2:
            return self.rotate(self.rotate(self.matrix))
        if n == 1:
            return self.rotate(self.matrix)

    def rotate(self, input_matrix):
        """rotates matrix to the left"""

        transformed = []
        height = len(input_matrix)
        width = len(input_matrix[0])

        for i in range(0, width):
            # add blank cells
            transformed.append([])

        for row in input_matrix:
            index = 0
            for cell in row:
                # top left should become bottom left
                column_index = height - 1 - index

                if column_index < 0 or column_index > width:
                    pass

                transformed[width - 1 - index].append(cell)
                index += 1

        return transformed

    def reflect_x(self):
        """Reflects along the x-axis"""
        return self.matrix[::-1]

    def reflect_y(self):
        """Reflects along the y-axis"""
        transformed = []

        for row in self.matrix:
            transformed.append(row[::-1])

        return transformed

    def all_transformations(self):
        return [
            self.matrix,
            self.rotate_n(1),
            self.rotate_n(2),
            self.rotate_n(3),
            #self.reflect_x(),
            #self.reflect_y()
        ]


class Ships:
    Carrier = [
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]

    Hovercraft = [
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 1, 1, 1, 1]
    ]

    Destroyer = [
        [1, 1, 1, 1],
        [1, 2, 2, 1],
        [1, 1, 1, 1]
    ]
    Cruiser = [
        [1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]
    Battleship = [
        [1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1]
    ]

    def all(self):
        return [self.Carrier, self.Hovercraft, self.Destroyer, self.Cruiser, self.Battleship]


def bubble_ships():
    """
    all the ships with space (a bubble) around them
    """

    Carrier = [
        [1, 5, 5, 5, 1],
        [1, 5, 2, 5, 1],
        [1, 5, 2, 5, 1],
        [1, 5, 2, 5, 1],
        [5, 2, 2, 2, 5],
        [5, 5, 5, 5, 5]
    ]

    Hovercraft = [
        [5, 5, 5, 5, 5],
        [5, 1, 2, 1, 5],
        [5, 2, 2, 2, 5],
        [5, 2, 1, 2, 5],
        [5, 5, 5, 5, 5]
    ]

    Destroyer = [
        [5, 5, 5, 5],
        [5, 2, 2, 5],
        [5, 5, 5, 5]
    ]
    Cruiser = [
        [5, 5, 5, 5, 5],
        [5, 2, 2, 2, 5],
        [5, 5, 5, 5, 5]
    ]
    Battleship = [
        [5, 5, 5, 5, 5, 5],
        [5, 2, 2, 2, 2, 5],
        [5, 5, 5, 5, 5, 5]
    ]

    return [Carrier, Hovercraft, Destroyer, Cruiser, Battleship]


def raw_ships():
    Carrier = [
        [1, 2, 1],
        [1, 2, 1],
        [1, 2, 1],
        [2, 2, 2],
    ]

    Hovercraft = [
        [1, 2, 1],
        [2, 2, 2],
        [2, 1, 2],
    ]

    Destroyer = [
        [2, 2]
    ]
    Cruiser = [
        [2, 2, 2]
    ]
    Battleship = [
        [2, 2, 2, 2]
    ]

    return [Carrier, Hovercraft, Destroyer, Cruiser, Battleship]


def slice_overlap(listin, n):
    """overlapping slice through list of size n"""
    i = 0
    max_overlaps = len(listin) - n + 1

    while i < max_overlaps:
        yield listin[i:i + n]
        i += 1


def match_match_single(x, y, bubble=constants.BUBBLE):
    """
    x is single element from the needle, will allow 5s / bubble to match against anything
    bubble being in the function signature is an optimization
    """

    # if x == constants.UNKNOWN or y == constants.UNKNOWN:
    #     return True

    return x == y or x == bubble


def match_slice(needle, haystack):
    i = 0
    for element in needle:
        if not match_match_single(element, haystack[i]):
            return False
        i += 1

    return True


def match_row(needle, haystack):
    i = 0
    for slice in slice_overlap(haystack, len(needle)):
        if match_slice(needle, slice):
            yield i
        i += 1


def match_matrix_same_height(needle, haystack):
    if len(needle) != len(haystack):
        raise RuntimeError('matrices should be same height')

    temp_matches = []

    i = 0
    for row in needle:
        row_matches = match_row(row, haystack[i])

        if row_matches:
            temp_matches.append(row_matches)
        else:
            temp_matches.append(-1)

        i += 1

    return temp_matches


def match_matrix(needle, haystack):
    """matches a pattern against a ship"""

    matches = []

    for j in range(len(haystack) - len(needle) + 1):
        ungrouped = match_matrix_same_height(needle, haystack[j:j + len(needle)])

        positions = matches_to_relative_position(group_matches(ungrouped), j)

        for p in positions:
            matches.append(p)

    # for index, cell in enumerate(matches):
    #     if cell == []:
    #         matches.pop(index)

    return matches


def group_matches(matches):
    """interpret the match_row() results to give a result to show where the whole matrix was matched"""

    cols = []

    for row in matches:
        # expand the generator
        row_expanded = [x for x in row]

        if not cols:
            cols = row_expanded[:]

            if not cols:
                # if cols still empty after first run, then there can be no values in all columns
                break

            continue

        for col in cols[:]:
            # if you remove an element, python doesn't iterate to the true end of the list, so iterate through a copy
            # if column is not contained in next row, remove it

            # can't check if element is in a generator
            if col not in row_expanded:
                cols.remove(col)

                if len(cols) == 0:
                    return []

    return cols

def matches_to_relative_position(matches, j):
    for i in matches:
        yield (i, j)

def only_hits(matrix):
    i = 0
    for row in matrix:
        j = 0

        for cell in row:
            if cell != constants.OCCUPIED:
                matrix[i][j] = 0

            j += 1
        i += 1
    return matrix