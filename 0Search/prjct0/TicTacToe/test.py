import tictactoe as tic

if __name__ == '__main__':
    board = tic.initial_state()
    print(board)

    new_board = board
    t = (0, 0)
    new_board = tic.result(new_board, t)
    t = (1, 0)
    new_board = tic.result(new_board, t)
    t = (0, 1)
    new_board = tic.result(new_board, t)
    t = (1, 2)
    new_board = tic.result(new_board, t)
    t = (0, 2)
    new_board = tic.result(new_board, t)

    print(new_board)
    print(tic.winner(new_board))
    0. Search / prjct0 / TicTacToe
