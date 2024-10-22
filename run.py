import random



HIT_CHAR = 'x'
MISS_CHAR = 'o'
BLANK_CHAR = '.'
VERTICAL = 'v'
HORIZONTAL = 'h'
MAX_MISSES = 20
SHIP_SIZES = {
    "carrier": 5,
    "battleship": 4,
    "shadwell": 3,
    "submarine": 3,
    "destroyer": 2, 
}

NUM_ROWS = 10
NUM_COLS = 10
ROW_IDX = 0
COL_IDX = 1
MIN_ROW_LABEL = 'A'
MAX_ROW_LABEL = 'J'

def get_random_position():
    """Generates a random location on a board of NUM_ROWS x NUM_COLS."""

    row_choice = chr(
                    random.choice(
                        range(
                            ord(MIN_ROW_LABEL),
                            ord(MIN_ROW_LABEL) + NUM_ROWS
                        )
                    )
    )

    col_choice = random.randint(0, NUM_COLS - 1)

    return (row_choice, col_choice)

def play_battleship():
    """Controls flow of Battleship games including display of
    welcome and goodbye messages.

    :return: None
    """

    print("Let's Play Battleship!\n")

    game_ower = False

    while not game_ower:

        game = Game()
        game.display_board()

    while not game.is_complete():
            pos = game.get_guess()
            result = game.check_guess(pos)
            game.update_game(result, pos)
            game.display_board()
    
    game_over = end_program()

print("Goodbye.")  

class Ship:
     def __init__(self, name, start_position, orientation):

        self.name = name
        num_positions = SHIP_SIZES[name]
        self.positions = {}
        self.sunk = False

        for pos in range(num_positions):
            if orientation == VERTICAL:
                vertical_position, horizontal_position = start_position
                self.positions[(chr(ord(vertical_position) + pos), horizontal_position)] = False

            elif orientation == HORIZONTAL:
                vertical_position, horizontal_position = start_position
                self.positions[(vertical_position, horizontal_position + pos)] = False

class Game:


    _ship_types = ["carrier", "battleship", "shadwell", "submarine", "destroyer"]

    def display_board(self):

        print()
        print("  " + ' '.join('{}'.format(i) for i in range(len(self.board))))
        for row_label in self.board.keys():
            print('{} '.format(row_label) + ' '.join(self.board[row_label]))
        print()

    def __init__(self, max_misses = MAX_MISSES):

        self.max_misses = MAX_MISSES
        self.ships = []
        self.guesses = []
        self.board = []
        self.initialize_board()
        self.create_and_place_ships()

    def update_game(self, guess_status, position):

        row, column = position

        if guess_status == True and self.board[row][column] == BLANK_CHAR:
            self.board[row][column] = HIT_CHAR

        elif guess_status == False and self.board[row][column] ==BLANK_CHAR:
            self.board[row][column] = MISS_CHAR

        if guess_status == False:
            self-guesses.append(position)

    def is_complete(self):

        if len(self.guesses) == self.max_misses:
            print("SORRY! NO GUESSES LEFT.")
            return True

            ships_sunk = []

        for ship in self.ships:
            ships_sunk.append(ship.sunk)
        
