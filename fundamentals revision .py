print("Hello world ")
name = "shivam"
age = 30
print(name)
print(age)
x = 0 
def shivam():
    global x  # Declare x as global to modify the outer variable
    while x < 5:
        print(f' The current value is {x}')
        x = x + 1
print (shivam())


name = "Shivam"
age = 21 
print(type(name))
print(type(age))

name1 = "sk"
name2 = "'sk'"
print (name1 , name2)

a = None 
print(type(a))
b = True
print(type(b))

# their are 33 keywords 
a = 5
b = 6
print(a+b)
sum = a+b
#Operator
#Arithmetic operator   +, - , * , /(divide) , %(reminder)  , **(power)
a= 6
b = 7
print(a / b)
print(a ** b)
print(a % b)

#Relational operator  == , != , > , < , >= , <=   
a = 50 
b = 20 
print(a == b)  # returns a bollean value 
print( a != b)
print(a >= b)
print(a <= b)
print(a < b)
print(a > b)

#Assignment operator  = , += , -= , *= , /= , %= , **= , //=
a = 10 
b = 5
a += b
print(a)
print("a :", a)
number = 345
number *= 10
number /= 10
print(number )

#Logical operator  and , or , not
print(not True)
a= 12
b = 20 
print(not (b>a))

a = 10 
b = 20 
if b > a:
    print (f'and operator {a} and {b}')
print(" OR operator:" , ( a==b) or (a<b))    


a= 2
b = 4.424
sum = a + b
print(sum)

#type casting 
a= int("2")   # force fully converting one data type to another
b = 4.235
print (a + b)
print(type(a))

a = 425
a = str(a)
print(type(a))

# #INput in python
# name = input("Enter your name :")
# print("Your name is :" , name)
# house = int(input("Enter your house number :"))
# print("House number is :" , house) 
# result = int(input("enter the reuslt:"))
# print (result)
# print (type(result))
# age = float(input(" Enter the age :"))
# print(age)
# num1 = int(input("enter the number1:"))
# num2 = int(input("enter the number2:"))
# print (num1 +num2)
# print("Sum = " , num1 +num2 )


# side = float(input('"Enter the value of side:'))
# print("area" , side *side )
# Area = side**2
# print(Area)

# a = float(input("Enter the value of a:"))
# b = float(input("Enter the value of b:"))

# print ("Average = " , (a+b)/2)


# a = int(input ("ENter the value of a:"))
# b = int(input("Enter the value of b:"))
# # if a >= b:
# #     print (True)
# print((a>=b))




#LECTURE2 
#Strings and Conditional statements


# shivam = int(input(" Enter a grade:"))
# if shivam >= 90:
#     print ("Grade A")

# Escape sequence characters 
str1 = "this is shivam naredi. \nI hope you are doing well"
print(str1)


#String operations 
#1.  Concatination of a string 
a = "Shivam"
b = " Naredi"
print(a+b)
#2.  Lenght funtion 
print(len(str1))
len1 = len(a+b)
print(len1)

#3.  Indexing
str = "Shivam Naredi"
print(str[4])


#4.  Slicing
# ending index is not included 
str = "Shivam Naredi"
print(str[0:6])
print(str[2:6])
print(str[7:len(str)])
print(str[6:]) # automatically goes to the end
print(str[:6]) # automatically goes to the beginning 
#negative indexing 
# -1 is the last element.
print(str[-1])
print(str[-5:-1])

#string funtions 
str = " My name is Shivam Naredi"
print(str.endswith("Naredi"))
print(str.endswith("Na"))
print(str.endswith("me"))

#for capitalizing the first char we use .capitalize() function
str1 = "i am a student at JDCOEM"
str1 = str1.capitalize()
print(str1)

str = "I am studing python."
print(str.replace("am" , "was"))

#Find syntax is used to return the 1st index of the 1st occurance of the particular word
str = "I am studing python."
print(str.find("python"))

#count funtion counts the occurance of a particular word ina string 
str = "I am am am am am studing python."
print(str.count("am"))


#for finding more string funtions you can use str.
#important are endswith , capitilize , replace , find , count 
# user = input("Eter your name:")
# print(len(user))
# print("lenght of the name is" , len(user))

str = "Hello everyone i am $hivam one of the largest konwn individual in the college"
print(str.count("$"))


#conditional statements
#if - elif - else 
# if(condition):
#     what ever you want over here 
# else:
#     what ever you want over here

#yaha se bhoot important hai 
# age = int(input("ENter yopur age"))
age = 21
if(age >=18):
    print("Ajao vote karne ")
else:
    print("chalo beta ghar jao")    

