''' Compare Two Numbers
Prompt twice for an integer. Print the larger of the two numbers, or print a message indicating they are equal.
'''
print(" Compare Two Numbers ")
num1=int(input("please enter first integer number: "))
num2=int(input("please enter second integer number: "))
if num1 > num2 :
    print("the large number is ", num1)
elif num1 < num2 :
    print("the large number is ", num2)
elif num1 == num2 :
    print(num1,"is equal", num2 )
else :
    print("invalid input , please enter an integer number ")
