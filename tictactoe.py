"""
Unbeatable Tic-Tac-Toe Ai

At best you can tie

Ai uses minimax search algorithm for optimizing its movements

Sometimes Ai decides to mock with its opponent. Still won't lose though
"""

import copy

X = "X"
O = "O"

board = [[" " for _ in range(3)] for _ in range(3)]


def main():
    '''
    Main game loop
    '''
    while True:
        print_board(board)
        if player(board) == "X":
            i, j = get_move()
        else:
            print("Ai is thinking")
            art_int = minimax(board)
            i = art_int[0]
            j = art_int[1]
        board[i][j] = player(board)
        if terminal(board):
            if winner(board) is not None:
                print_board(board)
                print(f"{'Ai' if winner(board) == 'O' else 'user'} won!")
                break
            print_board(board)
            print("Tie!")
            break


def print_board(lis):
    '''
    Prints board.
    '''
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(lis[i][j], "|", end=" ")
        print("\n-------------")


def get_move():
    '''
    Gets move from the user and validates.
    '''
    while True:
        try:
            inp = input("Input your move as i,j (1 indexed): ")
            i, j = inp.split(",")
            i = int(i) - 1
            j = int(j) - 1

            if 0 <= i <= 2 and 0 <= j <= 2 and board[i][j] == " ":
                return (i, j)
            raise ValueError
        except ValueError:
            print("Wrong input")


def player(lis):
    '''
    Returns which players turn at given state.
    '''
    count = 0
    for row in lis:
        for _ in row:
            if _ == " ":
                count += 1
    if count % 2 == 1:
        return X
    return O


def actions(lis):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = -1
    j = -1
    valid = set()
    for row in lis:
        i += 1
        for col in row:
            j += 1
            j = j % 3
            if col == " ":
                crd = (i, j)
                valid.add(crd)
    return valid


def result(lis, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    cpyboard = copy.deepcopy(lis)
    x, y = action
    if cpyboard[x][y] == " ":
        cpyboard[x][y] = player(lis)
    else:
        raise ValueError("Invalid move")
    return cpyboard


def winner(lis):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if lis[i][0] == lis[i][1] == lis[i][2] != " ":
            return lis[i][0]
    for j in range(3):
        if lis[0][j] == lis[1][j] == lis[2][j] != " ":
            return lis[0][j]
    if lis[0][0] == lis[1][1] == lis[2][2] != " ":
        return lis[0][0]
    if lis[0][2] == lis[1][1] == lis[2][0] != " ":
        return lis[0][2]
    return None


def terminal(lis):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(lis) is not None:
        return True
    for row in lis:
        for i in row:
            if i == " ":
                return False
    return True


def utility(lis):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(lis) == "X":
        return 1
    elif winner(lis) == "O":
        return -1
    else:
        return 0


def minimax(lis):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(lis)

    if turn == X:
        c = float("-inf")
        for action in actions(lis):
            v = min_value(result(lis, action))
            if v > c:
                c = v
                reslt = action
                if c == 1:
                    return reslt
        return reslt
    elif turn == O:
        c = float("inf")
        for action in actions(lis):
            v = max_value(result(lis, action))
            if v < c:
                c = v
                reslt = action
                if c == -1:
                    return reslt
        return reslt
    return None

def max_value(lis):
    '''
    Returns maximum value for given board.
    Will be used for recursion.
    '''
    v = float("-inf")
    if terminal(lis):
        return utility(lis)
    for action in actions(lis):
        v = max(v, min_value(result(lis, action)))
    return v


def min_value(lis):
    '''
    Returns minimum value for given board.
    Will be used for recursion.
    '''
    v = float("inf")
    if terminal(lis):
        return utility(lis)
    for action in actions(lis):
        v = min(v, max_value(result(lis, action)))
    return v


if __name__ == "__main__":
    main()
