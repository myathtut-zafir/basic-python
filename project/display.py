def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

def user_choice():
    choice="WRONG"
    acceptable_range=range(0,10)
    within_range=False
    
    while choice.isdigit()==False or within_range==False:
        choice=input("enter 0-10: ")
        if choice.isdigit()==False:
            print('Sry nor digit!')
            
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print("not accept!")
                within_range=False
    return int(choice)

row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
row2[1]='X'
display(row1,row2,row3)
# result=input("pls enter value: ")
# print(result)
user_choice()
