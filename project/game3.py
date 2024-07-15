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

# def position_choice():
#     choice="WRONG"
      
#     while choice not in ['0','1','2']:
#         choice=input("enter (0,1,2): ")
#         if choice not in ['0','1','2']:
#             print("not accept!")
#     return int(choice)

# def gameon_choice():
#     choice="WRONG"
#     while choice not in ['Y','N']:
#         choice=input("Keep playing (Y or n): ")
#         if choice not in ['0','1','2']:
#             print("Sorry I do not understand!")
            
#     if choice=='Y':
#         return True
#     else:
#         return False
    
def player_input():
    marker=''
    while  not (marker =='X' or marker=='O'):
        marker=input("Player1 choose1 X or O: ").upper()
    if marker=='X':
        return ('X','O')
    else:
        return  ('O','X')

def player_marker(board,marker,position):
    board[position]=marker
def win_check(board,mark):
    
# player_1,player_2=player_input()
# print(player_1)
# print(player_2)
