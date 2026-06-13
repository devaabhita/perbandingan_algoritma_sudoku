def find_empty(board):
   for i in range(9):
      for j in range(9):
         if board[i][j] == 0:
               return i, j
   return None


def is_valid(board, row, col, num):

   if num in board[row]:
      return False

   for i in range(9):
      if board[i][col] == num:
         return False

   start_row = (row // 3) * 3
   start_col = (col // 3) * 3

   for i in range(3):
      for j in range(3):
         if board[start_row+i][start_col+j] == num:
               return False

   return True


def get_possible_values(board, row, col):

   possible = set(range(1, 10))

   possible -= set(board[row])

   possible -= {
      board[i][col]
      for i in range(9)
   }

   start_row = (row // 3) * 3
   start_col = (col // 3) * 3

   for i in range(3):
      for j in range(3):
         possible.discard(
               board[start_row+i][start_col+j]
         )

   return possible