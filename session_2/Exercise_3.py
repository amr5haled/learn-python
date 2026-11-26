
'''Inclusive Range Sum
Prompt twice for an integer (e.g., 10 and 15). Calculate and print the sum of all integers between them inclusively (10+11+12+13+14+15 = 75).
'''
num1=int(input("please enter first integer number: "))
num2=int(input("please enter second integer number: "))
total=0
for i in range(num1,num2+1):
    total=i+1  
for n in range(num1,num2):
    print(n, end="+")
print(num2,"=",total)