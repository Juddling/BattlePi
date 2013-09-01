from random import randint
import constants


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotate_n(self, n):
        if n == 4:
            return self.rotate(self.rotate(self.rotate(self.rotate(self.matrix))))
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
                index+=1

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
    # reverse elements in the list
    # original[::-1]

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
    # reverse elements in the list
    # original[::-1]

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
        [2,2]
    ]
    Cruiser = [
        [2,2,2]
    ]
    Battleship = [
        [2,2,2,2]
    ]

    return [Carrier, Hovercraft, Destroyer, Cruiser, Battleship]


def slice_overlap(listin, n):
    """overlapping slice through list of size n"""
    i = 0
    while i < len(listin) - n + 1:
        yield listin[i:i + n]
        i += 1


def match_match_single(x, y):
    if x == constants.UNKNOWN or y == constants.UNKNOWN:
        return True

    return x == y


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


def match_matrix(needle, haystack):
    """matches a pattern against a ship, right now pattern and ship must have the same height"""

    matches = []

    for j in range(len(haystack) - len(needle) + 1):
        temp_matches = []

        i = 0
        for row in needle:
            row_matches = match_row(row, haystack[j + i])

            if row_matches:
                temp_matches.append(row_matches)
            else:
                temp_matches.append(-1)

            i += 1

        matches.append(group_matches(temp_matches))

    return matches


def group_matches(matches):
    """interpret the match_row() results to give a result to show where the whole matrix was matched"""

    cols = []

    for row in matches:
        if not cols:
            cols = [x for x in row]

            if not cols:
                # if cols still empty after first run, then there can be no values in all columns
                break

            continue

        for col in cols:
            # if column is not contained in next row, remove it
            if col not in row:
                cols.remove(col)

    return cols

def matches_to_relative_position(matches):
    pos = []
    j = 0

    for row in matches:
        for i in row:
            yield (i, j)

        j += 1

def heat_map(matches, haystack):
    # TODO: tweak the haystacks according to the tuples in matches
    # TODO: use matrix addition to make the heatmap

    pass


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