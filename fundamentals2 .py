#CHAPTER 4 - Dictonary and sets
dict = { "Shivam" : "Naredi" , "age" : 21 , "college" : "JDCOEM" , "is adult" : True , "Marks" : 99.9 ,
         "Subjets" : ["maths" , "DAA"]}
print(type(dict))
#dict are muttable in python
#Dont allow duplicate keys    (keys:value)

print(dict["Shivam"])
print(dict["Subjets"])
print(dict["age"])
dict["Shivam"] = "Agrawal"
print(dict["Shivam"]) #overwrite 

#Empty dictinory or null dictnoary
null_dict = {}
null_dict = {"Dj" : "Bravo"}
print(null_dict)

#nested dictonary
student= {
    "name" : "Shivam Naredi" , 
    "Subjects" :{
        "English" : 90, 
        "Hindi" : 82
    }
}
print(student ["Subjects"])
#typecast in the form of list 
print(list(student.keys()))
#dictonary methods 
# .keys() , .values() , .items()
# .copy() , .clear() , .pop() , .update() , .get()

dict = {"Name" :"Shivam Naredi" , 
        "age" : 21}
print(list(dict.values()))
student= {
    "name" : "Shivam Naredi" , 
    "Subjects" :{
        "English" : 90, 
        "Hindi" : 82
    }
}
new_student = {"city" : "Nagpur" , "age" : 21} # values sepreated by comma are another keyvalue pair 
# their is no duplicate value is allowed therefore while updating previous value will be overwritten 
student.update(new_student)
print(student)
# pairs = list(student.items())
# print(pairs[0])
# print(student["name"])  #error 
# print(student.get["name"])  #no error -> None 


#SET in python
#Set is a collection of unordered and unindexed elements
#Each element in the set must be uniuqe and immutable , but set itself is mutable(add or remove values)
#Tuple can be used as a set but list and dict cannot be used 
nums = {1,2,3,4,5,6}
shivam = {2,3,4,2,3,3,2,"shivam"}
print(shivam) # Duplicate values are removed while using set ## but it will be in unorrdered form
print(type(nums))
print(len(shivam)) #lenght will also not include duplicate values 

#-->How to create an Empty set
example = {} # wrong way as it will create a empty dict 
example_2 = set() # correct way to create a empty set
print(type(example_2))

#Methods of set 
collection = set()
collection.add(1)
collection.add(2)
collection.add((1,2,3)) #tuple can be added in a list 
# collection.add([1,2,3]) # list cannot be added in a set
# collection.remove(1)
print(collection)

#clear method 
print(len(collection))
collection.clear()
print(collection)
Data = {"Hello" , "Shivam" , "nice" , "Meeting" ,"you"}
print(Data.pop()) #used to pop a random element from the set 
print(Data.pop()) #used to pop a random element from the set 

#Union and intersection method --> Improtant 
#set.union(set2) # combines both set values and return new set
#set.intersection(set2) # combines common values from both set return new set
set1 = {1,2,3,4}
set2 = {3,24,54,1,12,4,5,6}

print(sorted(set1.union(set2)))
print(set1.intersection(set2))

#practice 
dict_cat = {"table": ["a peice of furniture" , "list of facts and figure"] , 
            "cat": "a small animal" }
print(dict_cat["table"][1])

list= ["python" , "java" , "c++" , "C" , "python" , "java" , "c++" , "Javascript"]
subject = set(list)
print(len(subject))


# subjects = {}
# x = int(input("Enter the marks of the English :"))
# subjects.update({"English" : x})
# x = int(input("Enter the marks of the Maths :"))
# subjects.update({"Maths" : x})
# x = int(input("Enter the marks of the Programming :"))
# subjects.update({"Programming" : x})
# # subjects.update({"English" : 97})
# # subjects.update({"Programming" : 85})
# # subjects.update({"Maths" : 99})
# print(subjects)

#--> How can you store two value such as a int and a flaot in set as different value
set = {(1, int) , (1.0 , float)}
set = {1 , "1.0"} #or you can convert one value as a string
print(set)

print("Shivam Naredi")