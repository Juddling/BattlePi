import os
import constants
from random import randint
import transform

__author__ = 'Judd'
# Clear the screen and draw the two boards side by side
def PrintBoards(Player, Opponent):
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print board labels
    print(' ' * 10, 'PLAYER', ' ' * 30, 'OPPONENT')
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    for x in range(6):
        print(letters[x], "  ".join(map(DisplayChar, Player[x])), " " * 18, "| ",
              "  ".join(map(DisplayChar, Opponent[x])))
    for x in range(6, 12):
        print(letters[x], "  ".join(map(DisplayChar, Player[x])), " | ", "  ".join(map(DisplayChar, Opponent[x])))
    print(" ", "  ".join(map(str, range(1, 10))), " 10 11 12", "  ", "  ".join(map(str, range(1, 10))), " 10 11 12")

# Mapping function that determines how each square state is displayed
def DisplayChar(x):
    if x == 0:
        return '?'
    elif x == constants.UNOCCUPIED or x == constants.BUBBLE:
        return ' '
    elif x == constants.OCCUPIED:
        return 'X'
    elif x == 3:
        return ' '
    elif x == 4:
        return '*'

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
    Player = [[1] * (6 if x < 6 else 12) for x in range(constants.BOARD_HEIGHT)]
    Opponent = [[0] * (6 if x < 6 else 12) for x in range(constants.BOARD_HEIGHT)]

    return Player, Opponent

# Read a move from the keyboard and return board indices
def GetMove():
    # We are expecting letter+number, e.g. C3
    is_valid = False
    while not is_valid:
        # Read opponent's move
        entry = input('Enter opponents move (e.g. C3): ')
        entry = entry.lower()
        if (len(entry) == 2) or (len(entry) == 3):
            # Convert letter coordinate into ASCII code and convert to index by subtracting code for 'a'
            i1 = ord(entry[0]) - 97
            # Convert number coordinate to zero-based indexing
            i2 = int(entry[1:]) - 1
            # Check whether they are valid coordinates
            if (i1 <= 5) and (i1 >= 0):
                # Top half of board
                is_valid = (i2 >= 0) and (i2 <= 5)
            elif (i1 >= 6) and (i1 <= 11):
                # Bottom half of board
                is_valid = (i2 >= 0) and (i2 <= 11)
        if not is_valid:
            print('Invalid coordinate, try again')
    return i1, i2

# Read the outcome of the shot from the keyboard
def GetOutcome():
    is_valid = False
    while not is_valid:
        entry = input('Outcome? (h/m) ')
        if entry.lower() == 'h':
            is_valid = True
            Outcome = 4
        elif entry.lower() == 'm':
            is_valid = True
            Outcome = 3
        else:
            print("Invalid input: must enter h (hit) or m (miss)")
    return Outcome


def RandomCoOrdinates():
    i1 = randint(0, 11)
    if i1 < 6:
        # Top half of board, so choose between first and sixth row
        i2 = randint(0, 5)
    else:
        # Bottom half so choose between first and twelfth row
        i2 = randint(0, 11)

    return i1, i2

def PrintMove(i, j):
    print('my move: ', chr(i + 65), j + 1)

# Decide what move to make based on current state of opponent's board and print it out
def ChooseAndPrintMove(Opponent):
    # Completely random strategy
    # Knowledge about opponent's board is completely ignored
    i1, i2 = RandomCoOrdinates()

    # Display move in letter+number grid reference
    print('my move: ', chr(i1 + 65), i2 + 1)
    return i1, i2

# Distribute the fleet onto your board
def DeployFleet(Player):
    ships = transform.raw_ships()

    for ship in ships:
        ship = transform.RandomTransform(ship)
        x, y = ValidPlacement(Player, ship)

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

def ValidPlacement(domain, ship):
    attempts = 0
    while True:
        if attempts > 10:
            raise RuntimeError('Could not find solution after multiple attempts')

        x, y = RandomCoOrdinates()

        if (x + len(ship)) > constants.BOARD_HEIGHT:
            continue

        if (y + len(ship[0])) > len(domain[x]):
            continue

        print ("doing some checking...")

        # collisions
        collision = False
        for row in domain[x:x+len(ship)]:
            print (row)

            if constants.OCCUPIED in row[y:y+len(ship[0])]:
                print ("collision found")
                collision = True

        if collision:
            attempts += 1
            continue

        # if clips outside edge?

        return x, y

def UpdateAndPrint(Player, Opponent, i1, i2):
    if (Player[i1][i2] == 2) or (Player[i1][i2] == 4):
        # They may (stupidly) hit the same square twice so we check for occupied or hit
        Player[i1][i2] = 4
        PrintBoards(Player, Opponent)
        print('Hit!')
    else:
        # You might like to keep track of where your opponent has missed, but here we just acknowledge it
        PrintBoards(Player, Opponent)
        print('Missed!')
    return Player

