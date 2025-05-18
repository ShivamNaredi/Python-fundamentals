def conversion(money):
    USD = money *83
    print(USD)
conversion(2)


#small game of shuffle 

# #Shuffle mylist
# from random import shuffle
# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist   


# #pick a number/guess
# def number_guess():
#     guess=''
#     while guess not in ['0' , '1' , '2']:
#         guess = input("Pick a number: 0, 1, 2")
#     return(int(guess))    
        
# #check guess 
# def check_guess(mylist , guess):
#     if mylist[guess] == 'o':
#         print("Correct Guess")
#     else:
#         print("Try again")
#         print(f"The correct guess was {mylist}")    
        
# #create mylist
# # mylist = [ '' , 'o' , '' ]        
# # shuffled_list = shuffle_list(mylist)
# # guess =  number_guess()
# # check_guess(shuffled_list , guess)

#write me a programm to captilize 1st and 4 th letter in a list 
def mylist_letter(name):
    if len(name) <4:
        return "Enter the name that contain more than 4 letters"
    list_letter = list(name)
    list_letter[0] = list_letter[0].upper()
    list_letter[3] = list_letter[3].upper()
    return ''.join(list_letter)
print (mylist_letter("shivam"))   
        
        