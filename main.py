import random
class GameBoard:
  def __init__(self, board):
    self.board = board

  def get_letters_to_numbers():
    letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, }
    return letters_to_numbers

  def print_board(self):
      print("  A B C D E F ")
      print("  +-+-+-+-+-+")
      row_number = 1
      for row in self.board:
          print("%d|%s|" % (row_number, "|".join(row)))
          row_number += 1
class Battleship:
  def __init__(self, board):
    self.board = board

  def create_ships(self):
    for i in range(2):
      self.x_row, self.y_column = random.randint(0,5), random.randint(0, 5)
      while self.board[self.x_row][self.y_column] == "X":
        self.x_row, self.y_column = random.randint(0, 5), random.randint(0, 5)
      self.board[self.x_row][self.y_column] = "X"
    return self.board

  def get_user_input(self):
    try:
      x_row = input("Enter the row of the ship: ")
      while x_row not in '123456':
          print('open your eyes and choose wisely')
          x_row = input("now do it again you blind: ")

      y_column = input("Enter the column letter of the ship: ").upper()
      while y_column not in "ABCDEF":
          print('open your eyes and choose wisely')
          y_column = input("now stop playing around and choose the letter: ").upper()
      return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
    except ValueError and KeyError:
      print("stop playing around")
      return self.get_user_input()

  def count_hit_ships(self):
    hit_ships = 0
    for row in self.board:
      for column in row:
        if column == "X":
          hit_ships += 1
    return hit_ships

def RunGame(): 
  computer_board = GameBoard([[" "] * 6 for i in range(6)])
  user_guess_board = GameBoard([[" "] * 6 for i in range(6)])
  Battleship.create_ships(computer_board)
 
  turns = 4
  while turns > 0:
    GameBoard.print_board(user_guess_board)
   
    user_x_row, user_y_column = Battleship.get_user_input(object)
   
    while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
      print("been there ,done that")
      user_x_row, user_y_column = Battleship.get_user_input(object)
   
    if computer_board.board[user_x_row][user_y_column] == "X":
      print("You sunk 1 of my battleship!,now you have done it !")
      user_guess_board.board[user_x_row][user_y_column] = "X"
    else:
      print("its my lucky day!")
      user_guess_board.board[user_x_row][user_y_column] = "-"
   
    if Battleship.count_hit_ships(user_guess_board) == 5:
      print("you know something its just my bad luck , congrats on your winning !")
      break
    else:
      turns -= 1
      print(f"You have {turns} turns remaining")
      if turns == 0:
        print("hahahahaha.........who is the boss?, its me.........sorry mate you lost")
        GameBoard.print_board(user_guess_board)
        break

if __name__ == '__main__':
  RunGame()
