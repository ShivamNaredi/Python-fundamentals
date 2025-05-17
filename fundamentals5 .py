# further of for loop (easy then previous one)
str = "Shivam"
for i in str:
    if(i == 'a'):
        print("A found ")
        break
    print(i)

else:
    print("ki Jai ho")
    #why this above case     
    #we use this in case of break (meko bhi nahi smajha)
    
#using for loop find a desired number in the list 
x = [1,234,234,1,1,3,34,12321,24,234,1,1,42,24,2]
y = 1
idx = 0
for i in  x:
    if(i == y) :   
        print("Number found at Index " , idx)
    idx += 1  
    
    
# range funtion can also be used individually aside from for loop
# pass statement 
#--> pass is a null statement that does nothing. It is used as a placeholder for future code 
for i in range(5):
    #empty
    pass
print("END")


#WAP to priont the sum of first n numbers
n = 5
sum = 0
for i in range(1 , n +1):
    sum += i
print(sum)    
  
# printing factorial of a number 
n = 5
fact = 1
for i in range(1 , n+1):
    fact *= i
print(fact)


# next we will discuss funtions 
