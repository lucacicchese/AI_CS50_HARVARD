"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    board_copy = copy.deepcopy(board)

    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            temp = board_copy[i][j] == X

            if board_copy[i][j] == X:
                countX = countX+1
            elif board_copy[i][j] == O:
                countO = countO+1

    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    board_copy = copy.deepcopy(board)

    action_set = set()
    for i in range(3):
        for j in range(3):
            if board_copy[i][j] == EMPTY:
                t = (i, j)
                action_set.add(t)
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    possible_actions = actions(board)
    if action in possible_actions:
        new_board[action[0]][action[1]] = player(board)
        return new_board

    else:
        raise Exception('Invalid Action')



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_board = board
    for i in range(3):

        # Columns
        if (win_board[0][i] == win_board[1][i] and win_board[2][i] == win_board[1][i]) and (win_board[0][i] != EMPTY):
            return win_board[0][i]

        # Rows
        if (win_board[i][0] == win_board[i][1] and win_board[i][2] == win_board[i][1]) and (win_board[i][0] != EMPTY):
            return win_board[i][0]

        # Diagonals
        if (win_board[0][0]== win_board[1][1] and win_board[2][2] == win_board[1][1]) and (win_board[0][0] != EMPTY):
            return win_board[0][0]

        if (win_board[0][2] == win_board[1][1] and win_board[2][0] == win_board[1][1]) and (win_board[0][2] != EMPTY):
            return win_board[0][2]

        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win is not None:
        if win == X:
            return 1
        elif win == O:
            return -1
        else:
            return 0
    else:
        return 0

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 2000
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -2000
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_action = None

    if terminal(board):
        return None

    if player(board) == X:
        best_until_now = -3000
        for action in actions(board):
            score = max_value(result(board, action))

            if score > best_until_now:
                best_until_now = score
                best_action = action
    else:
        best_until_now = 3000
        for action in actions(board):
            score = min_value(result(board, action))

            if score < best_until_now:
                best_until_now = score
                best_action = action

    return best_action

