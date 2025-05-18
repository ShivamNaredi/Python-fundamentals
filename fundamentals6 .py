# We will Disxuss about funtions in this with few small projects realted to funtions 
#Block of statment 
#Used to reduce the redundant lines of code in the program
#there are 2 types of funtions 
#Built-in and User defined funtions 
def sum(a , b):
    sum = a+b
    print(sum)
sum(2 , 10)    
sum(12,123)

def reverse(str):
    new_string = 0
    while str >0:
        random = str % 10
        str = str // 10
        new_string = new_string * 10 + random 
    print(new_string)

reverse(24234234)     
        
def sumus(str):
    digit = 0
    while str >0:
        random = str %10        
        str = str // 10
        digit = digit + random
    print(digit)
sumus(1232424131)    
sumus(2345432)    
reverse(22113344)


#check true if any number of even in inside a list
def check_even_number(num_lst):
    for i,index in enumerate(num_lst):# if I want the index to start from 1 it can be done by start = 1
        if i % 2== 0:
            print(f"Number {i} at {index} is even")
        else:
            pass
check_even_number([1,2,4,3,2,1,134,1])       

# average of 3 numbers
def avg(a, b, c):
    the_avg = (a+b+c)/3 
    print(the_avg)
avg(12,34,1)    

#Return number if any number is even inside of a list
def check_even (num_list):
    even_number = []
    for i in num_list:
        if i %2 == 0:
            even_number.append(i)
        else:
            pass
    print( even_number )    
check_even([1,123,1,123,123,4,45,234,13,42,424,13,1242,5252,4])        

#write a basic program to check fro emp-loyee of the month 
work_hours = [('Shivam' , 167) , ('jaiho' , 120) , ('Max' , 132)]
def emp_check(work_hours):
    current_max = 0
    employee_of_month =''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours 
            employee_of_month = employee
        else:
            pass
    print(employee_of_month , hours)       
result = emp_check(work_hours)     

#write a funtion to print the e=lenght of a list 
def the_len(list):
        print(len(list))
   
list = [123,13,34,31,34,23413,13,4234,2312,3123,1]
the_len(list)

#write a program to find facotirla of n 
def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact *= i  
    print(fact) 
number= 5
factorial(number )        