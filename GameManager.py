import constants
import os
import game_logic
from Attack import HuntType, Attack

class GameManager:
    def __init__(self):
        self.set_up_boards()
        self.attacker = Attack([], HuntType.LINES, self)
        self.print_boards()

        first_move = input('Do I take the first move? (y/n) ')

        if first_move.lower() == 'y':
            self.do_player_attack()

        self.do_opponent_attack()
        self.do_player_attack()

    def do_player_attack(self):
        self.attacker.begin_attacking()

    def after_attack_event(self):
        self.print_boards()

        if game_logic.CheckWinner(self.attacker.view_of_opponent):
            print('Woohoo! I win')
            return

        self.do_opponent_attack()

        if game_logic.CheckWinner(self.player):
            # you check your own board to see if the opponent has won
            print('Boo! You win')

    def attack_from_below(self, attack):
        """
        called from the attack class, should return the result
        """

        i, j = attack[0]
        self.print_move(i, j)
        outcome = self.get_outcome()

        return outcome

    def do_opponent_attack(self):
        Player = self.player
        i1, i2 = self.get_opponent_move()

        if (Player[i1][i2] == 2) or (Player[i1][i2] == 4):
            # They may (stupidly) hit the same square twice so we check for occupied or hit
            Player[i1][i2] = 4
            print('Hit!')
        else:
            print('Missed!')

        # self.print_boards()

    def set_up_boards(self):
        while True:
            self.player, self.opponent = game_logic.InitBoards()

            try:
                self.player = game_logic.DeployFleet(self.player, False)
            except RuntimeError as e:
                continue

            break

    def get_outcome(self):
        while True:
            entry = input('Outcome? (h/m) ')

            if entry.lower() == 'h':
                return True
            elif entry.lower() == 'm':
                return False
            else:
                print("Invalid input: must enter h (hit) or m (miss)")

    @staticmethod
    def print_move(i, j):
        print('my move: ', chr(i + 65), j + 1)

    @staticmethod
    def get_opponent_move():
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

    def print_boards(self):
        """
        Clear the screen and draw the two boards side by side
        """

        Player = self.player
        Opponent = self.attacker.view_of_opponent

        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print board labels
        print(' ' * 10, 'PLAYER', ' ' * 30, 'OPPONENT')
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        for x in range(6):
            print(letters[x], "  ".join(map(GameManager.display_char, Player[x])), " " * 18, "| ",
                  "  ".join(map(GameManager.display_char, Opponent[x])))
        for x in range(6, 12):
            print(letters[x], "  ".join(map(GameManager.display_char, Player[x])), " | ", "  ".join(map(GameManager.display_char, Opponent[x])))
        print(" ", "  ".join(map(str, range(1, 10))), " 10 11 12", "  ", "  ".join(map(str, range(1, 10))), " 10 11 12")

    @staticmethod
    def display_char(x):
        """
        Mapping function that determines how each square state is displayed
        """

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

class IterateGameManager(GameManager):
    def __init__(self, config):
        self.set_up_boards()

        if config == []:
            enemy_config = self.player
        else:
            enemy_config = config

        self.attacker = Attack(enemy_config, HuntType.LINES, self)
        self.do_player_attack()

    def do_player_attack(self):
        self.attacker.begin_attacking()

    def after_attack_event(self):
        pass

    def attack_from_below(self, attack):
        """
        called from the attack class, should return the result
        """

        i, j = attack[0]

        return self.attacker.enemy_config[i][j] == constants.OCCUPIED