light = "red"
if (light == "green"):
    print("Bhago ")
elif (light == "Yellow"):
    print("DHreee karlo")
elif (light == "red"):
    print("Ruko")
else:
    print("Signal hi nahi hai")    

#you can also take user input for the above example 
num = 5
if( num > 2):
    print("Greater than 2")
elif(num >3):
    print("Greater than 3")
else:
    print("I dont know ")     

# marks = int(input("Enter your marks: "))
# if(marks >=90):
#     print("Your grade is A")
# elif(marks >=80 and marks < 90):
#     print("Your grade is B")
# elif(marks >=70 and marks < 80):
#     print("Your grade is C")
# else:
#     print("Your grade is D")


# marks = int(input("Enter your marks: "))
marks = 91
if(marks >=90):
    grade ="A"
elif(marks >=80 and marks < 90):
    grade = "B"
elif(marks >=70 and marks < 80):
    grade = "C"
else:
    grade ="D"

print("Grade of the student ->" , grade)        



#Nesting 
# age = 34
# id = input("Do you have ID Enter Y or N")
# if(age >= 18):
#     if(id == "y"):
#         print("You are ellgible for vote ")
# else:
#     print("Chalo beta ghar jao ")

age = 24
if (age >= 18) :
    if (age<80) :
        print ("you can drive the vehicle")
else:
    print ("NA HO PAYGA ")         

    #practice questions 
# num = int(input("Enter the number: "))
# if (num%2 == 0):
#     print("Number is even")
# else:
#     print("Number is odd")
           
# num1 = int(input("Enter the number:" ))
# num2 = int(input("Enter the number:" ))
# num3 = int(input("Enter the number:"))

# if (num1> num2 and num1>num3):
#     print("Num1 is the largest")
# elif(num2>num1 and num2>num3):
#     print("Num2 is largest")
# else:
#     print("num3 is the largest ")        


number = 48

if (number % 7 ==0):
    print("Number is multiple of 7")
else:
    print("not a multiple ")    


#nesting
age = 24
if(age >= 18):
    if(age <= 80):
        print("You can drive the vehicle ")
    else:
        print("Cannot Drive ")
else:
    print(" Cannot Drive ")

# num1 = int(input("Enter a number: "))
# # num2 = int(input("Enter a number: "))
# # num3 = int(input("Enter a number: "))
# # # if(num%2 == 0):
# # #     print("Even")
# # # else:
# # #     print("Odd")
# # if (num1 > num2 and num1 > num3):
# #     print("Num1 is the largest ")
# # elif (num2 > num1 and num2 > num3):
# #     print("Num2 is the largest")
# # else:
# #     print("Num3 is the largest")
# if (num1 %7 == 0):
#     print("Num1 is multiple of 7")

# list and tuples 
#index in python starts from 0
#list are mutaible in python 
marks = [1,2,3,4,5,6,7,8,9]
print(type(marks))
student = ["Shivam" , 99.9 , 18 , "Nagpur"]
print(student[0])
student[0] = "Shivam Naredi"
print(student)
# print(student[4])      error

#list Slicing 
#     list_name[start:end]     ending is not included 
#     list_name[start:end:stepsize]

marks = [89,56,9,6,94,61,94]
print(marks[1:4])
print(marks[:2])
print(marks[2:])
print(marks[:5:2])

#list methods 
list = [ 54,6,264]
list.append(143)
print(list)

list.sort()
print(list)

list.sort(reverse = True)    # sorting in descending order 
print(list)

list.reverse()
print(list)

list.insert(1, 23423)
print (list)

list.pop(1)
print(list)


#Tuples 
# Tuples are immutable in python. Writen with round braces
tup = (1,23,4,4,.2,4.24,3)
print(type(tup))
print(tup[4])
print(tup)

print(tup.index(3))

print(tup.count(4))
print(len(tup))

#WAP to ask a user to enter 3 movie names and store them in a form of list
# list = []
# list = input("Enter the favorite movie name :").split()
# print(list)

# movies = []
# mov1 = input("Enter the movie name 1:")
# mov2 = input("Enter the movie name 2:")
# mov3 = input("Enter the movie name 3:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#WAP to check if a list contains a palindrom of the elements

list = [ 1, "abc" , "abc"  , 1]
list_copy = list.copy()
list_copy.reverse()
if(list == list_copy):
    print("list is palindrom")
else:
    print ("The list is not palindrom")

# tup_1 = ("C" , "D" , "A" , "A" , "B" , "B" , "A")
# # # print(tup.count("A")) # count of A in the tuple
# # list1 = list(tup)
# # list1.sort()
# # print(list1)
# print(sorted(list(tup_1)))

