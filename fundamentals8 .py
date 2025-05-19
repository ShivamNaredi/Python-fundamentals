#Recursion 
#When a funtion call itself repeatedly

def showe(n):
    if n == 0:
        return
    print(n)
    showe(n - 1)
showe(4)    

def fact(n):
    if( n ==0 or n ==1):
        return 1
    else:
        return n * fact(n-1)  # n! = (n-1)! x n   (! = factoral)
print(fact(12))   

#write a rescursive funtion to calcalate sum of n natural numbers
def natural(n):
    if n == 1:
        return 1
    else:
        return n + natural(n-1)
print(natural(5))

# write a recursive funtion to print all elements in a list 

def the_list(mylist , index =0):
    if index == len(mylist):
        return 
    print(mylist[index])
    the_list(mylist , index +1)
 
the_list(["Shivam", "Naredi", "AI", "ML"])
the_list([1,23,42,3,4,21,45])    