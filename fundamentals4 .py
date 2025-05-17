#For loops in python 
#Loop are used for sequenctial traversal 

for i in range(1 , 11):
    print(i)
print("\n")

for i in range( 0 , 21 , 2):
    print (i)  
# for i in range(0 , 21):
#     if (i % 2 == 0):
#         print(i)

n = 5
total = 0
for i in range(1 , n+1):
    total = total + i
print (total)


# Paterrn making 
rag = 5
for i in range(1 , rag+1):
    print ("*" * i)
#for numbers 
rows = 5 
for i in range(1 , rows+1):
    for j in range ( 1 , i + 1 ):
        print(j , end="")
    print()
# Reversed triangle 
rows = 5
for i in range (rows , 0 , -1):   # this is do the counting in decreasing order 
    for j in range(1 , i+1 ):
        print("*" , end="")
    print()    

#pyramid
rows = 5
for i in range(1 , rows +1):
    for j in range(rows - i):
        print(" " , end = "")
    
    for k in range(2 * i - 1):
        print("*" , end= "")
        
    print()

#inversed pyramid 
rows= 5
for i in range(rows, 0 , -1 ):
    for j in range(rows - i ):
        print(" " , end="")
    
    
    for k in range( 2 * i - 1):
        print("*" , end="")
    
    print()    
    
        
# square 
rows = 5
for i in range(1 , rows +1):
    print("*" *rows)
    
# square number 
rows= 5
for i in range(1 , rows+1):
    for j in range(rows+1):
        print(j , end ="")
    print()        