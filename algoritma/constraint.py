from utils.sudoku_utils import (
   find_empty,
   get_possible_values
)


def solve_cp(board, counter):

   empty = find_empty(board)

   if not empty:
      return True

   row, col = empty

   domain = get_possible_values(
      board,
      row,
      col
   )

   for num in domain:

      counter["calls"] += 1

      board[row][col] = num

      if solve_cp(board, counter):
         return True

      board[row][col] = 0

   return False