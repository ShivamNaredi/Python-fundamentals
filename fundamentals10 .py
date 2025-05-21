#OOPs
#To map with real world scenarios we started using object in code 
#This is called object oriented programming 
class Dog():
    #Class Object Attirbute
    #Same for any instance of a class
    species = 'mammal'
    
    
    def __init__(self,mybreed , name):
    #attirbute 
    # We take in the argument 
    # Assign it using self.attribute_name 
        self.mybreed= mybreed
        self.name = name 
        
    #opertions/Actions --> methods 
    def bark(self , number):
        print("WOOF! My name is {} and the number is {}".format(self.name , number))
my_dog = Dog(mybreed ='lab', name = 'Sam' )
print(my_dog.mybreed)



class Circle():
    
    # Class Object attributes 
    pi = 3.14
    
    def __init__(self , radius =1):
        self.radius = radius
        
    #method 
    def get_circumfarance(self):
        return self.radius * self.pi * 2
my_circle = Circle(30)

print(my_circle.pi)
print(my_circle.radius)       
print(my_circle.get_circumfarance())
        
class Dog():
    def __init__(self , breed , name , spots):
        
        species = 'mammal'
        
        self.breed = breed 
        self.name = name 
        
        
        self.spots = spots 
        
my_dog = Dog(breed = 'Lab' , name = 'sam' , spots = 'True')  
print(my_dog.breed)             