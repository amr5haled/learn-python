
'''
Integer Checker
Prompt the user for a lucky number. Print a message if the input is NOT an integer (Hint: check .isdigit() or handle signs).
'''
num=input("Enter a lucky number: ")
if num.isdigit() == True :
    print("your lucky number is ",num)
else:
    print("invaled input please enter a integer number ")
