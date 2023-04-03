from board import Board
import numpy as np


if __name__ == "__main__":

    init_state = np.array([
        [1,1,0],
        [0,1,0],
        [0,0,1]
    ])
    expected_next_state = np.array([
        [1,1,0],
        [1,1,1],
        [0,0,0]
    ])

    initBoard = Board(3,3)
    expBoard = Board(3,3)
    initBoard.board = init_state
    expBoard.board = expected_next_state

    initBoard.next_step()

    if np.array_equal(initBoard.board, expBoard.board):
        print ("PASSED 1")
    else:
        print ("FAILED 1!")
        print ("Expected:")
        print (expBoard.board)
        print ("Actual:")
        print (initBoard.board)
