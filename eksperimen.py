import time
import copy

from algoritma.backtracking import (
   solve_backtracking
)

from algoritma.constraint import (
   solve_cp
)


def run_experiment(board):

   # backtracking
   bt_board = copy.deepcopy(board)

   bt_counter = {
      "calls": 0
   }

   start = time.time()

   solve_backtracking(
      bt_board,
      bt_counter
   )

   bt_time = time.time() - start


   # constraint propagation
   cp_board = copy.deepcopy(board)

   cp_counter = {
      "calls": 0
   }

   start = time.time()

   solve_cp(
      cp_board,
      cp_counter
   )

   cp_time = time.time() - start


   return {

      "bt_time": bt_time,
      "bt_calls": bt_counter["calls"],
      "bt_board": bt_board,

      "cp_time": cp_time,
      "cp_calls": cp_counter["calls"],
      "cp_board": cp_board
   }