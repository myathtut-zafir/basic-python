game_list=[0,1,2]
game_on=True
def display_game(game_list):
    print("herer is current list: ")
    print(game_list)
def position_choice():
    choice="WRONG"
      
    while choice not in ['0','1','2']:
        choice=input("enter (0,1,2): ")
        if choice not in ['0','1','2']:
            print("not accept!")
    return int(choice)

def replacement_choice(game_list,position):
    user_placement=input("Type a string to place at position: ")
    game_list[position]=user_placement
    return game_list

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
    

while game_on:
    display_game(game_list)
    position=position_choice()
    game_list=replacement_choice(game_list,position)
    display_game(game_list)
    game_on=gameon_choice()
