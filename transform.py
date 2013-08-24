from random import randint


def RotateLeft(matrix):
    transformed = []
    # add some empty rows
    for i in range(0, len(matrix[0])):
        transformed.append([])
    for row_index, row in enumerate(matrix):
        for column_index, cell in enumerate(row):
            transformed[column_index].append(cell)
    return transformed


def RandomTransform(matrix):
    rand = randint(1, 4)

    if rand == 1:
        return matrix
    elif rand == 2:
        return RotateLeft(matrix)
    elif rand == 3:
        return matrix[::-1]

    return RotateLeft(matrix[::-1])


def GetShips():
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