# Break and Continue statemnet 
#Break : used to treminate the program 
# Reversing a number using a while loop
number = 314324
Rev_number = 0
while number > 0:
    random = number % 10
    number = number // 10
    Rev_number = Rev_number * 10 + random  
print(f"The reversed number is {Rev_number}")

i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue 
    print(i)
    i += 1

#Some of numbers 
num = 1641565
sum_of_digits = 0
while num > 0:
    digit = num % 10          
    sum_of_digits += digit   
    num = num // 10           
print("Sum of digits is:", sum_of_digits)

#printing of even numbers 
i = 0 
while i <= 10:
    if (i % 2 !=0):
        i +=1 
        continue 
    print(i)
    i+=1