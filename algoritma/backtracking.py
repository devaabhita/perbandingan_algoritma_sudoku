from utils.sudoku_utils import find_empty, is_valid


def solve_backtracking(board, counter):

   empty = find_empty(board)

   if not empty:
      return True

   row, col = empty

   for num in range(1, 10):

      counter["calls"] += 1

      if is_valid(board, row, col, num):

         board[row][col] = num

         if solve_backtracking(board, counter):
               return True

         board[row][col] = 0

   return False