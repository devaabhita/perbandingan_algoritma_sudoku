from datasets.sample_data import (
   sudoku_intermediate
)

from eksperimen import (
   run_experiment
)


def print_board(board):

   for i in range(9):

      if i % 3 == 0 and i != 0:
         print("-" * 25)

      for j in range(9):

         if j % 3 == 0 and j != 0:
               print("|", end=" ")

         print(board[i][j], end=" ")

      print()


def main():

   result = run_experiment(
      sudoku_intermediate
   )

   print("\nBACKTRACKING\n")

   print_board(
      result["bt_board"]
   )

   print("\nTime:",
         result["bt_time"])

   print("Calls:",
         result["bt_calls"])


   print("\nCONSTRAINT PROPAGATION\n")

   print_board(
      result["cp_board"]
   )

   print("\nTime:",
         result["cp_time"])

   print("Calls:",
         result["cp_calls"])


if __name__ == "__main__":
   main()