from game_logic import *

# Main
while True:
    Player, Opponent = InitBoards()

    try:
        Player = DeployFleet(Player, True)
    except RuntimeError as e:
        continue

    break

PrintBoards(Player, Opponent)
entry = input('Do I take the first move? (y/n) ')
if entry.lower() == 'y':
    # Make a move by looking at the opponent's board
    i1, i2 = ChooseAndPrintMove(Opponent)
    # Ask the user to enter the outcome
    Outcome = GetOutcome()
    # Update our knowledge of the opponent's board
    Opponent[i1][i2] = Outcome
    # Show the current board state
    PrintBoards(Player, Opponent)
# No-one has won yet
PlayerWins = 0
OpponentWins = 0
# Suggested game loop:
while not (PlayerWins or OpponentWins):
    # Opponent's turn
    i1, i2 = GetMove()
    Player = UpdateAndPrint(Player, Opponent, i1, i2)
    OpponentWins = CheckWinner(Player)

    if not OpponentWins:
    # My turn
        i1, i2 = ChooseAndPrintMove(Opponent)
        Outcome = GetOutcome()
        Opponent[i1][i2] = Outcome
        PrintBoards(Player, Opponent)
        OpponentWins = CheckWinner(Player)
if PlayerWins:
    print('Woohoo! I win')
else:
    print('Boo! You win')