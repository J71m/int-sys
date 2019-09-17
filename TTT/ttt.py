board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def print_current_board():
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=' ')
        print()
    print()

def is_tie():
    for row in board:
        for col in row:
            if isinstance(col, int):
                return False
    return True
        
def check_if_empty(choice):
    choice = choice - 1
    row, col = (choice//3, choice % 3)
    if board[row][col] != "X" and board[row][col] != "O":
        return True
    else:
        return False

def update_board(player, choice):
    choice = choice - 1
    row, col = (choice//3, choice % 3)
    board[row][col] = player
    
def win_indices(n):
    for r in range(n):
        yield [(r, c) for c in range(n)]
    for c in range(n):
        yield [(r, c) for r in range(n)]
    yield [(i, i) for i in range(n)]
    yield [(i, n - 1 - i) for i in range(n)]


def is_winner(decorator):
    n = len(board)
    for indexes in win_indices(n):
        if all(board[r][c] == decorator for r, c in indexes):
            return True
    return False

def next_choice_win(player_icon):
    board_default = list(range(1,10))
    diag1 = [board[0][0],board[1][1],board[2][2]]
    diag2 =[board[0][2],board[1][1],board[2][0]]
    diag1_counter = 0
    diag2_counter = 0
    for row in range(3):
        if diag1[row] == player_icon:
            diag1_counter += 1
            if diag1_counter == 2:
                for next_win in range(3):
                    if isinstance(diag1[next_win], int):
                        return diag1[next_win]
        if diag2[row] == player_icon:
            diag2_counter += 1
            if diag2_counter == 2:
                for next_win in range(3):
                    if isinstance(diag2[next_win], int):
                        return diag2[next_win]
        col_counter = 0
        row_counter = 0
        
        for col in range(3):
            if board[row][col] == player_icon:
                row_counter += 1
                if row_counter == 2:
                    for next_win in range(3):
                        if isinstance(board[row][next_win], int):
                            return board[row][next_win]
            if board[col][row] == player_icon:
                col_counter += 1
                if col_counter == 2:
                    for next_win in range(3):
                        if isinstance(board[next_win][row], int):
                            return board[next_win][row]

    
    return False

def ai_win_next():
    ai_next_move = next_choice_win("O")
    return ai_next_move

def ai_not_lose_next():
    ai_next_move = next_choice_win("X")
    return ai_next_move

def ai_first_empty():
    for row in range(3):
        for col in range(3):
             if board[row][col] != "X" and board[row][col] != "O":
                 return board[row][col]

def ai_next_move():
    next_win_move = ai_win_next()
    next__not_lose_move = ai_not_lose_next()
    if  next_win_move!= False:
        return next_win_move
    elif next__not_lose_move != False:
        return next__not_lose_move
    else:
        return ai_first_empty()


def main():
    print_current_board()
    game = True
    while game:
        player_x_choice = True
        while player_x_choice:
            player_x = int(input("Player X: "))
            if check_if_empty(player_x):    
                update_board("X", player_x)
                player_x_choice = False
            else:
                print("Invalid choice, try again!")
        print_current_board()
        if is_winner("X"):
            print("X won")
            game = False
            break
        elif is_tie():
            print("Tie")
            game = False
            break
        
        player_o_choice = True
        while player_o_choice:    
            player_o = int(ai_next_move())
            if check_if_empty(player_o):
                print("Player O (AI):", player_o)
                update_board("O", player_o)
                player_o_choice = False
            else:
                print("Invalid choice, try again!")
        print_current_board()
        if is_winner("O"):
            print("O won (AI)")
            game = False
            break
        elif is_tie():
            print("Tie")
            game = False
            break
        
main()
