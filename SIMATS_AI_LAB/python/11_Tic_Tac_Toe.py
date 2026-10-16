board = [' '] * 9
win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def check_win(player):
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

moves = [(0, 'X'), (4, 'O'), (1, 'X'), (3, 'O'), (2, 'X')]

for position, player in moves:
    board[position] = player
    if check_win(player):
        print(board[0], '|', board[1], '|', board[2])
        print(board[3], '|', board[4], '|', board[5])
        print(board[6], '|', board[7], '|', board[8])
        print('Player', player, 'Wins!')
        break
