# st = 'Print only the words that start with s in this sentence'
# for str in st:
#     if str=='s':
#         print(str)

# for num in range(0,10):
#     if(num%2==0):
#         print(num)

# myNum=[x for x in range(1,50)if x%3==0]
# print(myNum)

# for index, value in enumerate(st):
#     if index%2==0:
#         print(value)


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
        
st = 'Create a list of the first letters of every word in this string'
x = st.split()
myList=[]
for str in x:
    first_letters = ''.join([i[0] for i in str.split()]) 
    myList.append(first_letters)

print(myList)