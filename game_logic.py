import constants
from random import randint
import transform

__author__ = 'Judd'

# Check whether the fleet is sunk
def CheckWinner(Board):
    # We just need to test whether the number of hits equals the total number of squares in the fleet
    hits = 0
    for i in range(12):
        hits += Board[i].count(4)
    return hits == 21

# Initialise the boards: player to empty, opponent to unknown
def InitBoards():
    # The boards are stored in a "jagged" 2 dimensional list
    # Example: to access the opponent at position B6 use Opponent[1][5]
    # (Remember python indexes from 0)

    # The following convention is used for storing the state of a square:
    # 0 = Unknown
    # 1 = Empty
    # 2 = Occupied
    # 3 = Missed
    # 4 = Hit (player or opponent)

    # Initially, the player's board is all empty, the opponent's is all unknown
    Player = InitPlayerBoard()
    Opponent = [[0] * (6 if x < 6 else 12) for x in range(constants.BOARD_HEIGHT)]

    return Player, Opponent

def InitPlayerBoard(square = 1):
    return [[square] * (6 if x < 6 else 12) for x in range(constants.BOARD_HEIGHT)]

# Read a move from the keyboard and return board indices

def RandomCoOrdinates():
    i1 = randint(0, 11)
    if i1 < 6:
        # Top half of board, so choose between first and sixth row
        i2 = randint(0, 5)
    else:
        # Bottom half so choose between first and twelfth row
        i2 = randint(0, 11)

    return i1, i2



# Decide what move to make based on current state of opponent's board and print it out
def ChooseAndPrintMove(Opponent):
    # Completely random strategy
    # Knowledge about opponent's board is completely ignored
    i1, i2 = RandomCoOrdinates()

    # Display move in letter+number grid reference
    print('my move: ', chr(i1 + 65), i2 + 1)
    return i1, i2

# Distribute the fleet onto your board
def DeployFleet(Player, verbose=False):
    ships = transform.raw_ships()
    initial = Player.copy()

    for ship in ships:
        m = transform.Matrix(ship)
        ship = m.rotate_n(randint(1,4))

        x, y = ValidPlacement(Player, ship, verbose)

        if verbose:
            PrintMove(x, y)

        i = 0
        for row in ship:
            # Player[x+i][y:y+len(row)-1] = row
            j = y
            for cell in row:
                Player[x+i][j] = cell
                j += 1
            i += 1

    return Player

def ValidPlacement(domain, ship, verbose=False):
    attempts = 0
    while True:
        if attempts > 10:
            raise RuntimeError('Could not find solution after multiple attempts')

        x, y = RandomCoOrdinates()

        if (x + len(ship)) > constants.BOARD_HEIGHT:
            continue

        if (y + len(ship[0])) > len(domain[x]):
            continue

        if verbose:
            print ("doing some checking...")

        # collisions
        collision = False
        for row in domain[x:x+len(ship)]:
            if verbose:
                print (row)

            if constants.OCCUPIED in row[y:y+len(ship[0])]:
                if verbose:
                    print ("collision found")
                collision = True

        if collision:
            attempts += 1
            continue

        # if clips outside edge?

        return x, y