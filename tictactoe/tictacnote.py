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
    else:
        turn = (board.count(EMPTY))%2
        if turn == 1:
            return(X)
        return(O)

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
                return 'N'
    else:
        actions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        boards = [val for sublist in board for val in sublist]
        for ind, val in enumerate(boards):
            if val != EMPTY:
                del actions[ind]
        return(set(actions))

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)
    if board2[action[0]][action[1]] != EMPTY:
        raise ValueError ('move not possible')
    else:
        board2[action[0]][action[1]]= player(board)
        return(board2)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    player2 = player(board)
    
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
    if [player2, player2, player2] in grid:
        return player2
    else:
        num = board.count(EMPTY)
        if num == 0:
            return(None)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or actions(board)== set():
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
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
    if terminal(board):
        return None

    def MaxValue(board):
        if terminal(board):
            return(utility(board), None)
        v = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
        optimal = []
        for action in actions(board):
            v = max(v, MinValue(result(board, action)[0]))
            print(v)
            if v > -1:
                optimal.append(action)
        print(v, optimal)
        return (v, optimal)
    
    
    def MinValue(board):
        if terminal(board):
            return(utility(board), None)
        v = (math.factorial(9)/(math.factorial(9-2)/12))
        optimal = []
        for action in actions(board):
            v = min(v, MaxValue(result(board, action)[0]))
            if v < 1:
                optimal.append(action)
        return (v, optimal)

    if player(board) == X:
        val = MaxValue(board)
        print("Final max_value: " +str(val))

        return val[1][0]
    else:
        val = MinValue(board)
        print("Final min_value: " +str(val))
        return val[1][0]
        
        
        
        
        
    alpha = (math.factorial(9)/(math.factorial(9-2)/12))
    beta = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
    
def minimax(actions(board), depth=0, alpha, beta, player(board)):
        if depth == 0 or terminal(board):
            return(utility(board), None)
        
        if player(board) == X:
            maxEval = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
            for action in actions(board):
                evals = minimax(action, depth -=1, alpha, beta, player(board))
                maxEval = max(maxEval, evals)
                alpha = max(alpha, evals)
                if beta <= alpha:
                    break
            return maxEval
        
        else:
            minEval = (math.factorial(9)/(math.factorial(9-2)/12))
            for action in actions(board):
                evals= minimax(action, depth -=1, alpha, beta, player(board))
                beta = min(beta, evals)
                beta = max(beta, evals)
                if beta <= alpha:
                    break
            return minEval
            

#File "/Users/Koala/Downloads/tictactoe/tictactoe.py", line 165, in minimax
    #return val[1][0]
#IndexError: list index out of range

    alpha = (math.factorial(9)/(math.factorial(9-2)/12))
    beta = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
        
    if player(board) == X:
        val = MaxValue(board, alpha, beta)
        return val[1][0]
    else:
        val = MinValue(board, alpha, beta)
        return val[1][0]


def MaxValue(board, alpha, beta):
    if terminal(board):
        return(utility(board), None)
    v = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
    optimal = []
    for action in actions(board):
        v = max(v, MaxValue(result(board, action), alpha, beta)[0])
        alpha = max(alpha, v)
        if v > -1:
            if beta <= alpha:
                break
            optimal.append(action)
    return (v, optimal)


def MinValue(board, alpha, beta):
    if terminal(board):
        return(utility(board), None)
    v = (math.factorial(9)/(math.factorial(9-2)/12))
    optimal = []
    for action in actions(board):
        v = min(v, MaxValue(result(board, action), alpha, beta)[0])
        beta = min(beta, v)
        if v < 1:
            if beta <= alpha:
                break
            optimal.append(action)
    return (v, optimal)
    
    
    
    
    
    def MaxValue(board, alpha, beta):
    if terminal(board):
        return(utility(board), None)
    alpha = (math.factorial(9)/(math.factorial(9-2)/12))
    beta = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
    optimal = []
    for action in actions(board):
        alpha = max(alpha, MinValue(result(board, action), alpha, beta)[1])
        if beta <= alpha:
            break
        else:    
            optimal.append(action)
    print (beta, optimal)
    return (alpha, optimal)


def MinValue(board, alpha, beta):
    if terminal(board):
        return(utility(board), None)
    alpha = (math.factorial(9)/(math.factorial(9-2)/12))
    beta = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
    optimal = []
    for action in actions(board):
        beta = min(beta, MaxValue(result(board, action), alpha, beta)[1])
        if beta <= alpha:
            break
        else:
            optimal.append(action)
    print (beta, optimal)
    return (beta, optimal)
    
    
def minimax_val(board,maxPlayer,alpha,beta):

    if terminal(board):
        return utility(board)
    
    elif maxPlayer:
        best = ((math.factorial(9)/(math.factorial(9-2)/12))*-1)
        for action in actions(board):
            value = minimax_val(result(board, action), False, alpha, beta)
            best= max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    
    else:
        best = (math.factorial(9)/(math.factorial(9-2)/12))
        for action in actions(board):
            value = minimax_val(result(board, action), True, alpha, beta)
            best= min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    else:
        
        best_action = (-1, -1)
        if player(board) == X:
            max_value = -250000
            for action in actions(board):
                value = minimax_val(result(board, action), True, -250000, 250000)
                if value > max_value:
                    max_value = value
                    best_action = action
            return best_action
        
        elif player(board) == O:
            min_value = 250000
            for action in actions(board):
                value = minimax_val(result(board, action), False, -250000, 250000)
                if value < min_value:
                    min_value = value
                    best_action = action
            return best_action
