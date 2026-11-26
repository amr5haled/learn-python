'''Ask the user to enter multiple numbers on one line separated by spaces. Split them into a list, loop through them, and display only numbers > 0.
'''
nums=input('enter multiple numbers on one line separated by spaces :  ')
for i in nums.split(" "):
    if int(i) > 0:
        print(i)
