
'''
Integer Checker
Prompt the user for a lucky number. Print a message if the input is NOT an integer (Hint: check .isdigit() or handle signs).
Extend Exercise 1: if the entered value IS a valid integer, also print how many digits are in that number.

'''
num=input("Enter a lucky number: ")
if num.isdigit() == True :
    print("your lucky number is ",num)
    print("The length of number is : ", len(num))
else:
    print("invaled input please enter a integer number ")
