import random

# Singleton Design Pattern for GameSettings
class GameSettings:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameSettings, cls).__new__(cls)
            cls._instance.ships_count = 2
            cls._instance.board_size = 6
        return cls._instance

# Encapsulation, Inheritance, and Abstraction
class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[" "] * size for _ in range(size)]

    def print_board(self):
        print("  " + " ".join([chr(i) for i in range(65, 65 + self.size)]))
        print("  " + "+-" * self.size + "+")
        for i, row in enumerate(self.board):
            print(f"{i+1}|{'|'.join(row)}|")

    @staticmethod
    def get_letters_to_numbers():
        return {chr(i): i - 65 for i in range(65, 65 + 6)}

# Inheritance
class GameBoard(Board):
    pass

class GuessBoard(Board):
    pass

class ShipPlacementStrategy:
    def place_ships(self, board, count):
        raise NotImplementedError("This method should be overridden.")

class RandomShipPlacement(ShipPlacementStrategy):
    def place_ships(self, board, count):
        for _ in range(count):
            x_row, y_column = random.randint(0, board.size - 1), random.randint(0, board.size - 1)
            while board.board[x_row][y_column] == "X":
                x_row, y_column = random.randint(0, board.size - 1), random.randint(0, board.size - 1)
            board.board[x_row][y_column] = "X"

class BattleshipGame:
    def __init__(self, placement_strategy):
        self.settings = GameSettings()
        self.computer_board = GameBoard(self.settings.board_size)
        self.user_guess_board = GuessBoard(self.settings.board_size)
        self.placement_strategy = placement_strategy
        self.placement_strategy.place_ships(self.computer_board, self.settings.ships_count)

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '123456':
                print('Open your eyes and choose wisely')
                x_row = input("Enter the row of the ship again: ")

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEF":
                print('Open your eyes and choose wisely')
                y_column = input("Enter the column letter again: ").upper()
            return int(x_row) - 1, Board.get_letters_to_numbers()[y_column]
        except (ValueError, KeyError):
            print("Invalid input, try again.")
            return self.get_user_input()

    def count_hit_ships(self, board):
        return sum(row.count("X") for row in board.board)

    def run_game(self):
        turns = 8
        while turns > 0:
            self.user_guess_board.print_board()
            user_x_row, user_y_column = self.get_user_input()

            while self.user_guess_board.board[user_x_row][user_y_column] in ["-", "X"]:
                print("You've already guessed that location.")
                user_x_row, user_y_column = self.get_user_input()

            if self.computer_board.board[user_x_row][user_y_column] == "X":
                print("You sunk 1 of my battleships!")
                self.user_guess_board.board[user_x_row][user_y_column] = "X"
            else:
                print("It's my lucky day!")
                self.user_guess_board.board[user_x_row][user_y_column] = "-"

            if self.count_hit_ships(self.user_guess_board) == self.settings.ships_count:
                print("Congratulations, you win!")
                break
            else:
                turns -= 1
                print(f"You have {turns} turns remaining")
                if turns == 0:
                    print("Game over! You lost.")
                    self.user_guess_board.print_board()
                    break

if __name__ == '__main__':
    # Factory Method Design Pattern for creating a BattleshipGame with RandomShipPlacement
    def game_factory():
        return BattleshipGame(RandomShipPlacement())

    game = game_factory()
    game.run_game()
