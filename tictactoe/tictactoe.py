"""
Tic Tac Toe Player
"""

import math

import copy

X = "X"
O = "O"
EMPTY = '-'


    
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
    if terminal(board):
            return ('M')
    step = []
    for i in board:
        m =  (i.count('X') + i.count('O'))
        step.append(m)
    turn = sum(step)%2
    if turn == 0:
        return X
    else:
        return O
            
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
                return 'N'
    else:
        posact = set()
        for i in range(3):
            for c in range(3):
                if board[i][c] == EMPTY:
                    val = (i, c)
                    posact.add(val)
        return posact



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)
    if board2[action[0]][action[1]] != '-':
        raise ValueError ('move not possible')
    else:
        board2[action[0]][action[1]]= player(board)
        return(board2)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    try:
        player = player(board)
    except:
        step=[]
        for i in board:
            m =  (i.count('X') + i.count('O'))
            step.append(m)
        turn = sum(step)%2
        if turn == 0:
            player = X
        else: 
            player = O
    
    grid = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]],
        ]
    if [player, player, player] in grid:
        return player
    else:
        step1=[]
        for c in board:
            m2 =  c.count(EMPTY) 
            step1.append(m2)
        turn2 = sum(step1)
        if turn2 < 1:
            return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    step3=[]
    for c in board:
        m3 =  c.count(EMPTY) 
        step3.append(m3)
    turn3 = sum(step3)
    if turn3 < 1:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if terminal(board):
        return None

    if player(board) == X:
        val = MaxValue(board)
        return val[1][0]
    else:
        val = MinValue(board)
        return val[1][0]


def MaxValue(board):
    if terminal(board):
        return(utility(board), None)
    v = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
    optimal = []
    for action in actions(board):
        v = max(v, MinValue(result(board, action))[0])
        if v > -1:
            optimal.append(action)
    return (v, optimal)


def MinValue(board):
    if terminal(board):
        return(utility(board), None)
    v = (math.factorial(9)/(math.factorial(9-2)/12))
    optimal = []
    for action in actions(board):
        v = min(v, MaxValue(result(board, action))[0])
        if v < 1:
            optimal.append(action)
    return (v, optimal)