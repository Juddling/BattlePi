from game_logic import InitPlayerBoard

def add_jagged_list(list_one, list_two):
    result = InitPlayerBoard(0)

    i = 0
    for row in list_one:
        result[i] = [i for i in map(lambda x, y: x + y, row, list_two[i])]
        i += 1

    return result