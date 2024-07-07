def say_hello():
    print("hi")

say_hello()

def say_hello_two(name="mgmmg"):
    print(f"hi {name} ")

say_hello_two()

def num(num1,num2):
    return num1+num2

print(num(1,2))

def even_check(number):
    if number%2==0:
        return True
    else:
        pass

print(even_check(21))

work_hours=[('Abby',100),('Billy',400),('cassie',800)]
def employee(work_hours):
     current_max=0
     employee_of_month=''
     for employee,hours in work_hours:
         if hours>current_max:
             current_max=hours
             employee_of_month=employee
         else:
             pass
         
     return (employee_of_month,current_max)
 
print(employee(work_hours))
name,hour=employee(work_hours) 
print(name)
print(hour)