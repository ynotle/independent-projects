import os

board = {}
for i in range(42):
    board[i] = '  ' 

print(board)


def board_making():
    for row in range(6):
        for col in range(7):
            print(f"|{board[(row * 7)+col]}", end = "")
        print("|")
    print ("  1  2  3  4  5  6  7  ")

Player1 = True 
row_number = 5
#player one is 🔵
#player two is 🔴

def move():
    global Player1, row_number
    row_number = 5
    move = input("What's your move? ")
    
    if not move: 
        print("Not a valid move!")
        return 
    move = int(move)
    col_number = move - 1

    if not move in range(0,8):
        print("Not a valid move!")
        return 
    
    if check_col(col_number) >= 6:
        print("Column Full.")
        return


    row_number -= (1 * check_col(col_number))


    
    if check_row(row_number):
        row_number -= 1 
    
    move = row_number * 7 + col_number

    
    
    if check_board(move):
        if Player1:
            board[move] = "🔵"
            current_piece = "🔵"
            Player1 = False
            board_making()
            return move, col_number, Player1, current_piece, row_number
        else:
            board[move] = "🔴"
            current_piece = "🔴"
            Player1=True
            board_making()
            return move, col_number, Player1, current_piece, row_number
    else:
        print("This spot is already taken.")

def check_board(n):

    if board[n] == "  ":
        return True
    else:
        return False

def check_row(row_number):
    return all(board[i] in ("🔵","🔴") for i in range((row_number * 7), ((row_number * 7) + 7)))



def check_col(col_number):
    level_ticker = 0

    for i in range (col_number, 42, 7):
        if board[i] in ("🔵","🔴"):
            level_ticker +=1

    return level_ticker

def check_win(a, b):
    if a or b:
        
        return False
    else: 
        
        return True

def check_col_win(move, col_number,current_piece):
    together = 0 
    for i in range(col_number, 42, 7):

        if (board[i]) == current_piece:
            together += 1 
            if together ==4:
                print("YAY")
                return True
        else:
            together = 0
    return False
            
def check_row_win(move, row_number, current_piece):
    together = 0 
    for i in range((row_number*7),((row_number*7)+7)):
        if (board[i]) == current_piece:
            together += 1 
            if together ==4:
                print("YAY")
                return True
        else:
            together = 0
    return False

def check_diagnol_win(move_pos,row_number, col_number, current_piece):
    together = 0
    for i in range(move_pos-23,move_pos+25,8):
        if 0 <=i < 42:
            if board[i] == current_piece:
                print("yay")
        

    # for row_number in range(1,4):
    #     for col_number in range(1,4):
    #         if board[row_number * 7 + col_number] == current_piece:
    #             print("yay")
   
    # # row_number * 7 + col_number
    # for i in range((
        
    #     row_number * 7 + col_number
        
    #     ), )

    # move = row_number * 7 + col_number


Game_On = True
board_making()
while Game_On:
    move_pos, col_number, Player1, current_piece, row_number = move()
    
    check_col_win_result = check_col_win(move_pos, col_number, current_piece)
    check_row_win_result = check_row_win(move, row_number, current_piece)
    check_diagnol_win(move_pos,row_number, col_number, current_piece)
    Game_On = check_win(check_col_win_result, check_row_win_result)
     




    # os.system('clear')
    
    

