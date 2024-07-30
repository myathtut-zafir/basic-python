def division():
   x = 5
   y = 0
   z = x/y
try:
    result=division()
except ZeroDivisionError:
    print("error!")
finally:
    print("All done")


def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)

