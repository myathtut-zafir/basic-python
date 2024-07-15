def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Initialize the board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Display the initial empty board
# print_board(board)

def position_choice():
    choice="WRONG"
      
    while choice not in ['0','1','2']:
        choice=input("enter (0,1,2): ")
        if choice not in ['0','1','2']:
            print("not accept!")
    return int(choice)

def gameon_choice():
    choice="WRONG"
    while choice not in ['Y','N']:
        choice=input("Keep playing (Y or n): ")
        if choice not in ['0','1','2']:
            print("Sorry I do not understand!")
            
    if choice=='Y':
        return True
    else:
        return False
    
def replacement_choice(game_list,line,position):
    user_placement=input("Type a string to place at position: ")
    if user_placement in ['X','O']:
        game_list[line][position]=user_placement
        return game_list
    return game_list

def check_winner(board):
    
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    # Check for a tie
    if all(cell != ' ' for row in board for cell in row):
        return 'Tie'
    
    # If no winner and no tie, return None
    return None
game_on=True
while game_on:
    print_board(board)
    line=position_choice()
    position=position_choice()
    board=replacement_choice(board,line,position)
    
    result = check_winner(board)
if result == 'Tie':
    print("The game is tied!")
elif result:
    print(f"Player {result} has won!")
else:
    print("The game is still ongoing.")
    
    print_board(board)
    game_on=gameon_choice()
